def tipo_triangulo(x, y, z):
    
    for lado in (x, y, z):
        if type(lado) not in (int, float):
            return Exception

    
    if x != x or y != y or z != z:
        return Exception

    
    if x <= 0 or y <= 0 or z <= 0:
        return Exception
    if x == float("inf") or y == float("inf") or z == float("inf"):
        return Exception

    
    
    if not (x < y + z and y < x + z and z < x + y):
        return "Não é um triângulo"

    
    if x == y == z:
        return "Equilátero"
    elif x == y or x == z or y == z:
        return "Isósceles"
    else:
        return "Escaleno"







assert tipo_triangulo(5, 5, 5) == "Equilátero"
assert tipo_triangulo(2.5, 2.5, 2.5) == "Equilátero"


assert tipo_triangulo(5, 5, 3) == "Isósceles"
assert tipo_triangulo(5, 3, 5) == "Isósceles"
assert tipo_triangulo(3, 5, 5) == "Isósceles"
assert tipo_triangulo(4.5, 4.5, 6.0) == "Isósceles"


assert tipo_triangulo(3, 4, 5) == "Escaleno"
assert tipo_triangulo(7, 8, 9) == "Escaleno"
assert tipo_triangulo(5.5, 6.5, 7.5) == "Escaleno"







assert tipo_triangulo(1, 2, 10) == "Não é um triângulo"
assert tipo_triangulo(10, 2, 1) == "Não é um triângulo"
assert tipo_triangulo(2, 10, 1) == "Não é um triângulo"


assert tipo_triangulo(1, 2, 3) == "Não é um triângulo"
assert tipo_triangulo(5, 2, 3) == "Não é um triângulo"







assert tipo_triangulo(0, 5, 5) == Exception
assert tipo_triangulo(5, 0, 5) == Exception
assert tipo_triangulo(5, 5, 0) == Exception
assert tipo_triangulo(-3, 4, 5) == Exception
assert tipo_triangulo(3, -4, 5) == Exception
assert tipo_triangulo(3, 4, -5) == Exception


assert tipo_triangulo(float("inf"), 5, 5) == Exception
assert tipo_triangulo(5, float("-inf"), 5) == Exception
assert tipo_triangulo(float("nan"), 5, 5) == Exception







assert tipo_triangulo(True, 5, 5) == Exception
assert tipo_triangulo(5, False, 5) == Exception


assert tipo_triangulo("3", 4, 5) == Exception
assert tipo_triangulo(3, "4", 5) == Exception
assert tipo_triangulo(3, 4, "5") == Exception

#
assert tipo_triangulo(None, 4, 5) == Exception
assert tipo_triangulo([3], 4, 5) == Exception
assert tipo_triangulo(3, (4,), 5) == Exception
assert tipo_triangulo(3, 4, {"z": 5}) == Exception

print("Todos os testes passaram com sucesso!")