

def calcular_notas(n1, n2, n3, letra):
    if not isinstance(letra, str):
        return Exception

    operacao = letra.strip().upper()
    if operacao not in ("A", "P"):
        return Exception

    notas = (n1, n2, n3)
    for i, n in enumerate(notas, start=1):
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            return Exception
        if n < 0:
            return Exception
    
    if operacao == "A":
        return (n1 + n2 + n3) / 3
    else:  # operacao == "P"
        return ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10    
    

assert calcular_notas(10, 10, 10, "A") == 10.0
assert calcular_notas(0, 0, 0, "A") == 0.0
assert calcular_notas(6, 7, 8, "A") == 7.0
assert calcular_notas(6, 7, 8, "a") == 7.0
assert calcular_notas(6, 8, 10, "p") == 7.4
assert calcular_notas(6, 7, 8, "  A  ") == 7.0
assert calcular_notas(True, 8, 9, "A") == Exception 
assert calcular_notas(7, 8, 9, "tipo_invalido") == Exception
assert calcular_notas(7, "obj", 9, "A") == Exception


print("Todos os testes ok!")