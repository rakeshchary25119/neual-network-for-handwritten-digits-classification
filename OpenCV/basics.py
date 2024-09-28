import cv2 as cv
import numpy as np

img = cv.imread("cat.jpg")

cv.imshow("Cat Original", img)

## 1. Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

## 2. Blur the image using Gaussian function
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

## 3. Edge Cascading i.e., Drawing Borders
canny = cv.Canny(blur, 125, 174)
cv.imshow("Canny", canny)

## 4. Dilation - Fills the gaps, adds outer layer
dilated = cv.dilate(canny, (7,7), iterations = 3)
cv.imshow("Dilated image", dilated)

## 5. Erosion - Removes isolated noisy pixels, smoothens the boundaries.
eroded = cv.erode(canny, (7,7), iterations = 3)
cv.imshow("Eroded Image", eroded)

## 6. Resizing the image
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow("Resized Image", resized)

## 7. Cropping the image
cropped = img[50:200, 200:400]
cv.imshow("Cropped Image", cropped)


cv.waitKey(0)
