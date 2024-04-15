import cv2 as cv


# function to pixelate an input image by resizing down and back up
def pixelate_img(image):
    width, height, _ = image.shape
    image = cv.resize(image, (32, 32), interpolation=cv.INTER_AREA)
    image = cv.resize(image, (height, width), interpolation=cv.INTER_AREA)
    return image


# set up webcam
cam = cv.VideoCapture(0)

# loop to capture video from the camera and display it on the screen
while True:
    success, img = cam.read()

    # flip image
    img = cv.flip(img, 1)
    img = pixelate_img(img)

    # display image on screen
    cv.imshow("Video", img)

    # press esc key to exit
    key = cv.waitKey(1)
    if key == 27:
        break

# exit webcam
cam.release()
cv.destroyAllWindows()
