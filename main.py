import cv2 as cv
import numpy as np
#Read the  images


img1 = cv.imread('1.jpg')
img2 = cv.imread('2.jpg')
img3 = cv.imread('3.jpg')
img4 = cv.imread('4.jpg')
vis1 = np.concatenate((img1, img2), axis=1)
cv.imwrite('out1.jpg', vis1)
vis2 = np.concatenate((img3, img4), axis=1)
cv.imwrite('out2.jpg', vis2)
out1 = cv.imread('out1.jpg')
out2 = cv.imread('out2.jpg')
vis = np.concatenate((out1, out2), axis=0)
cv.imwrite('out.jpg', vis)

