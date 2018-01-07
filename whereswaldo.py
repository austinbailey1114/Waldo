import cv2 as cv
from matplotlib import pyplot as plt

print "---Where's Waldo---"

## read in images
whereswaldo = cv.imread('./whereswaldo.jpg')
waldo = cv.imread('./waldo.jpg')
## get width and height of waldo
_, w, h = waldo.shape[::-1]

## method
method = eval('cv.TM_CCOEFF_NORMED')


## match template, and get top left corner of matched area
res = cv.matchTemplate(whereswaldo, waldo, method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc

## build and draw rectangle around matched area
bottom_right = (top_left[0] + w, top_left[1] + h)
cv.rectangle(whereswaldo, top_left, bottom_right, 255, 2)

## show result
plt.imshow(whereswaldo, cmap = 'gray')
plt.title("Where's Waldo")
plt.show()
