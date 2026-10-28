def somatorio(n):
    # 1. Validação estrita de tipo (apenas int, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. O enunciado exige valor estritamente positivo (n > 0)
    if n <= 0:
        return Exception

    # Fórmula da soma de Gauss: n * (n + 1) // 2
    return n * (n + 1) // 2


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# n = 1 -> 1
assert somatorio(1) == 1

# n = 2 -> 1 + 2 = 3
assert somatorio(2) == 3

# n = 3 -> 1 + 2 + 3 = 6
assert somatorio(3) == 6

# n = 5 -> 1 + 2 + 3 + 4 + 5 = 15
assert somatorio(5) == 15

# n = 10 -> 1 + 2 + ... + 10 = 55
assert somatorio(10) == 55

# n = 100 -> 5050
assert somatorio(100) == 5050


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Zero e valores negativos (não são positivos)
assert somatorio(0) == Exception
assert somatorio(-1) == Exception
assert somatorio(-5) == Exception
assert somatorio(-100) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando int)
assert somatorio(True) == Exception
assert somatorio(False) == Exception

# Floats
assert somatorio(5.0) == Exception
assert somatorio(3.14) == Exception

# Strings, None e coleções
assert somatorio("5") == Exception
assert somatorio("dez") == Exception
assert somatorio(None) == Exception
assert somatorio([5]) == Exception
assert somatorio((5,)) == Exception
assert somatorio({"n": 5}) == Exception

print("Todos os testes passaram com sucesso!")