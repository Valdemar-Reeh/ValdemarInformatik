import numpy as np
from PIL import Image
import cv2

image1 = 'image.png'


img = Image.open(image1)
im = cv2.imread(image1)
img.show()

pixel_map = img.load()
matrix = [
    [0,-1,0],
    [-1,4,-1],
    [0,-1,0]
]

# Ensure the image is loaded correctly
if img is None or im is None:
    raise ValueError("Image not loaded correctly")

def redEdit(x , y):
    matrixTotalr = []
    
    for i in range(0,3):
        for j in range(0,3):
            loopCords = (x - 1 + i, y - 1 + j)
            r, g, b = img.getpixel(loopCords)
            matrixTotalr.append(matrix[i][j]*r)
            print(i,j)
            #print(matrix[i][j], matrixTotalr)
    #print(sum(matrixTotalr)/len(matrixTotalr), matrixTotalr, len(matrixTotalr),r)
    return(sum(matrixTotalr)/len(matrixTotalr))



def greenEdit():
    matrixTotalg = []
    for i in range(0,2):
        for j in range(0,2):
            matrixTotalg.append(matrix[i][j]*g)
    return(sum(matrixTotalg)/len(matrixTotalg))

def blueEdit():
    matrixTotalb = []
    for i in range(0,2):
        for j in range(0,2):
            matrixTotalb.append(matrix[i][j]*b)
    return(sum(matrixTotalb)/len(matrixTotalb))


# Loop through the image with adjusted ranges to avoid out-of-bounds errors
for x in range(im.shape[1]):
    for y in range(im.shape[0]):
        cords = (x, y)  # Note: PIL uses (x, y) coordinates
        print(cords)
        #try:
            #print(img.getpixel(cords))
        r, g, b = img.getpixel((x, y))
            # Apply formula of grayscale: 
            
            # grayscale = (0.299*r + 0.587*g + 0.114*b)

            # setting the pixel value. 
        pixel_map[x, y] = (int(redEdit(x, y)), int(greenEdit()), int(blueEdit())) 
        #except IndexError as e:
            #print(f"IndexError at {cords}: {e}")
        
img.show()


