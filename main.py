import cv2 as cv
import numpy as np
from PIL import Image
import os
from PIL.ExifTags import TAGS
#Read the  image

# intialize the webcam and pass a constant which is 0
cam = cv.VideoCapture(0)

# title of the app
cv.namedWindow('python webcam screenshot app')

# let's assume the number of images gotten is 0
img_counter = 1

# while loop
while True:
    # intializing the frame, ret
    ret, frame = cam.read()
    # if statement
    if not ret:
        print('failed to grab frame')
        break
    # the frame will show with the title of test
    cv.imshow('test', frame)
    #to get continuous live video feed from my laptops webcam
    k  = cv.waitKey(1)
    # if the escape key is been pressed, the app will stop
    if k%256 == 27:
        print('escape hit, closing the app')
        break
    # if the spacebar key is been pressed
    # screenshots will be taken
    elif k%256  == 32:
        # SPACE pressed
        img_name = "img{}.jpg".format(img_counter)
        frame = cv.resize(frame, (240, 240))
        cv.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
    if img_counter > 4:
        print("{} images taken !".format(img_counter-1))
        break


# release the camera
cam.release()


# nacitanie obrazkov
img1 = cv.imread('img1.jpg')
img2 = cv.imread('img2.jpg')
img3 = cv.imread('img3.jpg')
img4 = cv.imread('img4.jpg')

# tvorba mozaiky

vis1 = np.concatenate((img1, img2), axis=1)
cv.imwrite('out1.jpg', vis1)
vis2 = np.concatenate((img3, img4), axis=1)
cv.imwrite('out2.jpg', vis2)
vis = np.concatenate((vis1, vis2), axis=0)
cv.imwrite('mozaika1.jpg', vis)

cv.imshow("mozaika1 ", vis)


#otocenie 2 fotky o 90 stupnov

whiteFrame = 255 * np.ones((240,240,3), np.uint8) # uobi cisty obrazok
for j in range (0,240):
    for k in range (0,240):
        whiteFrame[j,k]=img2[239-k,j]

cv.imwrite('rot.jpg', whiteFrame)
img2 = cv.imread('rot.jpg')


# tvorba mozaiky

vis1 = np.concatenate((img1, img2), axis=1)
cv.imwrite('out1.jpg', vis1)
vis2 = np.concatenate((img3, img4), axis=1)
cv.imwrite('out2.jpg', vis2)
vis = np.concatenate((vis1, vis2), axis=0)
cv.imwrite('mozaika2.jpg', vis)


# R zlozka z 3 obrazka

img3[:,:,0] = 0
img3[:,:,1] = 0
cv.imwrite('red.jpg', img3)

vis[240:480,0:240,0] = 0
vis[240:480,0:240,1] = 0
cv.imwrite('mozaika3.jpg', vis)

# Kernel maska

kernel = np.array([[0, -1, 0],  # zaostrenie maska
                   [-1, 5, -1],
                   [0, -1, 0]])

vis[0:240,0:240] = cv.filter2D(vis[0:240,0:240], -1, kernel)
cv.imwrite('mozaika_final.jpg', vis)


image = Image.open('mozaika_final.jpg')
info_dict = {
    "Image Size": image.size,
    "Image Format": image.format,
    "Image Mode": image.mode,
}
file_path ='/Users/micha/Documents/Skola/FEI/LS/PVSO/cvicenie/PVSO/mozaika_final.jpg'
#vypis parametrov obrazka
print('datovy typ: '+str(image.format))
print('rozmer: '+str(image.size))
print('velkost '+str(os.path.getsize(file_path))+' bytes')


