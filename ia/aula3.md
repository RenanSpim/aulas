# Aula 3

## Dados e etapas de exploração
- Existe uma estimativa de que, a cada 20 meses, dobra a quantidade de dados armazenados no mundo
- +180 zetabytes de dados gerados por ano no mundo (1.000.000.000.000.000.000.000 bytes)
- 80% dados não estruturados, 20% dados estruturados

## Dados estruturados
- Tabela de atributos
- Objetos do mundo físico são abstraídos passando a ser representados como um conjunto de atributos

## Caracterização de atributos
- Atributo
  - Quantitativa
    - Discreta (contagem)
    - Contínua (temperatura)
  - Qualitativa
    - Nominal (sexo)
    - Ordinal (estatura: baixo médio, alto)

## Escala dos dados
- Define as operações permitidas sobre os valores dos atributos

### Dados qualitativos
- Escala nominal
  - Não conseguimos ordenar, (operadores: == e !=)
  - exemplo: id, cor, sexo
- Escala ordinal
  - Podemos ordenar (operadores: ==, !=, >, <. >=, <=)
  - exemplo: nível de febre, grau de escolaridade

### Dados quantitativos
- Escala intervalar
  - Números variam em um dado intervalo
  - possível ordenar (operadores: +, -, ==, !=, >, <. >=, <=)
- Escala racional
  - Números arbitrários sem escopo de limitação (operadores: +, -, /, *, ==, !=, >, <. >=, <=)

## AED
- Estatística descritiva
  - Medidas de localidade
  - Espalhamento e distribuição
- Visualização
  - Gráficos de barra, dispersão, boxplots
  - Técnicas de visualização específicas (ilustração com grafos, treemaps ...)

## Pré-processamento
- Técnicas usadas para melhorar a qualidade dos dados
  - Remoção de atributos, integração de dados, amostragem de dados, balanceamento de dados, limpezada de dados, redução de dimensionalidade, conversão de dados

### Removendo atributos
- Colunas que não tem relação com o que queremos calcular
- Merge de tabelas

### Amostragem de dados
- Trade-off (balanceamento) entre eficiência computacional e acurácia (taxa de predições corretas)
- Amostrar bem é a chave para modelar de forma eficiente um problema
- Amostragem precisa ser representativa
- Diferentes amostragens resultam em diferentes modelos
- Dados amostrados devem obedecer à mesma distribuição estatística que gerou o conjunto de dados originais
- Tipos de amostragem:
  - aleatória simples (sem reposição de exemplos, cada amostra selecionada apenas uma vez)
  - amostragem estratificada (classes de amostra, tentamos manter a mesma amostra pra todas elas)
  - amostragem progressiva (amostragem pequena, aumentamos até a acurácia continuar aumentando)

### Limpeza de dados
- Dados com ruído: possuem valores distintos do esperado (perturbação do equipamento...)
- Dados inconsistentes: não estão de acordo com as regras, expectativas ou padrões estabelecidos
- Dados incompletos: eliminar objetos com valores ausentes, preenche-los, tentar inferi-los, usar alguma heurísitica
- Dados redundantes: eliminar objetos altamente correlacionados
- One-hot encoding

