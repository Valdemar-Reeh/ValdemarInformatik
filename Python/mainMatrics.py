import numpy as np
from PIL import Image
import cv2

image1 = 'Billleder/image2.jpeg'
imageTestLille = 'Billleder/20241119-_RVB1178 – lille.jpeg'
#imageTestMellem = '20241119-_RVB1178 – mellem.jpeg'
#imageTestStor = '20241119-_RVB1178 – stor.jpeg'

img = Image.open(image1)
im = cv2.imread(image1)
img.show()
pixel_map = img.load()

# Ensure the image is loaded correctly
if img is None or im is None:
    raise ValueError("Image not loaded correctly")

# Define a 5x5 convolution matrix
# The sum of all elements in the matrix must not be 0
# Gaussian blur
convolutionMatrix = np.array([
    [1, 2, 4, 2, 1],
    [2, 4, 8, 4, 2],
    [4, 8, 16, 8, 4],
    [2, 4, 8, 4, 2],
    [1, 2, 4, 2, 1]
])
# Edge detection
#convolutionMatrix = np.array([
#    [-1, -1, 0, 1, 1],
#    [-1, -1, 0, 1, 1],
#    [-1, -1, 0, 1, 1],
#    [-1, -1, 0, 1, 1],
#    [-1, -1, 0, 1, 1]
#])

# Loop through the image with adjusted ranges to avoid out-of-bounds errors
for x in range(im.shape[1]):
    for y in range(im.shape[0]):
        cords = (x, y)   
        pixel = img.getpixel(cords)
        rTotal =[]; gTotal = []; bTotal = []
        for i in range(0,5):
            for j in range(0,5):
                loopCordsx = ((x - 2) + i)
                loopCordsy = ((y - 2) + j)
                if loopCordsx < 0:
                    rTotal.append(0)
                    gTotal.append(0)
                    bTotal.append(0)
                    continue
                if loopCordsy < 0:
                    rTotal.append(0)
                    gTotal.append(0)
                    bTotal.append(0)
                    continue
                if loopCordsx >= img.width:
                    loopCordsx = img.width - 1
                if loopCordsy >= img.height:
                    loopCordsy = img.height - 1
                r, g, b = img.getpixel((loopCordsx, loopCordsy))
                rTotal.append(r * convolutionMatrix[i][j])
                gTotal.append(g * convolutionMatrix[i][j])
                bTotal.append(b * convolutionMatrix[i][j])
        try:
            pixel_map[x, y] = (
            int(sum(rTotal) / sum(convolutionMatrix.flatten())), 
            int(sum(gTotal) / sum(convolutionMatrix.flatten())), 
            int(sum(bTotal) / sum(convolutionMatrix.flatten()))
            )
        except ZeroDivisionError:
            pixel_map[x, y] = (
                int(sum(rTotal)),
                int(sum(gTotal)),
                int(sum(bTotal))
            )
        else:
            pixel_map[x, y] = (
                int(sum(rTotal)),
                int(sum(gTotal)),
                int(sum(bTotal))
            )
img.show()


