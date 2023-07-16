import cv2 as cv

img = cv.imread('C:/Users/gatwa/computer-science/opencv-course/Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)