def pi() -> float:
    soma = 0
    i = 0
    while i < 1000:
        soma = soma + (-1) ** i / (2 * i + 1)
        i += 1  # Increment i to avoid an infinite loop
    return soma * 4

print(pi())
