def calcular_s_polinomial(n):
    # 1. Validação estrita de tipo (apenas int, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. O enunciado exige valor estritamente positivo (n > 0)
    if n <= 0:
        return Exception

    soma = 0.0
    for i in range(1, n + 1):
        numerador = (i ** 2) + 1
        denominador = i + 3
        soma += numerador / denominador

    return soma


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# n = 1 -> S = (1^2 + 1) / (1 + 3) = 2/4 = 0.5
assert calcular_s_polinomial(1) == 0.5

# n = 2 -> S = 0.5 + (2^2 + 1) / (2 + 3) = 0.5 + 5/5 = 1.5
assert calcular_s_polinomial(2) == 1.5

# n = 3 -> S = 1.5 + (3^2 + 1) / (3 + 3) = 1.5 + 10/6 = 3.1666666666666665
assert round(calcular_s_polinomial(3), 4) == 3.1667

# n = 4 -> S = 3.1666... + (4^2 + 1) / (4 + 3) = 3.1666... + 17/7 = 5.595238...
assert round(calcular_s_polinomial(4), 4) == 5.5952

# n = 5 -> S = 5.5952... + (5^2 + 1) / (5 + 3) = 5.5952... + 26/8 = 8.845238...
assert round(calcular_s_polinomial(5), 4) == 8.8452


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Zero e valores negativos (não são positivos)
assert calcular_s_polinomial(0) == Exception
assert calcular_s_polinomial(-1) == Exception
assert calcular_s_polinomial(-5) == Exception
assert calcular_s_polinomial(-100) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando comportamento de int)
assert calcular_s_polinomial(True) == Exception
assert calcular_s_polinomial(False) == Exception

# Ponto flutuante
assert calcular_s_polinomial(5.0) == Exception
assert calcular_s_polinomial(2.5) == Exception

# Strings, None e coleções
assert calcular_s_polinomial("5") == Exception
assert calcular_s_polinomial("N") == Exception
assert calcular_s_polinomial(None) == Exception
assert calcular_s_polinomial([5]) == Exception
assert calcular_s_polinomial((5,)) == Exception
assert calcular_s_polinomial({"n": 5}) == Exception

print("Todos os testes passaram com sucesso!")