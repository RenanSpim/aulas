# Aula 5
- Trabalho: COMPRESSÃO — falar sobre algoritmos de compressão (JPEG principalmente — transformada discreta do cosseno)

## Operações lógicas e aritméticas
- Ajustar brilho após o processo de aquisição
- Filtragem de imagens (especialmente no domínio da frequência e na modelagem de ruído)
- NÃO GOSTAMOS DE ESCUROS!!!! (comentário sobre filamentos de tungsténio)
- Para duas imagens/funções $f_1(x,y)$ e $f_2(x,y)$, operações elementares por pixel:
  - AND
  - OR
  - XOR
  - NOT

## Transformações geométricas
- $(x, y) = T\{(v, w)\}$
- $(v, w)$ são coordenadas de um pixel na imagem original
- $(x, y)$ são as coordenadas do pixel correspondente na imagem transformada

## Métricas de qualidade de imagens
- Notação: imagem original $f(x,y)$ e imagem processada $g(x,y)$, tamanho $M\times N$.

- Erro máximo (ME):
$$
\mathrm{ME} = \left| f(x,y) - g(x,y) \right|
$$

- Erro médio absoluto (MAE):
$$
\mathrm{MAE} = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} \left| f(x,y) - g(x,y) \right|
$$

- Erro médio quadrático (MSE):
$$
\mathrm{MSE} = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} \left( f(x,y) - g(x,y) \right)^2
$$

- Raiz do erro médio quadrático (RMSE):
$$
\mathrm{RMSE} = \sqrt{\mathrm{MSE}} = \sqrt{ \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} \left( f(x,y) - g(x,y) \right)^2 }
$$

- Coeficiente de Jaccard (para imagens binárias ou conjuntos de pixels):
$$
J(A,B) = \frac{|A \cap B|}{|A \cup B|}
$$
Em notação pixel-wise (com operações lógicas em binário):
$$
J = \frac{\sum_{x,y} (f(x,y) \land g(x,y))}{\sum_{x,y} (f(x,y) \lor g(x,y))}
$$

- Observações:
  - Quanto menores ME, MAE, MSE e RMSE, melhor a aproximação de $g$ em relação a $f$.
  - ME é sensível a outliers; MAE é menos sensível; MSE e RMSE penalizam erros grandes.
  - O coeficiente de Jaccard é útil para avaliar similaridade em segmentação binária.

## Modelos de ruídos em imagens
- Características
  - Funções de densidade de probabilidade
  - Tipos de ruído: uniforme, impulsivo, gaussiano
- Principais fontes de ruído em imagens digitais
  - Durante a aquisição
  - Transmissão
  - Sensores afetados por condições ambientais e qualidade dos sensores
- Considerando a observação 1 e H como operador identidade
  - Ruído em imagens pode ser observado a partir de uma função de densidade de probabilidade
  - uniforme, impulsivo, gaussiano
- Representação
  - Uma variável aleatória Z (nível de cinza)
  - Uma função de densidade de probabilidade p(z)
