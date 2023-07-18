import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray0', gray)


# blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded', eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)