


def eh_par(n):
    if type(n) != int:
        return Exception

    elif n < 0:
        return Exception

    elif n % 2 == 0:
        return True
    else:
        False    


assert eh_par(3) == False
assert eh_par(17) == False
assert eh_par(43) == False
assert eh_par(88) == True
assert eh_par(100) == True
assert eh_par("B") == Exception
assert eh_par("teste") == Exception
assert eh_par("7") == Exception
assert eh_par(0) == Exception
assert eh_par(-6) == Exception


print("Todos os testes ok!")        