def eh_primo(n):
    if not isinstance(n, int):
        return Exception

    if n <= 0:
        return Exception

    for i in range(2,n):
        if (n % i == 0):
            return False
    return True    


assert eh_primo(3) == True
assert eh_primo(17) == True
assert eh_primo(43) == True
assert eh_primo(88) == False
assert eh_primo(100) == False
assert eh_primo("B") == Exception
assert eh_primo("teste") == Exception
assert eh_primo("7") == Exception
assert eh_primo(0) == Exception
assert eh_primo(-6) == Exception


print("Todos os testes ok!")