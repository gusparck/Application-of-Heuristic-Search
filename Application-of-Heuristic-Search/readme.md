# 📘 Documentação do Projeto: Rota Ótima em Hyrule

---

## 1. Visão Geral e Objetivo

Este projeto simula a jornada de um herói em um mapa inspirado no jogo **The Legend of Zelda**.  
O objetivo principal não é apenas encontrar um caminho entre pontos, mas determinar a **rota global de menor custo** para uma missão complexa.

A missão consiste em:

- 🏠 Sair da **casa do herói (Link)**.
- ⚔️ Visitar **três masmorras** em qualquer ordem para coletar três pingentes.
- 🌲 Após coletar todos os pingentes, ir para o local final: **Lost Woods**.

O desafio é descobrir a **sequência ótima de visitação** das masmorras que minimiza o custo total da viagem, considerando os diferentes tipos de terreno no mapa principal e os caminhos dentro das masmorras.

---

## 2. Conceitos e Algoritmos Aplicados

O projeto se baseia em dois conceitos fundamentais da Inteligência Artificial e da Ciência da Computação.

### 2.1. Algoritmo de Busca **A\***

O **A\*** é o coração do sistema de navegação. Ele encontra o caminho de menor custo entre dois pontos específicos no mapa.  
Sua eficiência vem da fórmula:

```math
f(n) = g(n) + h(n)
```

Onde:

- `n` → próximo nó (célula do mapa) a ser considerado.
- `g(n)` → custo real do caminho desde o ponto inicial até o nó `n`.
- `h(n)` → heurística (estimativa do custo até o destino).

🔹 Neste projeto, utilizamos a **Distância de Manhattan** como heurística:

```math
h(n) = |x1 - x2| + |y1 - y2|
```

✅ O A\* garante encontrar o caminho mais curto se a heurística for **admissível**, o que é o caso da Distância de Manhattan.

---

### 2.2. Problema do **Caixeiro Viajante (TSP)**

Para determinar a ordem ideal das visitas às masmorras, usamos o **Problema do Caixeiro Viajante**.

Como temos apenas **3 masmorras**, uma solução de **força bruta** é viável:

- Gerar todas as permutações possíveis:
  - `3! = 6` rotas possíveis.
- Para cada rota, calcular o **custo total da jornada**:

```text
Casa → Masmorra A → Masmorra B → Masmorra C → Lost Woods
```

- Selecionar a rota de **menor custo**.

---

## 3. Estrutura dos Arquivos

O projeto é composto por três arquivos principais em Python:

- **`main.py`** → Arquivo principal com o algoritmo A\*, a lógica da jornada e visualização.
- **`mapa_principal.py`** → Define o mapa de Hyrule em **string** e em **matriz numérica de custos**.
- **`masmorras_maps.py`** → Define os mapas das três masmorras, no mesmo formato do mapa principal.

---

## 4. Arquitetura e Detalhamento do Código (`main.py`)

### 4.1. Configuração e Constantes

- **CORES** → Dicionário que mapeia símbolos do mapa para cores (`colorama`), tornando a visualização no terminal mais intuitiva.

---

### 4.2. Funções do Algoritmo A\*

#### `heuristica(pos_atual, destino)`

- Calcula a **Distância de Manhattan** entre dois pontos.
- Usada pelo **A\*** para estimar a distância até o alvo.

#### `a_star(mapa, inicio, fim)`

- Implementa o algoritmo **A\***.
- Entrada: matriz de custos (`mapa`), coordenadas de `inicio` e `fim`.
- Saída:
  - Lista de tuplas `(y, x)` representando o **caminho ótimo**.
  - Dicionário `g` com os **custos acumulados** de cada posição.

---

### 4.3. Funções de Visualização e Execução

#### `mostrar_caminho(mapa_str, caminho, is_dungeon, custos_g)`

- Exibe a **animação no terminal**.
- Mostra o custo em tempo real e atualiza o mapa a cada passo:
  - `*` → caminho já percorrido.
  - `L` → posição atual do herói.

#### `executar_rota(...)`

- Executa uma etapa da jornada.
- Chama `a_star` para obter o caminho e `mostrar_caminho` para exibição.

#### `fazer_masmorra(...)`

- Gerencia toda a lógica de visita a uma masmorra:
  - **Entrada → Pingente → Retorno à entrada**.
  - Atualiza a posição do herói em Hyrule.

---

### 4.4. Lógica Principal (`if __name__ == "__main__":`)

**Fase 1: Cálculo e Planejamento (sem animação)**

- Carrega informações das masmorras em `masmorras_info`.
- Pré-calcula o custo de ida e volta dentro de cada masmorra.
- Gera todas as **6 permutações** de visitação e calcula o custo total.
- Escolhe a rota com **menor custo**.

**Fase 2: Execução e Visualização**

- Exibe qual foi a **melhor ordem encontrada** e o custo total.
- Mostra a **animação da jornada** com contador em tempo real.
- Exibe o **custo final** ao término.

---

## 5. Como Executar o Projeto

### Pré-requisitos

- Ter **Python** instalado.
- Instalar a biblioteca **colorama**:

```bash
pip install colorama
```

---

### Estrutura de Arquivos

Certifique-se de que os três arquivos estão no mesmo diretório:

```text
📂 projeto_rota_otima
 ┣ 📜 main.py
 ┣ 📜 mapa_principal.py
 ┣ 📜 masmorras_maps.py
```

---

### Execução

No terminal, execute:

```bash
python main.py
```

---

✅ O programa primeiro calcula a rota ótima e, em seguida, exibe a **animação da jornada mais eficiente**.  
🎮 Acompanhe o herói passo a passo até o **Lost Woods**!
