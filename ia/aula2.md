# Aula 2

## Agentes inteligentes
- Agente: Entidade que percebe e atua em um ambiente
- Ambiente: Parte do sistema que o agente não controla
- O agente interage com o ambiente por meio de seus sensores e atuadores
- Tipos:
  - Humanos: sensores (olhos, ouvidos), atuadores (mãos, pés)

## Agentes racionais
- Quando é capaz de realizar "o que é correto", isto é, "age da forma correta" para atingir o objetivo
- No contexto de IA: fazer a coisa certa é ter sucesso em uma dada tarefa

## Como avaliar o sucesso de um agente?
- Difícil
- Exemplo:
  - Melhor caminho para o robô até a cantina
    - Caminho A: curto mas congestionado
    - Caminho B: médio, meio livre
    - Caminho C: longo, sempre livre
- **O agente tem sucesso se, com o tempo, ele aprende a escolher o caminho que minimiza o tempo médio de chegada à cantina**
- Um agente racional é aquile que realiza ações que maximizam sua função utilidade
- Função utilidade(U): descreve os objetivos do agente
- Objetivos do agente são definidos pelo programador (minimizar o tempo, por exemplo)
- Exemplos:
  1. Sistema de recomendação:
     - U = Relevância * Probabilidade
     - Objetivo: Maximizar a satisfação do usuário sugerindo as produções mais relevantees, considerando seu histórico
  2. Chatbots:
     - U = (Relevância da resposta) - (Tempo de processamento)
     - Objetivo: Fornecer respostas precisas e rápidas
  3. Modelos de apredizado de máquina:
     - U = -(Erro do modelo após uma ação)
     - Objetivo: Minimizar o erro de predição do modelo

## Pac-man como um agente racional
- Diante de um objetivo a ser alcançado (problema a ser resolvido), um agente deve buscar um plano para atingir seu objetivo
- Plano: Sequência de ações que o agente deve executar para alcançar seu objetivo
- Problema de busca: Problema em que um agente precisa encontrar um plano que leva de um estado inicial para um estado objetivo
- Objetivo: Capturar todas as recompensas em tempo mínimo

## Conceito de espaço de estados
- Conjunto de todos possíveis estados que podem ocorrer na resolução do problema
- Cada estado é uma representação criada a partir do "mundo" que estamos resolvendo o problema
- Estados mudam conforme aplicamos ações neles
- Espaço de estados = Conjunto de todos os estados possíveis do jogo
- Ações = permite o agente chegar a um estado diferente (transição de um estado pra outro)

## Exemplos
1. Deslocamentos entre cidades
   - Objetivo: Ir de Arad para Bucareste
   - Formulação do problema:
     - Espaço de estados: cidades
     - Estado inicial: Em Arad
     - Ações: Permite deslocamentos entre cidades vizinhas
     - Custo: Distância percorrida entre as cidades
   - Solução: Sequência de cidades
     - Ex: Arad -> Sibiu -> Fagaras -> Bucareste
2. Problema dos jarros
   - Dados: 2 jarros, 3L e 4L, 1 fonte de água, como preencher 2L de água no jarro de 4L
   - Preenchemos uma **Árvore de decisão** para resolver o problema

## Árvore de busca
- Estrutura de dados na qual
  - Cada nó contém um elemento do espaço de estados
  - Raiz é o estado inicial
  - Nós filhos correspondem aos sucessores, gerados por meio de ações de transição de estado
  - Cada aresta representa uma ação
- **Para a maioria dos problemas de busca não é viável construir a árvore inteira**
- Estado: Representa uma configuração específica do sistema agente-ambiente
- Nó de uma árvore de busca: Inclui estado, nó pai, ação e custo do caminho

## Estratégias de busca
- Expande a árvore à procura de um plano
- Mantêm na fronteira, os planos parciais que estão sendo considerados
- Tenta expandir o mínimo possível

## Algoritmos de busca em espaços de estados
- Um algoritmo de busca é completo se ele encontra uma solução
- É dito ótimo se ele garante encontrar a melhor solução (menor custo)
- Exemplo labirinto:
  - Uma busca em largura vai encontrar a saída pois pode explorar todas as possibilidades sem perder nenhuma
  - E se cada passo custa 1, também é ótimo, pois encontra o caminho mais curto
1. Busca cega (não informada)
  - BFS, DFS e IDDFS (busca em profundidade + largura)
2. Busca informada (heurísticas)
  - Faz uso da melhor escolha levando em conta **custos** ou **conhecimento específico**
  - Ideia-chave: Uso de função avaliação f(*n*) que retorna o nó de menor custo, ou seja, f(*n*) estima o custo para chegar até o nó *n* e expande ele
  - Algoritmos: Busca gulosa, A*
  - Busca gulosa: Abre o nó com menor heurística, considera apenas o estado atual
  - A*: evita expandir caminhos caros, f(n) = g(n) + h(n)
    - f = custo total estimado, g = custo real, h = custo estimado (heurística)
    - Chega no menor caminho possível, recalcula os nós quando necessário
