def contar_divisores(n):
    # 1. Validação estrita de tipo (apenas inteiros, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. O enunciado exige valor estritamente positivo (n > 0)
    if n <= 0:
        return Exception

    total_divisores = 0
    limite = int(n ** 0.5)

    # Itera até a raiz quadrada para garantir complexidade O(sqrt(n))
    for i in range(1, limite + 1):
        if n % i == 0:
            if i * i == n:
                total_divisores += 1
            else:
                total_divisores += 2

    return total_divisores


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# n = 1: apenas {1} -> 1 divisor
assert contar_divisores(1) == 1

# Números primos: apenas 1 e ele mesmo -> 2 divisores
assert contar_divisores(2) == 2
assert contar_divisores(3) == 2
assert contar_divisores(13) == 2
assert contar_divisores(97) == 2

# Quadrados perfeitos (quantidade ímpar de divisores)
# 4 -> {1, 2, 4} -> 3 divisores
assert contar_divisores(4) == 3
# 16 -> {1, 2, 4, 8, 16} -> 5 divisores
assert contar_divisores(16) == 5

# Números compostos comuns
# 6 -> {1, 2, 3, 6} -> 4 divisores
assert contar_divisores(6) == 4
# 12 -> {1, 2, 3, 4, 6, 12} -> 6 divisores
assert contar_divisores(12) == 6
# 28 -> {1, 2, 4, 7, 14, 28} -> 6 divisores
assert contar_divisores(28) == 6


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Zero e números negativos (não são positivos)
assert contar_divisores(0) == Exception
assert contar_divisores(-1) == Exception
assert contar_divisores(-6) == Exception
assert contar_divisores(-100) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando comportamento de int)
assert contar_divisores(True) == Exception
assert contar_divisores(False) == Exception

# Ponto flutuante
assert contar_divisores(6.0) == Exception
assert contar_divisores(12.5) == Exception

# Strings, None e coleções
assert contar_divisores("6") == Exception
assert contar_divisores("dez") == Exception
assert contar_divisores(None) == Exception
assert contar_divisores([6]) == Exception
assert contar_divisores((6,)) == Exception
assert contar_divisores({"n": 6}) == Exception

print("Todos os testes passaram com sucesso!")