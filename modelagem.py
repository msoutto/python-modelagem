from mip import Model, xsum, minimize, BINARY

def calcular_multa(atraso, peso):
    if atraso is not None and atraso <= 5:
        multa = atraso * peso
    else:
        multa = 0
    return multa

# def calcular_multa(atraso, wj):
#     if atraso <= 5:
#         return atraso * wj
#     else:
#         return 5 * wj + (atraso - 5) * 2 * wj


def resolver_problema(n: object, pedidos: object) -> object:
    # Criar modelo
    model = Model()

    # Variáveis de decisão
    dias = [[model.add_var(var_type=BINARY) for _ in range(n)] for _ in range(n)]
    atraso = [model.add_var() for _ in range(n)]

    # Função objetivo
    model.objective = minimize(xsum(calcular_multa(atraso[j], pedidos[j][3]) for j in range(n)))

    # Restrições
    for j in range(n):
        model += xsum(dias[j][k] for k in range(n)) == pedidos[j][2] - pedidos[j][1] + 1
        model += atraso[j] >= xsum((k + pedidos[j][1] - pedidos[j][0]) * dias[j][k] for k in range(n)) - pedidos[j][2]

    # Restrição de ajuste de máquinas
    for j in range(1, n):
        model += xsum(dias[j][k] for k in range(n)) >= xsum(dias[j - 1][k] for k in range(n)) + 1 - 1000 * (
                    1 - xsum(dias[j - 1][k] for k in range(n)))

    # Resolver o modelo
    model.optimize()

    # Obter resultados
    # Obter resultados
    resultado = []
    for j in range(n):
        inicio = -1
        ajuste = []
        for k in range(n):
            if dias[j][k].x is not None and dias[j][k].x >= 0.99:
                if inicio == -1:
                    inicio = k
                else:
                    ajuste.append(k)
        multa = calcular_multa(atraso[j].x, pedidos[j][3])
        resultado.append((pedidos[j][0], inicio, ajuste, multa))

    # resultado = []
    # for j in range(n):
    #     inicio = -1
    #     ajuste = []
    #     for k in range(n):
    #         if dias[j][k].x >= 0.99:
    #             if inicio == -1:
    #                 inicio = k
    #             else:
    #                 ajuste.append(k)
    #     multa = calcular_multa(atraso[j].x, pedidos[j][3])
    #     resultado.append((pedidos[j][0], inicio, ajuste, multa))

    # Calcular o total de multas
    total_multas = sum(multa for _, _, _, multa in resultado)

    return resultado, total_multas


# Exemplo de uso
pedidos = [
    # (rj, pj, dj, wj)
    (1, 10, 7, 1),  # Pedido 1
    (3, 12, 5, 2),  # Pedido 2
    (6, 15, 8, 3)   # Pedido 3
]

n = len(pedidos)
resultado, total_multas = resolver_problema(n, pedidos)

# Imprimir resultados
for i, (rj, inicio, ajuste, multa) in enumerate(resultado):
    print(f"Pedido {i + 1}:")
    print(f"   Data mínima de início: {rj}")
    print(f"   Dia de início da produção: {inicio}")
    print(f"   Dias gastos fazendo ajuste de máquinas: {ajuste}")
    print(f"   Multa paga: {multa}")
    print()

print(f"Total de multas pagas: {total_multas}")