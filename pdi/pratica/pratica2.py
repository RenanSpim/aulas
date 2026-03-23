import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

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

def main():
    imagem = mpimg.imread('calcio.jpg')
    
    if imagem.shape[-1] == 4:
        imagem = imagem[..., :3]

    output_image = imagem.copy()

    x = int(input("Digite a coordenada x: "))
    y = int(input("Digite a coordenada y: "))
    
    tolerancia = float(input("Digite a tolerância de cor Euclidiana (ex: 50): "))

    if not (0 <= x < imagem.shape[1] and 0 <= y < imagem.shape[0]):
        print("Erro: Coordenadas fora dos limites da imagem.")
        return

    vizinhanca = viz8(x, y, imagem)
    
    imagem_int32 = imagem.astype(np.int32)
    centro_cor = imagem_int32[y, x]

    for _, cor_pixel in vizinhanca.items():
        cor_pixel_int = cor_pixel.astype(np.int32)
        
        distancia_vizinho = np.linalg.norm(cor_pixel_int - centro_cor)
        
        if distancia_vizinho <= tolerancia:
            distancias_imagem = np.linalg.norm(imagem_int32 - cor_pixel_int, axis=-1)
            mask = distancias_imagem <= tolerancia
            output_image[mask] = [255, 0, 0]

    # Mostrar o resultado
    plt.imshow(output_image)
    plt.title(f"Semente RGB: ({x}, {y}) | Tolerância Euclidiana: {tolerancia}")
    plt.show()

if __name__ == "__main__":
    main()