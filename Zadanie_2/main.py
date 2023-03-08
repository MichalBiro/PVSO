from ximea import xiapi
import cv2 as cv
import numpy as np
from PIL import Image
import os
from PIL.ExifTags import TAGS
import glob

### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###

#create instance for first connected camera
cam = xiapi.Camera()

#start communication
#to open specific device, use:
#cam.open_device_by_SN('41305651')
#(open by serial number)
# print('Opening first camera...')
# cam.open_device()
#
# #settings
# cam.set_exposure(10000)
# cam.set_param('imgdataformat','XI_RGB32')
# cam.set_param('auto_wb', 1)
# print('Exposure was set to %i us' %cam.get_exposure())
#
# #create instance of Image to store image data and metadata
# img = xiapi.Image()
#
# #start data acquisition
# print('Starting data acquisition...')
# cam.start_acquisition()
#
# img_counter = 0
#
# wanted_image_count = 10
#
# while True:
#     # Initializing the frame, ret
#     cam.get_image(img)
#     frame = img.get_image_data_numpy()
#     frame = cv.resize(frame, (800, 800))
#
#     # if not ret:
#     #    print('failed to grab frame')
#     #    break
#
#     cv.imshow('Webcam image', frame)
#     # To get continuous live video feed from my laptops webcam
#     k = cv.waitKey(1)
#
#     if k%256 == 27: # ESC pressed - close app
#         print('ESC pressed, closing the app')
#         exit()
#     elif k%256  == 32: # SPACE pressed - take picture
#         img_name = "img{}.jpg".format(img_counter+1)
#         frame = cv.resize(frame, (800, 800))
#         cv.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1
#
#     if img_counter == wanted_image_count:
#         print("{} images taken!".format(img_counter))
#         break
#
#
# #stop data acquisition
# print('Stopping acquisition...')
# cam.stop_acquisition()
#
# #stop communication
# cam.close_device()

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:5].T.reshape(-1, 2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('*.jpg')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,5), None)
    # If found, add object points, image points (after refining them)
    if ret:
        print("test")
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,5), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey()
# cv.destroyAllWindows()

print('calibrate')

ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print('----')
print(ret)
print('----')
print(mtx)
print('----')
print(dist)
print('----')
print(rvecs)
print('----')
print(tvecs)

img = cv.imread('img1.jpg')
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

print('undistort')
# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult.png', dst)

print('end')