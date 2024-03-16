def conceito(nota: float) -> str:
    if nota < 5:
        res = "F"
    else:
        if nota >= 9:
            res = "A"
        elif 7.5 <= nota < 9:
            res = "B"
        elif 6 <= nota < 7.5:
            res = "C"
        elif 5 <= nota < 6:
            res = "D"
        else:
            res = "F"
    return res

nota = float(input("Enter the grade: "))
resultado = conceito(nota)
print(f"The concept for the grade {nota} is {resultado}")
