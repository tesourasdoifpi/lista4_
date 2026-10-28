def media_valores_positivos(valores):
    # 1. Validação do tipo do parâmetro (espera-se lista ou tupla)
    if type(valores) not in (list, tuple):
        return Exception

    # Coleção vazia não permite cálculo de média
    if len(valores) == 0:
        return Exception

    soma = 0.0

    for v in valores:
        # 2. Cada elemento deve ser estritamente int ou float (barrando bool)
        if type(v) not in (int, float):
            return Exception

        # Barrar NaN (x != x identifica NaN sem usar math)
        if v != v:
            return Exception

        # 3. O enunciado exige apenas valores positivos (> 0) e finitos
        if v <= 0 or v == float("inf"):
            return Exception

        soma += v

    return soma / len(valores)


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# Valores inteiros e decimais
assert media_valores_positivos([10, 20, 30]) == 20.0
assert media_valores_positivos([5, 5, 5, 5]) == 5.0
assert media_valores_positivos([2.5, 7.5]) == 5.0
assert media_valores_positivos((1, 2, 3, 4, 5)) == 3.0
assert media_valores_positivos([100]) == 100.0


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Valores iguais a zero ou negativos (não são positivos)
assert media_valores_positivos([0, 10, 20]) == Exception
assert media_valores_positivos([-1, 5, 10]) == Exception
assert media_valores_positivos([-10.5]) == Exception

# Lista/tupla vazia
assert media_valores_positivos([]) == Exception
assert media_valores_positivos(()) == Exception

# Infinito e NaN
assert media_valores_positivos([10, float("inf")]) == Exception
assert media_valores_positivos([float("nan"), 5]) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Booleanos (em Python, type(True) == bool, barrando int)
assert media_valores_positivos([True, 10, 20]) == Exception
assert media_valores_positivos([5, False]) == Exception

# Strings, None e estruturas incorretas
assert media_valores_positivos(["10", 20]) == Exception
assert media_valores_positivos([10, "vinte"]) == Exception
assert media_valores_positivos([None, 5]) == Exception
assert media_valores_positivos([10, [20]]) == Exception

# Tipo do argumento não iterável ou incorreto
assert media_valores_positivos(10) == Exception
assert media_valores_positivos("10, 20, 30") == Exception
assert media_valores_positivos(None) == Exception
assert media_valores_positivos({"a": 1}) == Exception

print("Todos os testes passaram com sucesso!")