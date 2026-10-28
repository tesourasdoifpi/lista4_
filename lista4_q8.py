

def eh_positivo(n):
    if type(n) != int:
        return Exception

    elif n >= 0:
        return True
    elif n < 0:
        return False

assert eh_positivo(5) == True
assert eh_positivo(20) == True
assert eh_positivo(-5) == False
assert eh_positivo(0) == True
assert eh_positivo("5") == Exception

print("Todos os testes OK!")


