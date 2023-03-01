import cv2 as cv
import numpy as np
from PIL import Image
import os
from PIL.ExifTags import TAGS

# Read the image

cam = cv.VideoCapture(0)

img_counter = 0

while True:
    # Initializing the frame, ret
    ret, frame = cam.read()

    if not ret:
        print('failed to grab frame')
        break

    cv.imshow('Webcam image', frame)
    # To get continuous live video feed from my laptops webcam
    k = cv.waitKey(1)

    if k%256 == 27: #ESC pressed - close app
        print('ESC pressed, closing the app')
        exit()
    elif k%256  == 32: # SPACE pressed - take picture
        img_name = "img{}.jpg".format(img_counter+1)
        frame = cv.resize(frame, (240, 240))
        cv.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

    if img_counter == 4:
        print("{} images taken!".format(img_counter))
        break


# Release the camera
cam.release()


# Read images
img1 = cv.imread('img1.jpg')
img2 = cv.imread('img2.jpg')
img3 = cv.imread('img3.jpg')
img4 = cv.imread('img4.jpg')

# Create mosaik

vis1 = np.concatenate((img1, img2), axis=1)
vis2 = np.concatenate((img3, img4), axis=1)

vis = np.concatenate((vis1, vis2), axis=0)

cv.imwrite('mosaik.jpg', vis)

cv.imshow('Mosaik', vis)

cv.waitKey()

# 1. image: Kernel mask

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

vis[0:240, 0:240] = cv.filter2D(vis[0:240, 0:240], -1, kernel)
cv.imwrite('mosaik_final.jpg', vis)

# 2. image: Rotate by 90 degrees

for j in range (0,240):
    for k in range (0,240):
        vis[j, 240 + k] = img2[239-k, j]

cv.imwrite('mosaik_final.jpg', vis)

# 3. image: channel R

vis[240:480, 0:240, 0] = 0
vis[240:480, 0:240, 1] = 0

cv.imwrite('mosaik_final.jpg', vis)

# Information about mosaic

image = Image.open('mosaik_final.jpg')
cv.imshow('Final mosaik', vis)

print('\nData type: \t'+str(image.format))
print('Image size: '+str(image.size))
print('File size:\t'+str(os.path.getsize('mosaik_final.jpg'))+' bytes')

cv.waitKey()
