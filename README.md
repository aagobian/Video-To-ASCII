# Video to Ascii Generator

This is a small project I created that captures live webcam video and converts it into an ASCII art representation in real-time. It uses OpenCV to handle video capture and image processing, transforming each frame of the video into grayscale, scaling it down, and then mapping grayscale values to ASCII characters based on their intensity. The ASCII art is then displayed on a Tkinter canvas, updating dynamically with the video feed. You can exit the program by pressing the "0" key.




## Installing required libraries

The required libraries are OpenCV, NumPy, and Tkinter (included with Python installation).


```bash
pip install opencv-python numpy
```

