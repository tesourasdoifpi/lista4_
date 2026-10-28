def eh_perfeito(n):
    # Se for booleano ou não for inteiro, levanta Exception
    if isinstance(n, bool) or not isinstance(n, int):
        raise Exception("O parâmetro deve ser um número inteiro.")

    # Números menores ou iguais a 1 não são perfeitos por definição
    if n <= 1:
        return False

    soma_divisores = 1
    limite = int(n ** 0.5)

    for i in range(2, limite + 1):
        if n % i == 0:
            soma_divisores += i
            complementar = n // i
            if complementar != i:
                soma_divisores += complementar

    return soma_divisores == n


assert eh_perfeito(6) == True       
assert eh_perfeito(28) == True      
assert eh_perfeito(496) == True     
assert eh_perfeito(8128) == True
assert eh_perfeito(0) == False
assert eh_perfeito(1) == False
assert eh_perfeito(-6) == False
assert eh_perfeito(-28) == False


entradas_invalidas = ["bh", 55.32, True, False, None, [6], {6: True}]

for entrada in entradas_invalidas:
    try:
        eh_perfeito(entrada)
        assert False, f"Deveria ter lançado Exception para: {entrada}"
    except Exception:
        assert True

print("Todos os testes passaram com sucesso!")