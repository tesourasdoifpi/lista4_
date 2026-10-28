def calcular_s(n):
    # 1. Validação estrita de tipo (apenas int, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. O enunciado exige valor estritamente positivo (n > 0)
    if n <= 0:
        return Exception

    soma = 0.0
    for i in range(1, n + 1):
        soma += 1 / i

    return soma


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# n = 1 -> S = 1
assert calcular_s(1) == 1.0

# n = 2 -> S = 1 + 1/2 = 1.5
assert calcular_s(2) == 1.5

# n = 3 -> S = 1 + 1/2 + 1/3 = 1.8333333333333333
assert round(calcular_s(3), 4) == 1.8333

# n = 4 -> S = 1 + 1/2 + 1/3 + 1/4 = 2.083333333333333
assert round(calcular_s(4), 4) == 2.0833

# n = 5 -> S = 1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283333333333333
assert round(calcular_s(5), 4) == 2.2833


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Zero e valores negativos (não são positivos)
assert calcular_s(0) == Exception
assert calcular_s(-1) == Exception
assert calcular_s(-5) == Exception
assert calcular_s(-100) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando int)
assert calcular_s(True) == Exception
assert calcular_s(False) == Exception

# Floats
assert calcular_s(5.0) == Exception
assert calcular_s(2.5) == Exception

# Strings, None e coleções
assert calcular_s("5") == Exception
assert calcular_s("N") == Exception
assert calcular_s(None) == Exception
assert calcular_s([5]) == Exception
assert calcular_s((5,)) == Exception
assert calcular_s({"n": 5}) == Exception

print("Todos os testes passaram com sucesso!")