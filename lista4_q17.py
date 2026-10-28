import random


def maior_menor_50(valores=None):
    # Se uma lista personalizada não for informada, gera 50 inteiros aleatórios via randint
    if valores is None:
        valores = [random.randint(-1000, 1000) for _ in range(50)]

    # 1. Validação de tipo do parâmetro (deve ser lista ou tupla)
    if type(valores) not in (list, tuple):
        return Exception

    # Deve conter exatamente 50 valores
    if len(valores) != 50:
        return Exception

    # 2. Validação estrita de cada valor (apenas inteiros, barrando bool, float, etc.)
    for v in valores:
        if type(v) != int:
            return Exception

    maior = valores[0]
    menor = valores[0]

    for v in valores[1:]:
        if v > maior:
            maior = v
        if v < menor:
            menor = v

    return maior, menor


# ========================================================
# 1. CASOS VÁLIDOS (GERAÇÃO AUTOMÁTICA E LISTAS DEFINIDAS)
# ========================================================

# Chamada padrão: gera 50 valores com random.randint
maior_gerado, menor_gerado = maior_menor_50()
assert type(maior_gerado) == int
assert type(menor_gerado) == int
assert maior_gerado >= menor_gerado

# Teste com 50 valores definidos manualmente (de 1 a 50)
lista_1_a_50 = list(range(1, 51))
assert maior_menor_50(lista_1_a_50) == (50, 1)

# Teste com 50 valores iguais
assert maior_menor_50([7] * 50) == (7, 7)

# Teste com 50 valores contendo extremos negativos
lista_com_negativos = [-100] + [0] * 48 + [500]
assert maior_menor_50(lista_com_negativos) == (500, -100)


# ========================================================
# 2. ENTRADAS COM QUANTIDADE INCORRETA (Exception)
# ========================================================

# Menos de 50 elementos
assert maior_menor_50([]) == Exception
assert maior_menor_50([1, 2, 3]) == Exception
assert maior_menor_50(list(range(49))) == Exception

# Mais de 50 elementos
assert maior_menor_50(list(range(51))) == Exception
assert maior_menor_50(list(range(100))) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Argumento que não é lista/tupla
assert maior_menor_50(50) == Exception
assert maior_menor_50("50 valores") == Exception
assert maior_menor_50({"a": 1}) == Exception

# Lista com 50 elementos, mas contendo tipos inválidos
# Booleanos (em Python, type(True) == bool, barrando int)
lista_com_bool = [1] * 49 + [True]
assert maior_menor_50(lista_com_bool) == Exception

# Floats
lista_com_float = [1] * 49 + [10.5]
assert maior_menor_50(lista_com_float) == Exception

# Strings e None
lista_com_str = [1] * 49 + ["50"]
assert maior_menor_50(lista_com_str) == Exception

lista_com_none = [1] * 49 + [None]
assert maior_menor_50(lista_com_none) == Exception

print("Todos os testes passaram com sucesso!")