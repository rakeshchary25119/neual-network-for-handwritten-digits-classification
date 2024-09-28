import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')

cv.imshow("Blank image", blank)

## 1. Paint the image with certain color

# blank[:] = (0,0, 255)
# cv.imshow("Color image", blank)

## 2. Draw a rectangle 
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness = -1)
cv.imshow("rectangle image", blank)

## 3. Draw a Circle
cv.circle(blank, (250, 250), 50, (0,255,0), thickness = -1)
cv.imshow("circle", blank)

## 4. Draw A Line 
cv.line(blank, (250, 250), (200, 200), (255,255,255), thickness = 3)
cv.imshow("Line", blank)


## 5. Put text
cv.putText(blank, "Hello this is text", (290, 290), cv.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255), 2)
cv.imshow("Line", blank)

cv.waitKey(0)