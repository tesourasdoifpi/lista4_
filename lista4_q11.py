def peso_ideal(altura, sexo):
    if type(altura) not in (int, float):
        return Exception
    
    if type(sexo) != str:
        return Exception

    if altura < 0.5 or altura > 2.8:
        return Exception

    sexo_normalizado = sexo.strip().upper()
    if sexo_normalizado not in ("M", "F"):
        return Exception

    if sexo_normalizado == "M":
        return round(72.7 * altura - 58, 4)
    else:  
        return round(62.1 * altura - 44.7, 4)



assert peso_ideal(1.75, "M") == 69.2250
assert peso_ideal(1.80, "m") == 72.8600
assert peso_ideal(2, "  M  ") == 87.4000  


assert peso_ideal(1.65, "F") == 57.7650
assert peso_ideal(1.60, "f") == 54.6600
assert peso_ideal(1.50, "  f  ") == 48.4500


assert peso_ideal(0.5, "M") == -21.6500
assert peso_ideal(2.8, "F") == 129.1800

assert peso_ideal(True, "M") == Exception
assert peso_ideal("1.75", "M") == Exception
assert peso_ideal(None, "M") == Exception
assert peso_ideal(10.0, "M") == Exception
assert peso_ideal(1.75, "Feminino") == Exception
assert peso_ideal(1.75, "") == Exception

print("Todos os testes passaram com sucesso!")