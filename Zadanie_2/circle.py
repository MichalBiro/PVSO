# PVSO / Zadanie 2 / 3. uloha
# detekcia kruhov

import sys
import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

img_counter = 0

while True:
    # Initializing the frame, ret
    ret, frame = cam.read()

    if not ret:
        print('failed to grab frame')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=200, param2=30,
                              minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(frame, center, radius, (255, 0, 255), 3)

    cv.imshow("detected circles", frame)

    #cv.imshow('Webcam image', frame)
    # To get continuous live video feed from my laptops webcam
    k = cv.waitKey(1)

    if k%256 == 27: # ESC pressed - close app
        print('ESC pressed, closing the app')
        exit()
    elif k%256  == 32: # SPACE pressed - take picture
        img_name = "img.jpg"
        #frame = cv.resize(frame, (240, 240))
        #cv.imwrite(img_name, frame)
        #print("{} written!".format(img_name))
        #src = cv.imread('img.jpg')


"""
def main(argv):
    default_file = 'img.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=200, param2=30,
                              minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(src, center, radius, (255, 0, 255), 3)

    cv.imshow("detected circles", src)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
"""

