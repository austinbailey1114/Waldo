import cv2 as cv

print "---Where's Waldo---"

waldo = cv.imread('./waldo.jpg')

cv.imwrite('./newWaldo.jpg', waldo)

