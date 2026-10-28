def duracao_jogo(h_inicio, m_inicio, h_fim, m_fim):

    parametros = (h_inicio, m_inicio, h_fim, m_fim)
    if any(type(p) != int for p in parametros):
        return Exception

    
    if not (0 <= h_inicio <= 23 and 0 <= h_fim <= 23):
        return Exception
    if not (0 <= m_inicio <= 59 and 0 <= m_fim <= 59):
        return Exception

    
    total_min_inicio = h_inicio * 60 + m_inicio
    total_min_fim = h_fim * 60 + m_fim

    
    diferenca = total_min_fim - total_min_inicio

    
    if diferenca == 0:
        duracao_total = 24 * 60
    
    elif diferenca < 0:
        duracao_total = diferenca + (24 * 60)
    
    else:
        duracao_total = diferenca

    duracao_horas = duracao_total // 60
    duracao_minutos = duracao_total % 60

    return duracao_horas, duracao_minutos


assert duracao_jogo(14, 0, 16, 30) == (2, 30)
assert duracao_jogo(10, 15, 12, 10) == (1, 55)
assert duracao_jogo(8, 0, 8, 45) == (0, 45)


assert duracao_jogo(22, 0, 2, 0) == (4, 0)
assert duracao_jogo(23, 40, 0, 20) == (0, 40)
assert duracao_jogo(21, 50, 1, 15) == (3, 25)


assert duracao_jogo(15, 30, 15, 30) == (24, 0)
assert duracao_jogo(0, 0, 0, 0) == (24, 0)

assert duracao_jogo(-1, 0, 10, 0) == Exception
assert duracao_jogo(24, 0, 10, 0) == Exception
assert duracao_jogo(10, 0, -5, 0) == Exception
assert duracao_jogo(10, 0, 25, 0) == Exception


assert duracao_jogo(10, -1, 12, 0) == Exception
assert duracao_jogo(10, 60, 12, 0) == Exception
assert duracao_jogo(10, 0, 12, -10) == Exception
assert duracao_jogo(10, 0, 12, 90) == Exception

assert duracao_jogo(True, 0, 10, 0) == Exception
assert duracao_jogo(10, False, 12, 0) == Exception


assert duracao_jogo(10.5, 0, 12, 0) == Exception
assert duracao_jogo(10, 0.0, 12, 0) == Exception


assert duracao_jogo("10", 0, 12, 0) == Exception
assert duracao_jogo(10, 0, "12", 0) == Exception
assert duracao_jogo(None, 0, 12, 0) == Exception
assert duracao_jogo([10], 0, 12, 0) == Exception
assert duracao_jogo(10, 0, 12, (0,)) == Exception

print("Todos os testes passaram com sucesso!")