import numpy as np
import re
from collections import Counter
from glob import glob
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import umap.umap_ as umap
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from nltk.corpus import stopwords
import nltk
from unidecode import unidecode

nltk.download('stopwords')

# Listar todos os arquivos CSV no diretório
file_paths = glob('C://Users//pc//Desktop//Pdpd_2023//observ_label//*.csv')

stop_words_pt = set(stopwords.words('portuguese'))
stop_words_en = set(stopwords.words('english'))

# Função para limpar o texto
def clean_text(text):
    # Remover links
    text = re.sub(r'http\S+', '', text)
    # Remover emojis
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Remover acentos e caracteres especiais
    text = unidecode(text)
    # Remover símbolos e sinais de pontuação
    text = re.sub(r'[^\w\s]', '', text)
    # Converter para minúsculas
    text = text.lower()
    # Remover stop words e palavras com menos de 4 caracteres
    words = [word for word in text.split() if word not in stop_words_pt and word not in stop_words_en and len(word) >= 4]
    return ' '.join(words)

# Função para processar um arquivo CSV
def process_csv(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        yield row['screen_name'], row['rtfrom'], row['text'], pd.to_datetime(row['created_at']).strftime('%b_%Y')

# Dicionário para armazenar os termos mais frequentes por rtfrom
rtfrom_top_terms_dict = {}

# Construir o dicionário de índices dos termos mais frequentes
term_index_dict = {}
index = 0

# Iterar sobre cada arquivo CSV
for file_path in file_paths:
    for screen_name, rtfrom, text, created_at in process_csv(file_path):
        # Verificar se o rtfrom existe
        if rtfrom and rtfrom != screen_name:
            # Processar o texto
            cleaned_text = clean_text(text)
            words = cleaned_text.split()

            # Contar a frequência dos termos com pelo menos 4 letras
            term_freq = Counter(word for word in words if len(word) >= 4)
            if rtfrom not in rtfrom_top_terms_dict:
                rtfrom_top_terms_dict[rtfrom] = Counter()
            rtfrom_top_terms_dict[rtfrom].update(term_freq)

            # Atualizar o dicionário de índices
            for term in term_freq.keys():
                if term not in term_index_dict:
                    term_index_dict[term] = index
                    index += 1

# Dicionário para armazenar os vetores de termos por screen_name agrupados por mês
monthly_screen_name_vectors = {}

# Dicionário para armazenar o número de vetores adicionados por screen_name
num_vectors_added = {}

# Dicionário para armazenar os vetores de termos por rtfrom agrupados por mês
monthly_rtfrom_vectors = {}

# Dicionário para armazenar o número de vetores adicionados por rtfrom
num_rtfrom_added = {}

# Iterar sobre cada arquivo CSV novamente
for file_path in file_paths:
    for screen_name, rtfrom, text, created_at in process_csv(file_path):
        # Verificar se o rtfrom existe
        if rtfrom and rtfrom != screen_name:
            # Processar o texto
            cleaned_text = clean_text(text)
            words = cleaned_text.split()

            # Verificar se o screen_name já está no dicionário para o mês atual
            if created_at not in monthly_screen_name_vectors:
                monthly_screen_name_vectors[created_at] = {}
                num_vectors_added[created_at] = {}
                monthly_rtfrom_vectors[created_at] = {}
                num_rtfrom_added[created_at] = {}

            if screen_name not in monthly_screen_name_vectors[created_at]:
                monthly_screen_name_vectors[created_at][screen_name] = np.zeros(len(term_index_dict))
                num_vectors_added[created_at][screen_name] = 0

            if rtfrom not in monthly_rtfrom_vectors[created_at]:
                monthly_rtfrom_vectors[created_at][rtfrom] = np.zeros(len(term_index_dict))
                num_rtfrom_added[created_at][rtfrom] = 0

            # Adicionar o vetor de termos para o screen_name se ainda não atingiu o limite
            if num_vectors_added[created_at][screen_name] < 7:
                for word in words:
                    if word in term_index_dict:
                        term_index = term_index_dict[word]
                        monthly_screen_name_vectors[created_at][screen_name][term_index] = 1
                num_vectors_added[created_at][screen_name] += 1

            # Adicionar o vetor de termos para o rtfrom se ainda não atingiu o limite
            if num_rtfrom_added[created_at][rtfrom] < 7:
                for word in words:
                    if word in term_index_dict:
                        term_index = term_index_dict[word]
                        monthly_rtfrom_vectors[created_at][rtfrom][term_index] = 1
                num_rtfrom_added[created_at][rtfrom] += 1

            # Adicionar o vetor do rtfrom ao screen_name se existir
            if rtfrom in monthly_screen_name_vectors[created_at]:
                monthly_screen_name_vectors[created_at][screen_name] += monthly_screen_name_vectors[created_at][rtfrom]

# Calcular a similaridade de cosseno entre os vetores de termos dos screen_name para cada mês
monthly_similarity_matrices = {}
for month, screen_name_vectors in monthly_screen_name_vectors.items():
    screen_name_vectors_list = list(screen_name_vectors.values())
    similarity_matrix = cosine_similarity(screen_name_vectors_list)
    monthly_similarity_matrices[month] = similarity_matrix

# Exibir os pontos no espaço bidimensional para cada mês com cores representando a similaridade
for month, similarity_matrix in monthly_similarity_matrices.items():
    plt.figure(figsize=(10, 6))
    plt.scatter(similarity_matrix[:, 0], similarity_matrix[:, 1], c=similarity_matrix.mean(axis=0), cmap='coolwarm', alpha=0.5)
    plt.title(f'Projeção dos Usuários - {month}')
    plt.xlabel('Componente 1')
    plt.ylabel('Componente 2')
    plt.colorbar(label='Similaridade')
    plt.show()
