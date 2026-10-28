def analisar_pesquisa(dados_habitantes):
    # 1. Validação de tipo do parâmetro principal (espera-se uma lista ou tupla)
    if type(dados_habitantes) not in (list, tuple):
        return Exception

    # Lista vazia não gera estatísticas
    if len(dados_habitantes) == 0:
        return Exception

    soma_salarios = 0.0
    soma_filhos = 0
    maior_salario = -1.0
    qtd_ate_350 = 0
    total_pessoas = len(dados_habitantes)

    for item in dados_habitantes:
        # Cada registro deve ser uma tupla ou lista com exatamente 2 elementos: (salario, filhos)
        if type(item) not in (list, tuple) or len(item) != 2:
            return Exception

        salario, filhos = item

        # Validação estrita dos tipos (salário: int/float, filhos: int)
        if type(salario) not in (int, float) or type(filhos) != int:
            return Exception

        # Barrar NaN (x != x)
        if salario != salario:
            return Exception

        # Barrar valores infinitos, negativos ou filhos negativos
        if salario < 0 or salario == float("inf") or filhos < 0:
            return Exception

        # Acumuladores e cálculos
        soma_salarios += salario
        soma_filhos += filhos

        if salario > maior_salario:
            maior_salario = float(salario)

        if salario <= 350.0:
            qtd_ate_350 += 1

    media_salario = soma_salarios / total_pessoas
    media_filhos = soma_filhos / total_pessoas
    percentual_ate_350 = (qtd_ate_350 / total_pessoas) * 100.0

    return media_salario, media_filhos, maior_salario, percentual_ate_350


# ========================================================
# 1. CASOS VÁLIDOS (CAMINHO FELIZ)
# ========================================================

# Conjunto 1: 4 habitantes
# Médias: salários (1000 + 350 + 200 + 5000)/4 = 6550/4 = 1637.5
# Filhos: (2 + 3 + 1 + 0)/4 = 6/4 = 1.5
# Maior salário: 5000.0
# Até R$ 350,00: 350 e 200 -> 2 de 4 = 50.0%
dados_teste_1 = [
    (1000, 2),
    (350, 3),
    (200, 1),
    (5000, 0)
]
assert analisar_pesquisa(dados_teste_1) == (1637.5, 1.5, 5000.0, 50.0)

# Conjunto 2: Apenas 1 habitante com salário até 350
dados_teste_2 = [
    (350.0, 0)
]
assert analisar_pesquisa(dados_teste_2) == (350.0, 0.0, 350.0, 100.0)

# Conjunto 3: Ninguém com salário até 350
dados_teste_3 = [
    (1200.0, 1),
    (800.0, 2)
]
assert analisar_pesquisa(dados_teste_3) == (1000.0, 1.5, 1200.0, 0.0)


# ========================================================
# 2. ENTRADAS COM VALORES INVÁLIDOS (Exception)
# ========================================================

# Salário negativo
assert analisar_pesquisa([(-100, 2), (500, 1)]) == Exception

# Quantidade de filhos negativa
assert analisar_pesquisa([(1000, -1), (500, 1)]) == Exception

# Salário infinito ou NaN
assert analisar_pesquisa([(float("inf"), 2)]) == Exception
assert analisar_pesquisa([(float("nan"), 2)]) == Exception

# Lista vazia
assert analisar_pesquisa([]) == Exception


# ========================================================
# 3. ENTRADAS COM TIPOS INVÁLIDOS (Exception)
# ========================================================

# Tipo do argumento não iterável ou inválido
assert analisar_pesquisa(123) == Exception
assert analisar_pesquisa("dados") == Exception
assert analisar_pesquisa(None) == Exception

# Registro com formato incorreto (faltando ou sobrando elementos)
assert analisar_pesquisa([(1000,)]) == Exception
assert analisar_pesquisa([(1000, 2, 3)]) == Exception
assert analisar_pesquisa([1000]) == Exception

# Filhos com float (número de filhos deve ser inteiro)
assert analisar_pesquisa([(1000, 2.5)]) == Exception

# Booleanos no lugar de salário ou filhos
assert analisar_pesquisa([(True, 2)]) == Exception
assert analisar_pesquisa([(1000, False)]) == Exception

# String no lugar de salário ou filhos
assert analisar_pesquisa([("1000", 2)]) == Exception
assert analisar_pesquisa([(1000, "2")]) == Exception

print("Todos os testes passaram com sucesso!")