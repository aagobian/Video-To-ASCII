import cv2 as cv
import numpy as np


def convert_to_ascii(image):
    pixels = image.flatten().tolist()
    for pixel in pixels:
        ascii_rep = round(pixel / 4)
        if ascii_rep == 64:
            ascii_rep -= 1
        ascii_list.append(ascii_chars[ascii_rep])


# function to pixelate an input image by resizing down and back up
def pixelate_img(image, h, w):
    image = cv.resize(image, (32, 32), interpolation=cv.INTER_AREA)
    image = cv.resize(image, (h, w), interpolation=cv.INTER_AREA)
    return image


# ASCII characters to be used for image output
ascii_chars = "$@B%8&WM#*oahkbdpqwmZLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,^`'."
ascii_list = []

# set up webcam
cam = cv.VideoCapture(0)

# loop to capture video from the camera and display it on the screen
while True:
    success, img = cam.read()

    width, height, _ = img.shape

    # image preprocessing
    img = cv.flip(img, 1)
    img = pixelate_img(img, height, width)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    convert_to_ascii(img)

    # display image on screen
    cv.imshow("Video", img)

    # press esc key to exit
    key = cv.waitKey(1)
    if key == 27:
        break

# exit webcam
cam.release()
cv.destroyAllWindows()


# TODO:
# 1. Convert ASCII character list into a displayable image
# 2. Optimize program runtime
# 3. Add color?
