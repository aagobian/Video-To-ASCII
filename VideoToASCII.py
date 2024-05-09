import cv2 as cv
import numpy as np
from tkinter import *

# function to convert image grayscale values into ascii character representations
def convert_to_ascii(image):
    scaled_image = cv.resize(image, (image.shape[1] // 16, image.shape[0] // 16), interpolation=cv.INTER_AREA)
    ascii_image = np.round(scaled_image / 4).astype(int)
    ascii_image[ascii_image >= 64] = 63
    ascii_chars_array = np.array(ascii_chars)
    ascii_image_array = ascii_chars_array[ascii_image]
    ascii_text = ''.join([''.join(row) + '\n' for row in ascii_image_array])
    return ascii_text


# function to pixelate an input image by resizing down and back up
def pixelate_img(image, h, w):
    image = cv.resize(image, (32, 32), interpolation=cv.INTER_AREA)
    image = cv.resize(image, (h, w), interpolation=cv.INTER_AREA)
    return image


# ASCII characters to be used for image output
ascii_chars = "$@B%8&WM#*oahkbdpqwmZLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,^`'."
ascii_chars = list(ascii_chars)

# webcam setup
cam = cv.VideoCapture(0)

# canvas setup
root = Tk()
c = Canvas(root, height=1080, width=1920, bg="black")
c.pack()

# loop to capture video from the camera and display it on the screen
while True:
    success, img = cam.read()
    width, height, _ = img.shape

    # image preprocessing
    img = cv.flip(img, 1)
    pixel_img = pixelate_img(img, height, width)
    gray_img = cv.cvtColor(pixel_img, cv.COLOR_BGR2GRAY)
    ascii_img = convert_to_ascii(gray_img)

    # # clear canvas and update with new ascii text
    c.delete("all")
    c.create_text(0, 0, anchor="nw", text=ascii_img, font=("Courier"))
    root.update()

    # press esc key to exit
    key = cv.waitKey(1)
    if key == 27:
        break

# exit webcam
cam.release()
cv.destroyAllWindows()

# TODO:
# 1. Improve appearance of image
# 2. See if program needs to be optimized
