def ordenar_valores(a, b):
    if type(a) != int or type(b) != int:
        return Exception

    if a > b:
        return b, a
    return a, b



assert ordenar_valores(2, 5) == (2, 5)
assert ordenar_valores(10, 3) == (3, 10)
assert ordenar_valores(7, 7) == (7, 7)
assert ordenar_valores(0, -5) == (-5, 0)
assert ordenar_valores(-8, -2) == (-8, -2)
assert ordenar_valores(-1, -9) == (-9, -1)
assert ordenar_valores(0, 0) == (0, 0)
assert ordenar_valores(1000000, -1000000) == (-1000000, 1000000)



assert ordenar_valores(True, 5) == Exception
assert ordenar_valores(5, False) == Exception
assert ordenar_valores(2.5, 4) == Exception
assert ordenar_valores(2, 4.0) == Exception
assert ordenar_valores("1", 2) == Exception
assert ordenar_valores(1, "2") == Exception
assert ordenar_valores(None, 10) == Exception

assert ordenar_valores(1, (2,)) == Exception


print("Todos os testes passaram com sucesso!")