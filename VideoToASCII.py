import cv2 as cv

# sets up webcam
cam = cv.VideoCapture(0)

# loop to capture video from the camera and display it on the screen
while True:
    success, img = cam.read()

    # flip image
    img = cv.flip(img, 1)

    cv.imshow("Video", img)
    cv.waitKey(15)