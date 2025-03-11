import numpy as np
from PIL import Image
import cv2

image1 = 'Billleder/image2.jpeg'
imageTestLille = 'Billleder/20241119-_RVB1178 – lille.jpeg'
#imageTestMellem = 'Billleder/20241119-_RVB1178 – mellem.jpeg'
#imageTestStor = 'Billleder/20241119-_RVB1178 – stor.jpeg'

img = Image.open(imageTestLille)
im = cv2.imread(imageTestLille)
pixel_map = img.load()

# Ensure the image is loaded correctly
if img is None or im is None:
    raise ValueError("Image not loaded correctly")

# Define a 3x3 edge detection convolution matrix
convolutionMatrix = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Create a new image to store the result
result_img = Image.new("RGB", img.size)
result_pixel_map = result_img.load()

# Loop through the image with adjusted ranges to avoid out-of-bounds errors
for x in range(1, img.width - 1):
    for y in range(1, img.height - 1):
        rTotal = 0
        gTotal = 0
        bTotal = 0
        for i in range(3):
            for j in range(3):
                loopCordsx = x + i - 1
                loopCordsy = y + j - 1
                r, g, b = img.getpixel((loopCordsx, loopCordsy))
                rTotal += r * convolutionMatrix[i][j]
                gTotal += g * convolutionMatrix[i][j]
                bTotal += b * convolutionMatrix[i][j]
        
        # Clamp the values to be between 0 and 255
        rTotal = max(0, min(255, rTotal))
        gTotal = max(0, min(255, gTotal))
        bTotal = max(0, min(255, bTotal))
        
        result_pixel_map[x, y] = (int(rTotal), int(gTotal), int(bTotal))

# Show the result image
result_img.show()

