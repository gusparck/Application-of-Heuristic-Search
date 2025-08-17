import time
import os
import heapq
import colorama
import itertools
import sys

from masmorras_maps import masmorra1, masmorra2, masmorra3, masmorra1_str, masmorra2_str, masmorra3_str
from mapa_principal import Hyrule, main_map_str

colorama.init(autoreset=False)  # mantém as cores até o fim do programa

CORES = {
    # Cores de Hyrule
    "G": colorama.Fore.GREEN,
    "S": colorama.Fore.YELLOW,
    "F": colorama.Fore.GREEN + colorama.Style.DIM,
    "M": colorama.Fore.YELLOW + colorama.Style.DIM,
    "A": colorama.Fore.BLUE,

    # Cores das Masmorras
    "X": colorama.Fore.WHITE + colorama.Style.DIM,
    "caminho_masmorra": colorama.Fore.WHITE,

    # Símbolos Especiais e de Animação
    "trace": colorama.Fore.CYAN,
    "D": colorama.Fore.CYAN + colorama.Style.BRIGHT,
    "W": colorama.Fore.BLUE,
    "E": colorama.Fore.CYAN + colorama.Style.BRIGHT,
    "P": colorama.Fore.CYAN + colorama.Style.BRIGHT,
    "L": colorama.Fore.MAGENTA + colorama.Style.BRIGHT,

    # Cor Padrão
    "default": colorama.Fore.WHITE
}

def heuristica(pos_atual, destino, menor_custo_terreno=10):
    x1, y1 = pos_atual
    x2, y2 = destino
    return (abs(x1 - x2) + abs(y1 - y2)) * menor_custo_terreno

