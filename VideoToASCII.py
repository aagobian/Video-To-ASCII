import cv2 as cv
import numpy as np
from tkinter import *


# function to convert image grayscale values into ascii character representations
def convert_to_ascii(image):
    scaled_image = cv.resize(image, (image.shape[1] // 16, image.shape[0] // 16), interpolation=cv.INTER_AREA)
    ascii_image = np.round(scaled_image / 16).astype(int)
    ascii_image[ascii_image >= 16] = 15
    ascii_chars_array = np.array(ascii_chars)
    ascii_image_array = ascii_chars_array[ascii_image]
    ascii_text = ""
    for row in ascii_image_array:
        ascii_text += ''.join(row)
        ascii_text += '\n'
    return ascii_text


def detect_key_press(event):
    if event.char == "0":
        cam.release()
        cv.destroyAllWindows()
        root.quit()


# ASCII characters to be used for image output
ascii_chars = "@$&%#?!*+=-:.   "
ascii_chars = list(ascii_chars)

# webcam setup
cam = cv.VideoCapture(0)

# canvas setup
root = Tk()
root.title("Press 0 to exit.")
root.bind('0', detect_key_press)
c = Canvas(root, height=1080, width=1920, bg="black")
c.pack()

# loop to capture video from the camera and display it on the screen
while True:
    success, img = cam.read()
    width, height, _ = img.shape

    # image preprocessing
    img = cv.flip(img, 1)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ascii_img = convert_to_ascii(gray_img)

    # clear canvas and update with new ascii text
    c.delete("all")
    c.create_text(0, 0, anchor="nw", text=ascii_img, font="Courier")
    root.update()
