import cv2 as cv

# reading images

# img = cv.imread('C:/Users/gatwa/computer-science/opencv-course/Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)

# reading videos

capture = cv.VideoCapture('C:/Users/gatwa/computer-science/opencv-course/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()