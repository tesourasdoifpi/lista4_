def calcular_fatorial(n):
    # 1. Validação estrita de tipo (apenas inteiros, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. Fatorial só é definido para números inteiros não negativos (n >= 0)
    if n < 0:
        return Exception

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# Casos base
assert calcular_fatorial(0) == 1
assert calcular_fatorial(1) == 1

# Fatoriais comuns
assert calcular_fatorial(2) == 2
assert calcular_fatorial(3) == 6
assert calcular_fatorial(4) == 24
assert calcular_fatorial(5) == 120
assert calcular_fatorial(6) == 720
assert calcular_fatorial(7) == 5040
assert calcular_fatorial(10) == 3628800


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Inteiros negativos (não existe fatorial de número negativo)
assert calcular_fatorial(-1) == Exception
assert calcular_fatorial(-5) == Exception
assert calcular_fatorial(-10) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando int)
assert calcular_fatorial(True) == Exception
assert calcular_fatorial(False) == Exception

# Ponto flutuante
assert calcular_fatorial(5.0) == Exception
assert calcular_fatorial(3.14) == Exception

# Strings, None e coleções
assert calcular_fatorial("5") == Exception
assert calcular_fatorial("fatorial") == Exception
assert calcular_fatorial(None) == Exception
assert calcular_fatorial([5]) == Exception
assert calcular_fatorial((5,)) == Exception
assert calcular_fatorial({"n": 5}) == Exception

print("Todos os testes passaram com sucesso!")