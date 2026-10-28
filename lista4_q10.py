def conceito(nota):
    if type(nota) not in (int, float):
        return Exception

    if nota < 0.0 or nota > 10.0:
        return Exception

    if nota < 5.0:
        return "D"
    elif nota < 7.0:
        return "C"
    elif nota < 9.0:
        return "B"
    else:
        return "A"

# Conceito D: [0.0, 5.0)
assert conceito(0) == "D"
assert conceito(0.0) == "D"
assert conceito(2.5) == "D"
assert conceito(4.9) == "D"
assert conceito(4.99) == "D"

# Conceito C: [5.0, 7.0)
assert conceito(5) == "C"
assert conceito(5.0) == "C"
assert conceito(6.0) == "C"
assert conceito(6.9) == "C"
assert conceito(6.999) == "C"

# Conceito B: [7.0, 9.0)
assert conceito(7) == "B"
assert conceito(7.0) == "B"
assert conceito(8.0) == "B"
assert conceito(8.9) == "B"
assert conceito(8.95) == "B"

# Conceito A: [9.0, 10.0]
assert conceito(9) == "A"
assert conceito(9.0) == "A"
assert conceito(9.5) == "A"
assert conceito(10) == "A"
assert conceito(10.0) == "A"

assert conceito("B") == Exception
assert conceito(-5) == Exception

print("Todos os testes ok!")      
