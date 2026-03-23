# Aula 4

## Relacionamento entre elementos de uma imagem
- Vizinhança-4
  - (x+1, y), (x-1, y), (x, y+1), (x, y-1)
- Vizinhança-8
  - (x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)

## Conectividade
- Elementos conexos
  - Vizinhos
    - Atendem algum critério de similaridade (mesma cor, profundidade ...)
  - Caminho
    - Sequência de pixels entre (x0, y0) até (xn, yn)

## Operações lógicas e aritméticas
- Adição: f1(x, y) + f2(x, y)
- Subtração: f1(x, y) - f2(x, y)
- Multiplicação: f1(x, y) * f2(x, y)
- Divisão: f1(x, y) / f2(x, y)
- Valores precisam ser inteiros entre 0 e 255