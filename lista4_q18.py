def tabuada(n):
    # 1. Validação estrita de tipo (apenas inteiros, barrando bool, float, etc.)
    if type(n) != int:
        return Exception

    # 2. Como a tabuada vai de 1 até N, N deve ser um inteiro positivo (N >= 1)
    if n < 1:
        return Exception

    linhas = []
    for i in range(1, n + 1):
        resultado = i * n
        linha = f"{i} x {n} = {resultado}"
        print(linha)
        linhas.append(linha)

    return linhas


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# N = 1 (1 x 1 = 1)
assert tabuada(1) == [
    "1 x 1 = 1"
]

# N = 3
assert tabuada(3) == [
    "1 x 3 = 3",
    "2 x 3 = 6",
    "3 x 3 = 9"
]

# N = 5
assert tabuada(5) == [
    "1 x 5 = 5",
    "2 x 5 = 10",
    "3 x 5 = 15",
    "4 x 5 = 20",
    "5 x 5 = 25"
]


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Valores menores que 1 (zero e negativos)
assert tabuada(0) == Exception
assert tabuada(-1) == Exception
assert tabuada(-5) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando int)
assert tabuada(True) == Exception
assert tabuada(False) == Exception

# Floats
assert tabuada(5.0) == Exception
assert tabuada(3.14) == Exception

# Strings, None e coleções
assert tabuada("5") == Exception
assert tabuada("N") == Exception
assert tabuada(None) == Exception
assert tabuada([5]) == Exception
assert tabuada((5,)) == Exception
assert tabuada({"n": 5}) == Exception

print("Todos os testes passaram com sucesso!")