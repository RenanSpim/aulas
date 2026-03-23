import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def main():
    imagem = mpimg.imread('calcio2.jpg')
    plt.imshow(imagem)
    plt.show()

    print("largura =", imagem.shape[1], "\naltura =", imagem.shape[0])

    if imagem.shape[2] == 1:
        print("quantizacao = 1 (Escala de Cinza)")
    elif imagem.shape[2] == 2:
        print("quantizacao = 2 (Escala de Cinza + Alfa)")
    elif imagem.shape[2] == 3:
        print("quantizacao = 3 (RGB)")
    elif imagem.shape[2] == 4:
        print("quantizacao = 4 (RGBA)")
    else:
        print("quantizacao = Desconhecido")

if __name__ == "__main__":
    main()
