from mip import Model, xsum, minimize, BINARY

def novo_pedido():
    pedido = dict()

    pedido["data_minima_inicio"] = -1
    while pedido["data_minima_inicio"] < 0:
        pedido["data_minima_inicio"] = input("Data mínima de início (maior que zero): ")

    pedido["duracao"] = 0
    while pedido["duracao"] < 1:
        pedido["duracao"] = input("Duração: ")
    
    pedido["data_desejada_entrega"] = 0
    while pedido["data_desejada_entrega"] < 1:
        pedido["data_desejada_entrega"] = input("Data desejada para a entrega: ")

    pedido["multa_por_dia"] = -1
    while pedido["multa_por_dia"] < 0:
        pedido["multa_por_dia"] = input("Multa por dia de atraso: ")
    
    pedido["tipo"] = "Z"
    while pedido["tipo"] != "A" and pedido["tipo"] != "B":
        pedido["tipo"] = input("Tipo de pedido (A,B): ")

    return pedido

pedidos = []

print("Deseja adicionar pedidos?")
adicionar_pedidos = input("1- SIM, 2- NÃO")

if adicionar_pedidos == 1:
    pedidos.append(novo_pedido())
else:
    print("Nenhum pedido")






# Exemplo de uso
pedidos = [
    # (rj, pj, dj, wj, tj)
    (1, 10, 7, 1, 'a'),  # Pedido 1
    (3, 12, 5, 2, 'b'),  # Pedido 2
    (6, 15, 8, 3, 'a')   # Pedido 3
]


def calcular_multa(atraso, peso):
    if atraso is not None and atraso <= 5:
        multa = atraso * peso
    else:
        multa = 0
    return multa

def calcular_data_entrega_inicial(data_inicio, duracao):
    return data_inicio + duracao

def calcular_data_entrega(j, pedidos):
    data_entrega = calcular_data_entrega_inicial(pedidos[j][0], pedidos[j][2])
    if j > 0 and pedidos[j][4] != pedidos[j-1][4]: data_entrega += 1

    return data_entrega

def calcular_dias_de_multa(j, pedidos):
    return 0

# FUNCOES
# data_entrega(j) = data_inicio(j) + duracao(j)
# if j > 0 && tipo(j) != tipo(j-1): data_entrega(j) += 1
# dias_de_multa(j) = data_entrega(j) - data_maxima_entrega(j)
# if dias_de_multa(j) > 5: multa_por_dia(j) *= 2
# multa(j) = dias_de_multa(j) * multa_por_dia(j)

# REGRAS
# data_inicio(j) >= data_minima_inicio(j)

# RESULTADOS
# data_inicio
# data_entrega
# teve_ajuste
# multa
