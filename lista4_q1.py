def volume(raio):

    if type(raio) == str or raio <= 0:
        return Exception
    return round(4/3 * 3.14 * raio**3,2)

assert volume(0) == Exception  # testando valor improvável
assert volume(-1) == Exception  # testando valor improvável
assert volume('abc') == Exception  # testando valor inválido
assert volume('') == Exception  # testando valor inválido
assert volume(1.0) == 4.19, "Deveria retornar 4.19"    # testando classe válida
assert volume(1) == 4.19    # testando classe válida

print("Todos os testes ok!")