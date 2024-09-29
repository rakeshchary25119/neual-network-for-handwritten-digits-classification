import cv2 as cv
import numpy as np

img = cv.imread("OpenCV/cat.jpg")

cv.imshow("Cat Original", img)

## 1. Translate the image along different axes.
def translate(img, x, y):
    """
    x = Right,
    y = Down,
    -x = Left,
    -y = Up
    """
    
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 40, 40)
cv.imshow("Translated Image", translated)


## Rotating the picture in Clock and Anti-Clock directions
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # (centre, angle, scaling)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow("Rotated Image", rotated)

## 3. Flip the image 
"""
1: flip horizontally,
0: flip vertically,
-1: flip by both horizontally and vertically
"""
flipped = cv.flip(img, 0)
cv.imshow("Flipped image", flipped)


cv.waitKey(0)