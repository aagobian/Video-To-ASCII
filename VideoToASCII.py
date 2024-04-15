import cv2 as cv


# function to convert image grayscale values into ascii character representations
def convert_to_ascii(image):
    ascii_image = ""
    w, h = image.shape()
    for i in range(w):
        for p in range(h):
            pixel = image[i, p]
            ascii_rep = round(pixel / 4)
            if ascii_rep == 64:
                ascii_rep -= 1
            ascii_image += ascii_chars[ascii_rep]
        ascii_image += "\n"
    return ascii_image


# function to pixelate an input image by resizing down and back up
def pixelate_img(image, h, w):
    image = cv.resize(image, (32, 32), interpolation=cv.INTER_AREA)
    image = cv.resize(image, (h, w), interpolation=cv.INTER_AREA)
    return image


# ASCII characters to be used for image output
ascii_chars = "$@B%8&WM#*oahkbdpqwmZLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,^`'."

# set up webcam
cam = cv.VideoCapture(0)

# loop to capture video from the camera and display it on the screen
while True:
    success, img = cam.read()

    width, height, _ = img.shape

    # image preprocessing
    img = cv.flip(img, 1)
    pixel_img = pixelate_img(img, height, width)
    gray_img = cv.cvtColor(pixel_img, cv.COLOR_BGR2GRAY)
    ascii_img = convert_to_ascii(gray_img)

    # display image on screen
    cv.imshow("Video", ascii_img)

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
