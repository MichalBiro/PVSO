#Begining of zadanie 3

# bonusova uloha na 5. prednasku

import cv2 as cv
import numpy as np

image = cv.imread('zebra.jpg')

cv.imshow('zebra', image)

laplacian = np.array([[0, 0, -1, 0, 0],
                   [0, -1, -4, -1, 0],
                   [-1, -4, 24, -4, -1],
                   [0, -1, -4, -1, 0],
                   [0, 0 , -1, 0, 0]])

gaussian = np.array([[1, 2, 4, 2 , 1 ],
                   [2, 4, 8, 4, 2],
                   [4, 8, 10, 8, 4],
                   [2, 4, 8, 4, 2],
                   [1, 2, 4, 2, 1]])/91

# gaussian = np.array([[1, 8, 12, 8 , 1 ],
#                      [8, 12, 20, 12, 8],
#                      [12, 20, 40, 20, 12],
#                      [8, 12, 20, 12, 8],
#                      [1, 8, 12, 8, 1]])/

print(laplacian)
print(gaussian)

log = gaussian - laplacian

# image1 = cv.filter2D(image, -1, kernel1)
# cv.imwrite('image1.jpg', image1)
#
# image2 = cv.filter2D(image, -1, kernel2)
# cv.imwrite('image2.jpg', image2)
#
# final =  image1;
# cv.imwrite('final.jpg', final)

image1 = cv.filter2D(image, -1, gaussian)
cv.imwrite('gaussian.jpg', image1)

image2 = cv.filter2D(image, -1, laplacian)
cv.imwrite('laplacian.jpg', image2)

image3 = cv.filter2D(image1, -1, laplacian)
cv.imwrite('LoG.jpg', image3)
