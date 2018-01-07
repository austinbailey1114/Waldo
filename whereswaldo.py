import cv2 as cv
from matplotlib import pyplot as plt

print "---Where's Waldo---"

#feature detection

## read in image
waldo = cv.imread('./waldo.jpg')

## create ORB object, detect and compute key points on waldo image
orb = cv.ORB_create()
kp = orb.detect(waldo, None)
kp, des = orb.compute(waldo, kp)

## draw the key points of waldo on 'img'
img = cv.drawKeypoints(waldo, kp, None)

## show 'img'
cv.imshow('image', img)

