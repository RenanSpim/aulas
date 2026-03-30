# Aula 4

## O que é IA
- "Estudo e design de agentes inteligentes", esndo o agente um sistema que percebe seu ambiente e toma atitudes que maximizam suas chances de sucesso
- També pode ser definida com ramo da CC que se ocupa do comportamento inteligente ou, que humanos fazem melhor

## Aprendizado de máquina
- Modelos computacionais que melhoram seu desempenho por meio dos dados
- Aprendem uma tarefa a partir de dados
- Em geral: é necessário grandes volumes de dados para capacitar a máquina a generalizar melhor a tarefa
  - Como: predizer a temperatura (tempo/clima): diagnosticar uma doença, recomendação de conteúdo via agrupamento
- Artificial inteligence > Machine learning > Deep learning (> = engloba)

## Onde está no diagrama?
- mapeamento -> caputra, preparação e armazenamento -> análise exploratória e inferência estatística -> MODELAGEM PREDITIVA

## Sintetizando
- Modelos de ML: melhoram seu desempenho por meio da experiência (dados)
  - Melhora execução de uma tarefa (T)
  - Com relação a uma medida de desempenho (P)
  - Baseada na experiência (E)
- Exemplo:
  - Tarefa T: reconhecer e classificar caracteres manuscrito
  - Medida de desempenho P: porcentagem dos dígitos classificados corretamente
  - Experiência E: base de dados de caracteres manuscritos com suas respectivas classificações

## ML x Inferência indutiva

### Inferência:
- Criar um raciocínio, para ter uma conclusão geral sobre todos os membros de uma classe por meio da análise de apenas alguns membros da classe
- De maneira geral: raciocínio do particular visando-se expandir para o geral
- Exemplo:
    - Todos os pacientes com Déficit de Atenção atendidos em 1986 sofriam de Ansiedade
    - Todos os pacientes com Déficit de Atenção atendidos em 1987 sofriam de Ansiedade
  - Podemos inferir logicamente que: todos os pacientes que sofrem de Déficit de Atenção também sofrem de Ansiedade?
  - Isso pode ser ou não verdade, mas propicia uma boa generalização a partir do raciocínio indutivo

## Tipos de aprendizado de máquina
- Aprendizado Supervisionado (maior parte)
  - Algoritmo de aprendizado (indutor) recebe um conjunto de registros de treinamento para os quais os rótulos da classe-alvo são conhecidos
  - Cada registro é descrito por um vetor de atributos e pelo rótulo da classe (exemplo: pacientes com déficit de atenção e ansiedade)
  - Objetivo do indutor: construir um modelo, que faça a inferência da classe de novos registros não-rotulados
    - Para rótulos de classe discretos -> problema de classificação
    - Para valores contínuos -> problema de regressão
- Aprendizado Não-Supervisionado
  - Situação onde não temos mais os rótulos pré-definidos
  - O indutor então analisará os registros fornecidos, tentando determinar se alguns deles podem ser agrupados de alguma forma, gerando assim clusters
  - Após a determinação dos clusters, em geral, é necessário uma análise para determinar o que cada cluster significa no contexto do problema estudado
- Aprendizado Semi-Supervisionado
  - Mistura as ideias de Aprendizado Não-Supervisionado com Supervisionado
  - Este aprendizado assume que, juntamente com o conjunto de treinamento com rótulos, há um segundo conjunto, de registros não-rotulados, também disponível durante o treinamento
  - Uma das metas do Aprendizado Semi-Supersivionado é treinar classificadores quando uma grande quantidade de registros não-rotulados está disponível, combinada à um pequeno conjunto de registros rotulados
- Aprendizado Por Reforço
  - Estratégias de aprendizado por reforço tratam de situações onde um agente aprende por tentativa e erro ao atuar sobre um ambiente dinâmico
  - Não é necessária uma entidade externa que forneça instâncias de dados, ou um modelo a respeito da tarefa a ser realizada: a única fonte de aprendizado é a própria experiência do agente junto ao ambiente
  - O objetivo formal é: adquirir um plano de ações que maximize seu desempenho

## Treinamento, validação e teste
- Treinamento: processo de ajuste de um modelo para aprender a realziar uma tarefa específica
- Importância de cada subconjunto de dados
  - Treinamento: ensia o modelo a partir do exemplos conhecidos
  - Validação: Ajuda no ajuste do modelo, tentando encontrar o melhor conjunto de hiperparâmetros, além de tentar evitar o chamado fenômeno de sobreajuste
  - Teste: Avalia a capacidade do modelo (após treinado) de generalizar para dados novos e nunca vistos
- Exemplo: (método de divisão de dados)
  - Método hold-out: os dados rotulados são divididos em dois grupos
    - P%: usados na etapa de treinamento
    - (1-P)%: usados na etapa de teste

## Modelos preditivos
- Problema de classificação: o domínio é um conjunto de valores nominais ou valores discretos
- Problema de regressão: o domínio é um conjunto infinito e ordenado de valores

## KNN - K nearest neighbours
- Classifica um novo objeto com base nos registros do conjunto de treinamento que são próximos a ele
- Não aprende um modelo compacto para os dados, apenas memoriza os dados de treinamento
- Vantagem: pode ser usado tanto para classificação quanto para regressão
- Ponto a ser observado: Tem variações definidas com base no número de vizinhos a serem considerados
- Parâmetro K: define quantos vizinhos mais próximos pra calcular o valor na regressão
- Calcula distância entre cada dois pontos
- Métrica mais usada: distância euclidiana

## Intuição
- classificar um novo livro dentro de uma biblioteca, quero classificar ele ou de história ou ciência, quero ver quantos caras são mais próximos a ele, se são os livros de história ou de ciência

## Algoritmo KNN
```
Entrada: D (conjunto de objetos do treinamento),
z (objeto-teste), que é um vetor de atributos,
L (conjunto de classes usadas para rotular os objetos).

Saída: A classe de z.

PARA CADA objeto yi de D FAÇA:
    Computa a distância entre yi e z;
FIM
Selecione o subconjunto (de vizinhos) dos k objetos do treinamento mais próximos à z;
A classe de saída (do objeto z) será a moda dos rótulos.

## caso o problema seja regressão, utiliza-se a média ou mediana dos valores reais dos k vizinhos mais próximos.
```
- Podemos usar heuríticas pra escolher o valor de K (dependendo do valor de K as classes escolhidas podem ser diferentes)

## Regressão logística
- Objetivo: ajustar uma curva, em um formato de “S”, aos valores das probabilidades e características (eixo x) dos dados
- Para isso, vamos adotar a função logística (função sigmoide) em nossa análise: h(z) = e\*\*z/(1 + e\*\*z)
- Tem como usar uma função pra caso tenha mais de 2 parâmetros

## Naive Bayes
- Curvas normais, calcula-se qual é mais provável A ou B
- Apesar de sua limitação na consideração da independência entre atributos, o classificador Naive Bayes é robusto e oferece bom desempenho em uma variedade de conjuntos de dados do mundo real
- Ele pode calcular todas as probabilidades necessárias a partir dos dados de treinamento em uma única iteração, tornando a modelagem bastante eficiente
- É altamente adaptável para operações incrementais, mostrando resistência a interferências causadas por ruídos e atributos irrelevantes