def a_star(mapa, inicio, fim):
    if not (inicio and fim):
        return None, {}

    colunas, linhas = len(mapa[0]), len(mapa)
    custos_validos = [c for linha in mapa for c in linha if c != 9999]
    menor_custo_terreno = min(custos_validos) if custos_validos else 10

    open_list = []
    heapq.heappush(open_list, (0, inicio))

    g = {inicio: 0}
    came_from = {}

    movimentos = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (dx, dy)

    while open_list:
        _, atual = heapq.heappop(open_list)

        if atual == fim:
            caminho = []
            while atual in came_from:
                caminho.append(atual)
                atual = came_from[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho, g

        x, y = atual
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy

            if 1 <= nx <= colunas and 1 <= ny <= linhas and mapa[ny-1][nx-1] != 9999:
                novo_custo = g[atual] + mapa[ny-1][nx-1]

                vizinho = (nx, ny)

                if vizinho not in g or novo_custo < g[vizinho]:
                    g[vizinho] = novo_custo
                    f = novo_custo + heuristica(vizinho, fim, menor_custo_terreno)
                    heapq.heappush(open_list, (f, vizinho))
                    came_from[vizinho] = atual

    return None, {}

def mostrar_caminho(mapa_str, caminho, is_dungeon, custos_g):
    # Mostra a animação do caminho sendo percorrido e o custo em tempo real.
    mapa_visual = [linha.split('\t') for linha in mapa_str.strip().split("\n")]
    
    # Pega o custo total do trecho para exibir como referência
    custo_total_trecho = custos_g.get(caminho[-1], 0)

    for i, passo_atual in enumerate(caminho):
        caminho_percorrido = set(caminho[0:i])
        frame_buffer = []
        for y, linha_visual in enumerate(mapa_visual):
            linha_renderizada = ""
            for x, char_original in enumerate(linha_visual):
                posicao = (x+1, y+1)  
                char_display = char_original

                if posicao == passo_atual:
                    cor = CORES.get("L")
                    char_display = "L"
                elif posicao in caminho_percorrido:
                    cor = CORES.get("trace")
                    char_display = "*"
                else:
                    if not char_original:
                        char_display = "."
                        cor = CORES["caminho_masmorra"]
                    else:
                        if is_dungeon and char_original not in ['X', 'E', 'P']:
                            cor = CORES["caminho_masmorra"]
                        else:
                            cor = CORES.get(char_original, CORES["default"])
                linha_renderizada += f"{cor}{char_display} "
            frame_buffer.append(linha_renderizada.rstrip())
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Constrói e exibe o mapa
        print("\n".join(frame_buffer))
        
        # Exibe o custo do passo atual abaixo do mapa
        custo_ate_agora = custos_g.get(passo_atual, 0)
        print(f"\n{colorama.Fore.CYAN}Custo do Percurso: {colorama.Fore.YELLOW}{custo_ate_agora} / {custo_total_trecho}{colorama.Style.RESET_ALL}")
        
        time.sleep(0.1)

def encontrar_posicao(mapa_str, simbolo):
    for y, linha in enumerate(mapa_str.strip().split("\n")):
        for x, cell in enumerate(linha.split("\t")):
            if cell == simbolo:
                return (x+1, y+1) 
    return None

def executar_rota(nome, mapa_numerico, mapa_str, inicio, fim, custo_total, is_dungeon_map=False):
    # Executa e anima uma única rota, atualizando o custo total.
    caminho, custos_g = a_star(mapa_numerico, inicio, fim)
    
    if caminho is None:
        print(f"\n[AVISO] Caminho não encontrado para: {nome}")
        return custo_total, inicio
    
    custo_trecho = custos_g.get(caminho[-1], 0)
    
    print(f"\nRota: {nome} | Custo do trecho: {custo_trecho}")
    
    # Passa o dicionário 'custos_g' para a função de animação
    mostrar_caminho(mapa_str, caminho, is_dungeon_map, custos_g)
    
    return custo_total + custo_trecho, caminho[-1]

def fazer_masmorra(nome, pos_hyrule_entrada, mapa_masmorra, str_masmorra, entrada, pingente, custo_total, pos_atual):
    # Função para executar a jornada completa de uma masmorra.
    custo_total, pos_atual = executar_rota(f"{nome} (Hyrule -> Entrada)", Hyrule, main_map_str, pos_atual, pos_hyrule_entrada, custo_total, is_dungeon_map=False)
    
    pos_no_mapa_da_masmorra = entrada
    custo_total, pos_no_mapa_da_masmorra = executar_rota(f"{nome} (Entrada -> Pingente)", mapa_masmorra, str_masmorra, pos_no_mapa_da_masmorra, pingente, custo_total, is_dungeon_map=True)
    
    custo_total, pos_no_mapa_da_masmorra = executar_rota(f"{nome} (Pingente -> Entrada)", mapa_masmorra, str_masmorra, pos_no_mapa_da_masmorra, entrada, custo_total, is_dungeon_map=True)
    
    pos_atual = pos_hyrule_entrada
    return custo_total, pos_atual


if __name__ == "__main__":
    casa_link = (25, 28)      
    lost_woods = (7, 6)

    masmorras_info = [
        {
            "nome": "Masmorra 1", "mapa_num": masmorra1, "mapa_str": masmorra1_str,
            "entrada_hyrule": (6, 33),   
            "entrada_masmorra": encontrar_posicao(masmorra1_str, "E"),
            "pingente": encontrar_posicao(masmorra1_str, "P"),
        },
        {
            "nome": "Masmorra 2", "mapa_num": masmorra2, "mapa_str": masmorra2_str,
            "entrada_hyrule": (40, 18),  
            "entrada_masmorra": encontrar_posicao(masmorra2_str, "E"),
            "pingente": encontrar_posicao(masmorra2_str, "P"),
        },
        {
            "nome": "Masmorra 3", "mapa_num": masmorra3, "mapa_str": masmorra3_str,
            "entrada_hyrule": (25, 2),   
            "entrada_masmorra": encontrar_posicao(masmorra3_str, "E"),
            "pingente": encontrar_posicao(masmorra3_str, "P"),
        }
    ]


    print("Calculando custos internos das masmorras...")
    for m in masmorras_info:
        caminho_ida, g_ida = a_star(m["mapa_num"], m["entrada_masmorra"], m["pingente"])
        caminho_volta, g_volta = a_star(m["mapa_num"], m["pingente"], m["entrada_masmorra"])
        
        if caminho_ida is None or caminho_volta is None:
            print(f"{colorama.Fore.RED}[ERRO FATAL] Não foi possível encontrar um caminho interno na {m['nome']}.")
            sys.exit(1)
            
        custo_numerico_ida = g_ida[m["pingente"]]
        custo_numerico_volta = g_volta[m["entrada_masmorra"]]
        m["custo_interno"] = custo_numerico_ida + custo_numerico_volta

    print("Calculando a rota ótima...")
    ordens_possiveis = list(itertools.permutations(masmorras_info))
    melhor_ordem = None
    menor_custo_total = float('inf')

    for ordem in ordens_possiveis:
        custo_da_ordem_atual = 0
        posicao_atual = casa_link
        rota_valida = True

        # Custo: Casa do Link -> 1ª Masmorra
        primeira_masmorra = ordem[0]
        caminho_trecho, g_trecho = a_star(Hyrule, posicao_atual, primeira_masmorra["entrada_hyrule"])
        
        if caminho_trecho is None:
            rota_valida = False
        else:
            custo_da_ordem_atual += g_trecho[primeira_masmorra["entrada_hyrule"]]
            custo_da_ordem_atual += primeira_masmorra["custo_interno"]

        # Custo: Entre as masmorras
        if rota_valida:
            for i in range(len(ordem) - 1):
                masmorra_origem = ordem[i]
                masmorra_destino = ordem[i+1]
                caminho_trecho, g_trecho = a_star(Hyrule, masmorra_origem["entrada_hyrule"], masmorra_destino["entrada_hyrule"])
                
                if caminho_trecho is None:
                    rota_valida = False; break
                
                custo_da_ordem_atual += g_trecho[masmorra_destino["entrada_hyrule"]]
                custo_da_ordem_atual += masmorra_destino["custo_interno"]
        
        # Custo: Última Masmorra -> Lost Woods
        if rota_valida:
            ultima_masmorra = ordem[-1]
            caminho_trecho, g_trecho = a_star(Hyrule, ultima_masmorra["entrada_hyrule"], lost_woods)
            
            if caminho_trecho is None:
                rota_valida = False
            else:
                custo_da_ordem_atual += g_trecho[lost_woods]

        if rota_valida and custo_da_ordem_atual < menor_custo_total:
            menor_custo_total = custo_da_ordem_atual
            melhor_ordem = ordem

    if melhor_ordem is None:
        print(f"\n{colorama.Fore.RED}{colorama.Style.BRIGHT}ERRO: Nenhuma rota válida foi encontrada.{colorama.Style.RESET_ALL}")
        sys.exit(1)

    print("\n" + "="*50)
    print(f"{colorama.Fore.CYAN}A MELHOR ORDEM ENCONTRADA É:")
    ordem_nomes = " -> ".join([m['nome'] for m in melhor_ordem])
    print(f"{colorama.Fore.CYAN}{ordem_nomes}")
    print(f"{colorama.Fore.YELLOW}CUSTO TOTAL ESTIMADO: {menor_custo_total}")
    print("="*50 + "\n")
    time.sleep(5) 

    custo_total_final = 0
    pos_atual = casa_link

    for masmorra in melhor_ordem:
        custo_total_final, pos_atual = fazer_masmorra(
            masmorra["nome"], masmorra["entrada_hyrule"], masmorra["mapa_num"],
            masmorra["mapa_str"], masmorra["entrada_masmorra"], masmorra["pingente"],
            custo_total_final, pos_atual
        )

    custo_total_final, pos_atual = executar_rota(
        "Hyrule -> Lost Woods", Hyrule, main_map_str, pos_atual, lost_woods, 
        custo_total_final, is_dungeon_map=False
    )

    print(f"\n{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}CUSTO TOTAL DA JORNADA: {custo_total_final}")