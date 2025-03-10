import numpy as np
from PIL import Image
import cv2

image1 = 'image2.jpeÑg'
img = Image.open(image1)
im = cv2.imread(image1)
img.show()
pixel_map = img.load()

# Ensure the image is loaded correctly
if img is None or im is None:
    raise ValueError("Image not loaded correctly")



# Loop through the image with adjusted ranges to avoid out-of-bounds errors
for x in range(im.shape[1]):
    for y in range(im.shape[0]):
        cords = (x, y)   
        pixel = img.getpixel(cords)
        rTotal =[]; gTotal = []; bTotal = []
        for i in range(0,7):
            for j in range(0,7):
                loopCordsx = ((x - 3) + i)
                loopCordsy = ((y - 3) + j)
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
                rTotal.append(r)
                gTotal.append(g)
                bTotal.append(b)
        pixel_map[x, y] = (int(sum(rTotal)/len(rTotal)), int(sum(gTotal)/len(gTotal)), int(sum(bTotal)/len(bTotal)))        
img.show()


