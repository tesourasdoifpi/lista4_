def tempo_em_dias(a,m,d):
    if type(a) != int or type(m) != int or type(d) != int:
        return Exception
    if (a not in range(0,121)) or (m not in range(0,13)) or (d not in range(0,31)):
        return Exception
    if a == 0 and  m == 0 and d == 0:
        return Exception
    return a*365 + m*30 + d

assert tempo_em_dias(1,1,31) == Exception  # testando classe inválida
assert tempo_em_dias(121,1,2) == Exception  # testando classe inválida (valores improváveis)
assert tempo_em_dias(10,13,2) == Exception  # testando classe válida (valores improváveis)
assert tempo_em_dias(-1,1,2) == Exception  # testando classe inválida (valores improváveis)
assert tempo_em_dias("*",1,2) == Exception  # testando classe inválida (valores inválidos)
assert tempo_em_dias(10.5,1,2) == Exception  # testando classe inválida (valores inválidos)
assert tempo_em_dias(10,1,2) == 3682  # testando classe válida
assert tempo_em_dias(0,1,2) == 32  # testando classe válida
assert tempo_em_dias(0,1,1) == 31  # testando classe válida
assert tempo_em_dias(0,0,0) == Exception  # testando classe válida valores limitrofes
assert tempo_em_dias(120,12,30) == 44190  # testando classe válida valores limitrofes
print("Todos os testes ok!")