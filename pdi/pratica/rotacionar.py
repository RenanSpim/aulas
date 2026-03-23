import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def main():
    imagem = mpimg.imread('calcio.jpg')
    output_image = np.zeros([imagem.shape[1], imagem.shape[0], imagem.shape[2]], dtype=np.uint8)

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            output_image[j][i] = imagem[i][j]

        
    plt.imshow(output_image)
    plt.show()

if __name__ == "__main__":
    main()
