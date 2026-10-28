def calcular_s_fatorial(n):
    # 1. Validação estrita de tipo (apenas int, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. O enunciado exige valor estritamente positivo (n > 0)
    if n <= 0:
        return Exception

    soma = 1.0
    fatorial = 1

    # Atualiza o fatorial a cada passo: i! = (i - 1)! * i
    for i in range(1, n + 1):
        fatorial *= i
        soma += 1 / fatorial

    return soma


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# n = 1 -> S = 1 + 1/1! = 1 + 1 = 2.0
assert calcular_s_fatorial(1) == 2.0

# n = 2 -> S = 1 + 1/1! + 1/2! = 1 + 1 + 0.5 = 2.5
assert calcular_s_fatorial(2) == 2.5

# n = 3 -> S = 2.5 + 1/6 = 2.6666666666666665
assert round(calcular_s_fatorial(3), 4) == 2.6667

# n = 4 -> S = 2.6666... + 1/24 = 2.7083333333333335
assert round(calcular_s_fatorial(4), 4) == 2.7083

# n = 5 -> S = 2.708333... + 1/120 = 2.716666666666667
assert round(calcular_s_fatorial(5), 4) == 2.7167


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Zero e valores negativos (não são positivos)
assert calcular_s_fatorial(0) == Exception
assert calcular_s_fatorial(-1) == Exception
assert calcular_s_fatorial(-5) == Exception
assert calcular_s_fatorial(-100) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando comportamento de int)
assert calcular_s_fatorial(True) == Exception
assert calcular_s_fatorial(False) == Exception

# Ponto flutuante
assert calcular_s_fatorial(5.0) == Exception
assert calcular_s_fatorial(2.5) == Exception

# Strings, None e coleções
assert calcular_s_fatorial("5") == Exception
assert calcular_s_fatorial("N") == Exception
assert calcular_s_fatorial(None) == Exception
assert calcular_s_fatorial([5]) == Exception
assert calcular_s_fatorial((5,)) == Exception
assert calcular_s_fatorial({"n": 5}) == Exception

print("Todos os testes passaram com sucesso!")