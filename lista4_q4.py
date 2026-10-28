def converter_segundos(total_segundos):
    if not isinstance(total_segundos, int):
        return Exception  

    if total_segundos < 0:
        return Exception  
    
    horas = total_segundos // 3600
    resto = total_segundos % 3600
    minutos = resto // 60
    segundos = resto % 60
    return horas, minutos, segundos


assert converter_segundos(45200) == (12, 33, 20)
assert converter_segundos(6425) == (1, 47, 5)
assert converter_segundos(32240) == (8, 57, 20)
assert converter_segundos(1200) == (0, 20, 0)
assert converter_segundos(86400) == (24, 0, 0)
assert converter_segundos(339) == (0, 5, 39)
assert converter_segundos("339") == Exception
assert converter_segundos(15.0) == Exception
assert converter_segundos(-50) == Exception


print("Todos os testes ok!")