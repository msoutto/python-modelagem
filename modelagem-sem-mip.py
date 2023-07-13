dia_minimo_inicio = [2, 5, 4, 0, 0, 8, 9]
duracao = [5, 6, 5, 4, 3, 4, 3]
dia_entrega = [25, 21, 15, 10, 8, 15, 22]
multa_por_dia = [3, 4, 2, 1, 1, 4, 2]
tipo = ['a', 'b', 'a', 'a', 'b', 'b', 'a']

n = len(dia_minimo_inicio)
pedidos = list(zip(dia_minimo_inicio, duracao, dia_entrega, multa_por_dia, tipo))


def calcular_valor_multas(ordem):
    data_inicio = [0] * n
    data_ajuste = [0] * n
    valor_multas = [0] * n

    for i in range(n):
        pedido_atual = ordem[i]
        if i > 0:
            pedido_anterior = ordem[i - 1]
            data_inicio[pedido_atual] = max(data_inicio[pedido_atual], data_inicio[pedido_anterior] + duracao[pedido_anterior])
            data_ajuste[pedido_atual] = max(data_ajuste[pedido_atual], data_inicio[pedido_atual] - 1)
        else:
            data_inicio[pedido_atual] = dia_minimo_inicio[pedido_atual]
            data_ajuste[pedido_atual] = dia_minimo_inicio[pedido_atual]

        if data_inicio[pedido_atual] + duracao[pedido_atual] > dia_entrega[pedido_atual]:
            dias_de_multa = data_inicio[pedido_atual] + duracao[pedido_atual] - dia_entrega[pedido_atual]
            multa = 0
            for dia in range(1, dias_de_multa + 1):
                if dia <= 5:
                    multa += multa_por_dia[pedido_atual]
                else:
                    multa += multa_por_dia[pedido_atual] * 2
            valor_multas[pedido_atual] = multa

    return sum(valor_multas)


from itertools import permutations

melhor_ordem = None
menor_valor_multas = float('inf')

for ordem in permutations(range(n)):
    valor_multas = calcular_valor_multas(ordem)
    if valor_multas < menor_valor_multas:
        menor_valor_multas = valor_multas
        melhor_ordem = ordem


data_inicio = [0] * n
data_ajuste = [0] * n
valor_multas = [0] * n

for i, pedido in enumerate(melhor_ordem):
    if i > 0:
        pedido_anterior = melhor_ordem[i - 1]
        data_inicio[pedido] = max(data_inicio[pedido], data_inicio[pedido_anterior] + duracao[pedido_anterior] + 2)
        data_ajuste[pedido] = max(data_ajuste[pedido], data_inicio[pedido] - 1)
    else:
        data_inicio[pedido] = dia_minimo_inicio[pedido]
        data_ajuste[pedido] = dia_minimo_inicio[pedido]

    if data_inicio[pedido] + duracao[pedido] > dia_entrega[pedido]:
        dias_de_multa = data_inicio[pedido] + duracao[pedido] - dia_entrega[pedido]
        multa = 0
        for dia in range(1, dias_de_multa + 1):
            if dia <= 5:
                multa += multa_por_dia[pedido]
            else:
                multa += multa_por_dia[pedido] * 2
        valor_multas[pedido] = multa

for i, pedido in enumerate(melhor_ordem):
    pedido_original = pedido  # Armazena o índice original do pedido
    pedido = melhor_ordem.index(pedido_original)  # Obtém o índice na ordem otimizada
    print(f'Pedido: {i + 1}')  # Adiciona 1 para exibir o número do pedido corretamente

    print(f'Data do inicio: {data_inicio[pedido]}')
    print(f'Data do ajuste: {data_ajuste[pedido]}')
    if valor_multas[pedido] == 0:
        print('Multa: Não houve multa.')
    else:
        print(f'Multa: {valor_multas[pedido]:.2f}')
    print()

print(f'Total de multas: {menor_valor_multas:.2f}')