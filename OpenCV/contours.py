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

gray_canny_contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

## Threshold Mapping instead of Blurring  and Edge Cascading

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
thresh_contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'gray_canny_contours has {len(gray_canny_contours)} contour(s)')
print(f'thresh_contours {len(thresh_contours)} contour(s)')


## Drawing all the contours on Blank image for better visualization.
"""
First Param: canvas i.e. Blank image to draw
Second Param: contours
Third Param: Number of Contours (in this all)
Fourth Param: Color of the contours
Fifth Param: Scaling of the Contours.
"""
# Gray canny plot
contour_img = cv.drawContours(blank, gray_canny_contours, -1, (255, 0, 0), 1)
cv.imshow("Contour Image", contour_img)



## Threshold mapping
blank = np.zeros(img.shape, dtype = 'uint8')
contour_img_thresh = cv.drawContours(blank, thresh_contours, -1, (0, 0, 255), 1)
cv.imshow("Thresh Image", contour_img_thresh)


cv.waitKey(0)