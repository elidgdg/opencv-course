import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # Images, videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live video (webcam etc)
    capture.set(3, width)
    capture.set(4, height)

# reading images
img = cv.imread('C:/Users/gatwa/computer-science/opencv-course/Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# reading videos
capture = cv.VideoCapture('C:/Users/gatwa/computer-science/opencv-course/Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale= .2)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# capture.release()
cv.destroyAllWindows()

