import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from collections import deque

def viz8(x, y, imagem):
    h, w = imagem.shape[:2]
    viz = {}
    
    if y > 0: viz["Norte"] = imagem[y-1, x]
    if y < h - 1: viz["Sul"] = imagem[y+1, x]
    if x < w - 1: viz["Leste"] = imagem[y, x+1]
    if x > 0: viz["Oeste"] = imagem[y, x-1]
    if y > 0 and x < w - 1: viz["Nordeste"] = imagem[y-1, x+1]
    if y < h - 1 and x < w - 1: viz["Sudeste"] = imagem[y+1, x+1]
    if y < h - 1 and x > 0: viz["Sudoeste"] = imagem[y+1, x-1]
    if y > 0 and x > 0: viz["Noroeste"] = imagem[y-1, x-1]
    
    return viz

def encontrar_caminho(mask_permitida, x1, y1, x2, y2):
    """
    Algoritmo de busca em largura (BFS) para encontrar o caminho mais curto
    entre dois pontos, movendo-se APENAS pelos pixels permitidos (True).
    """
    h, w = mask_permitida.shape
    
    # Se os pontos de partida ou destino não são vermelhos, já não tem caminho
    if not mask_permitida[y1, x1] or not mask_permitida[y2, x2]:
        return None

    # Fila para explorar os caminhos e matriz para marcar onde já passamos
    fila = deque([(x1, y1)])
    visitados = np.zeros_like(mask_permitida, dtype=bool)
    visitados[y1, x1] = True
    
    # Dicionário para reconstruir o caminho de volta depois de achar o Ponto B
    pai = {}

    # Movimentos possíveis (8 direções)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while fila:
        cx, cy = fila.popleft()

        # Se chegamos no Ponto B, reconstruímos a rota
        if cx == x2 and cy == y2:
            caminho = []
            atual = (cx, cy)
            while atual != (x1, y1):
                caminho.append(atual)
                atual = pai[atual]
            caminho.append((x1, y1))
            return caminho # Retorna a lista de coordenadas

        # Explora os vizinhos
        for dx, dy in direcoes:
            nx, ny = cx + dx, cy + dy
            
            # Verifica se está dentro da imagem, se é permitido (vermelho) e se não foi visitado
            if 0 <= nx < w and 0 <= ny < h:
                if mask_permitida[ny, nx] and not visitados[ny, nx]:
                    visitados[ny, nx] = True
                    pai[(nx, ny)] = (cx, cy)
                    fila.append((nx, ny))
                    
    # Se a fila esvaziar e não achar o Ponto B, o caminho está bloqueado
    return None

def main():
    imagem = mpimg.imread('calcio.jpg')
    
    if imagem.shape[-1] == 4:
        imagem = imagem[..., :3]

    output_image = imagem.copy()

    # Inputs
    print("--- Configuração da Máscara ---")
    x = int(input("Digite a coordenada x (semente): "))
    y = int(input("Digite a coordenada y (semente): "))
    tolerancia = float(input("Digite a tolerância de cor Euclidiana (ex: 50): "))

    print("\n--- Configuração do Caminho ---")
    xa = int(input("Digite a coordenada X do Ponto A: "))
    ya = int(input("Digite a coordenada Y do Ponto A: "))
    xb = int(input("Digite a coordenada X do Ponto B: "))
    yb = int(input("Digite a coordenada Y do Ponto B: "))

    # Limites da imagem
    h, w = imagem.shape[:2]
    if not (0 <= x < w and 0 <= y < h and 0 <= xa < w and 0 <= ya < h and 0 <= xb < w and 0 <= yb < h):
        print("Erro: Coordenadas fora dos limites da imagem.")
        return

    # Processar a máscara de cor vermelha
    vizinhanca = viz8(x, y, imagem)
    imagem_int32 = imagem.astype(np.int32)
    centro_cor = imagem_int32[y, x]

    mascara_total = np.zeros(imagem.shape[:2], dtype=bool)

    for _, cor_pixel in vizinhanca.items():
        cor_pixel_int = cor_pixel.astype(np.int32)
        distancia_vizinho = np.linalg.norm(cor_pixel_int - centro_cor)
        
        if distancia_vizinho <= tolerancia:
            distancias_imagem = np.linalg.norm(imagem_int32 - cor_pixel_int, axis=-1)
            mascara_total |= (distancias_imagem <= tolerancia)

    # Pintar a máscara de vermelho
    output_image[mascara_total] = [255, 0, 0]

    # Tentativa de encontrar o caminho contínuo (A -> B) apenas pelo vermelho
    caminho = encontrar_caminho(mascara_total, xa, ya, xb, yb)

    if caminho is None:
        print("nao tem caminho")
    else:
        # Se achou, desenha o caminho percorrido em verde
        espessura = 1
        for px, py in caminho:
            y_min = max(0, py - espessura)
            y_max = min(h, py + espessura + 1)
            x_min = max(0, px - espessura)
            x_max = min(w, px + espessura + 1)
            output_image[y_min:y_max, x_min:x_max] = [0, 255, 0]
            
        plt.title(f"Caminho Encontrado: A({xa},{ya}) -> B({xb},{yb})")

    # Mostrar o resultado
    plt.imshow(output_image)
    if caminho is None:
        plt.title("Nao tem caminho")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()