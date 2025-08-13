import heapq
from masmorras_maps import masmorra1, masmorra2, masmorra3 
from mapa_principal import Hyrule

def heuristica(pos_atual, destino, menor_custo_terreno=10):
    x1, y1 = pos_atual
    x2, y2 = destino
    return (abs(x1 - x2) + abs(y1 - y2)) * menor_custo_terreno

def a_star(mapa, inicio, fim):
    linhas, colunas = len(mapa), len(mapa[0])
    menor_custo_terreno = min(min(linha) for linha in mapa if min(linha) != 9999)

    open_list = []
    heapq.heappush(open_list, (0, inicio))
    g = {inicio: 0}
    came_from = {}
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        _, atual = heapq.heappop(open_list)

        if atual == fim:
            caminho = []
            while atual in came_from:
                caminho.append(atual)
                atual = came_from[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho, g[fim]

        x, y = atual
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < linhas and 0 <= ny < colunas and mapa[nx][ny] != 9999:
                novo_custo = g[atual] + mapa[nx][ny]
                vizinho = (nx, ny)

                if vizinho not in g or novo_custo < g[vizinho]:
                    g[vizinho] = novo_custo
                    f = novo_custo + heuristica(vizinho, fim, menor_custo_terreno)
                    heapq.heappush(open_list, (f, vizinho))
                    came_from[vizinho] = atual

    return None, float('inf')

if __name__ == "__main__":

    """ 
    # Busca masmorra 1
    inicio_m1 = (14, 26)  # exemplo: posição do 'P'
    fim_m1 = (14, 4)   # exemplo: posição do 'E'
    caminho_m1, custo_m1 = a_star(masmorra1, inicio_m1, fim_m1)

    print("\nCaminho masmorra 1:", caminho_m1)
    print("Custo total masmorra 1:", custo_m1)

    # Busca masmorra 2
    inicio_m2 = (13, 25)  # 'P' da masmorra 2
    fim_m2 = (3, 14)     # 'E' da masmorra 2
    caminho_m2, custo_m2 = a_star(masmorra2, inicio_m2, fim_m2)

    print("\nCaminho masmorra 2:", caminho_m2)
    print("Custo total masmorra 2:", custo_m2)

    # Busca masmorra 3
    inicio_m3 = (14, 25)  # 'P' da masmorra 3
    fim_m3 = (16, 19)     # 'E' da masmorra 3
    caminho_m3, custo_m3 = a_star(masmorra3, inicio_m3, fim_m3)

    print("\nCaminho masmorra 3:", caminho_m3)
    print("Custo total masmorra 3:", custo_m3)
    """
    
    # Busca Hyrule
    inicio_H = (25, 28)  # 'P' da masmorra 3
    fim_H = (7, 6)     # 'E' da masmorra 3
    caminho_H, custo_H = a_star(Hyrule, inicio_H, fim_H)

    print("\nCaminho Hyrule:", caminho_H)
    print("Custo total Hyrule:", custo_H)