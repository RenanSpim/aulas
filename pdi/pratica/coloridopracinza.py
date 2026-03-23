import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def main():
    imagem = mpimg.imread('calcio2.jpg')
    output_image = np.zeros([imagem.shape[0], imagem.shape[1], 1], dtype=np.uint8)

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            r = imagem[i][j][0]
            g = imagem[i][j][1]
            b = imagem[i][j][2]

            # cinza = (r + g + b) // 3
            cinza = (0.299 * r + 0.587 * g + 0.114 * b)

            output_image[i][j][0] = cinza
            # output_image[i][j][1] = cinza
            # output_image[i][j][2] = cinza

        
    plt.imshow(output_image, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()
