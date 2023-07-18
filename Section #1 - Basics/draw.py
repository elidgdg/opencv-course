import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# 1. paint the image a certian colour
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)

# draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow('rectangle', blank)

# # draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
# cv.imshow('cicle', blank)

# # draw a line
# cv.line(blank, (100,250), (300,400), (255,255,255), thickness = 3)
# cv.imshow('line', blank)

# write text on an image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)