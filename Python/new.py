import numpy as np
from PIL import Image
import cv2
import time

# Start measuring time
start_time = time.time()

imageTestLille = 'Billleder/20241119-_RVB1178 – lille.jpeg'
imageTestMellem = 'Billleder/20241119-_RVB1178 – mellem.jpeg'
imageTestStor = 'Billleder/20241119-_RVB1178 – stor.jpeg'
imageFinalBoss = 'Billleder/20250224-_RVB3287.jpg'

img = Image.open(imageFinalBoss)
im = cv2.imread(imageFinalBoss)
pixel_map = img.load()

# Ensure the image is loaded correctly
if img is None or im is None:
    raise ValueError("Image not loaded correctly")

# Define a 7x7 blur convolution matrix
convolutionMatrix = np.array([
    [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    [0.000, 0.000, 0.001, 0.002, 0.001, 0.000, 0.000],
    [0.000, 0.003, 0.013, 0.022, 0.013, 0.003, 0.000],
    [0.001, 0.013, 0.059, 0.097, 0.059, 0.013, 0.001],
    [0.002, 0.022, 0.097, 0.159, 0.097, 0.022, 0.002],
    [0.001, 0.013, 0.059, 0.097, 0.059, 0.013, 0.001],
    [0.000, 0.003, 0.013, 0.022, 0.013, 0.003, 0.000],
])

# Create a new image to store the result
result_img = Image.new("RGB", img.size)
result_pixel_map = result_img.load()

# Loop through the image with adjusted ranges to avoid out-of-bounds errors
for x in range(3, img.width - 3):
    if x == int(1/3 * (img.width - 6)):
        print("1/3 done")
    if x == int(2/3 * (img.width - 6)):
        print("2/3 done")
    for y in range(3, img.height - 3):
        rTotal = 0
        gTotal = 0
        bTotal = 0
        for i in range(7):
            for j in range(7):
                loopCordsx = x + i - 3
                loopCordsy = y + j - 3
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

# End measuring time and print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")