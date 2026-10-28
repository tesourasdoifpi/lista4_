def idade_nadador(idade):
        
    if isinstance(idade, bool) or not isinstance(idade, int):
        return Exception

    elif isinstance(idade, str):
        return Exception
    
    elif idade >= 120 or idade <= 0:
        return Exception
    
    elif idade >= 5 and idade <= 7:
        return "Infantil A"

    elif idade >= 8 and idade <= 10:
        return "Infantil B"

    elif idade >= 11 and idade <= 13:
        return "Juvenil A"

    elif idade >= 14 and idade <= 17:
        return "Juvenil B"

    elif idade >= 18:
        return "Adulto"

    


assert idade_nadador(5) == "Infantil A"
assert idade_nadador(6) == "Infantil A"
assert idade_nadador(7) == "Infantil A"
assert idade_nadador(8) == "Infantil B"
assert idade_nadador(10) == "Infantil B"
assert idade_nadador(11) == "Juvenil A"
assert idade_nadador(13) == "Juvenil A"
assert idade_nadador(14) == "Juvenil B"
assert idade_nadador(17) == "Juvenil B"
assert idade_nadador(18) == "Adulto"
assert idade_nadador(21) == "Adulto"
assert idade_nadador(120) == Exception
assert idade_nadador(0) == Exception
assert idade_nadador(-5) == Exception
assert idade_nadador(2.5) == Exception
assert idade_nadador("120") == Exception


print("Todos os testes passaram com sucesso!")