import cv2 as cv
import numpy as np


img = cv.imread("OpenCV/cat.jpg")
cv.imshow("Cat Original", img)

blank = np.zeros(img.shape, dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

"""
First Param: image
Second Param: Which type of contours -\
        (RETR_LIST: every type,\
        RETR_TREE: all hierarchical,\
        RETR_EXTERNAL: all external boundaries).
Third Param: Approximating the Boundaries.
"""
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

## Drawing all the contours on Blank image for better visualization.
"""
First Param: canvas i.e. Blank image to draw
Second Param: contours
Third Param: Number of Contours (in this all)
Fourth Param: Color of the contours
Fifth Param: Scaling of the Contours.
"""
contour_img = cv.drawContours(blank, contours, -1, (255, 0, 0), 1)
cv.imshow("Contour Image", contour_img)

cv.waitKey(0)