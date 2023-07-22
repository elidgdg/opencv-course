import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)
 
# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) # this comes out weird because opencv assumes it is bgr

# HSV to BGR 
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('Hsv-->BGR', hsv_bgr)

cv.waitKey(0)