def potencia(x, z):
    # 1. Validação estrita de tipo: base pode ser int ou float; expoente deve ser int
    if type(x) not in (int, float) or type(z) != int:
        return Exception

    # 2. Barrar NaN (x != x identifica NaN sem dependência de math)
    if x != x:
        return Exception

    # 3. Barrar valores infinitos na base
    if x == float("inf") or x == float("-inf"):
        return Exception

    # 4. Caso indeterminado: 0 elevado a expoente menor ou igual a zero (0^0 ou divisão por zero)
    if x == 0 and z <= 0:
        return Exception

    # 5. Cálculo por multiplicações sucessivas sem funções/operadores de potência prontos
    resultado = 1
    expoente_positivo = z if z >= 0 else -z

    for _ in range(expoente_positivo):
        resultado *= x

    # Se o expoente original for negativo: x^(-z) = 1 / (x^z)
    if z < 0:
        return 1 / resultado

    return resultado


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# Expoentes positivos
assert potencia(2, 3) == 8
assert potencia(5, 2) == 25
assert potencia(3, 4) == 81
assert potencia(10, 5) == 100000

# Base negativa com expoente par e ímpar
assert potencia(-2, 3) == -8
assert potencia(-2, 4) == 16

# Base com ponto flutuante (float)
assert potencia(0.5, 2) == 0.25
assert potencia(1.5, 2) == 2.25

# Expoente zero (qualquer base não nula elevada a zero é 1)
assert potencia(2, 0) == 1
assert potencia(-5, 0) == 1
assert potencia(7.5, 0) == 1

# Base zero com expoente positivo
assert potencia(0, 3) == 0

# Expoentes negativos
assert potencia(2, -1) == 0.5
assert potencia(2, -2) == 0.25
assert potencia(4, -2) == 0.0625
assert potencia(-2, -3) == -0.125


# ========================================================
# 2. ENTRADAS COM VALORES MATEMATICAMENTE INVÁLIDOS (Exception)
# ========================================================

# Indeterminações e divisões por zero com base 0
assert potencia(0, 0) == Exception
assert potencia(0, -1) == Exception
assert potencia(0, -3) == Exception

# Base infinita ou NaN
assert potencia(float("inf"), 2) == Exception
assert potencia(float("-inf"), 2) == Exception
assert potencia(float("nan"), 2) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando int)
assert potencia(True, 3) == Exception
assert potencia(2, False) == Exception

# Expoente não inteiro (a potência iterativa exige expoente inteiro)
assert potencia(2, 2.5) == Exception
assert potencia(4, 0.5) == Exception

# Strings, None e coleções
assert potencia("2", 3) == Exception
assert potencia(2, "3") == Exception
assert potencia(None, 2) == Exception
assert potencia(2, None) == Exception
assert potencia([2], 3) == Exception
assert potencia(2, (3,)) == Exception
assert potencia({"x": 2}, 3) == Exception

print("Todos os testes passaram com sucesso!")