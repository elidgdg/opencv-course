import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow('average blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur', gauss)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow('median blur', median)



cv.waitKey(0)
