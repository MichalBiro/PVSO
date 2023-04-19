
#Pouzivaly sme literaturu: https://github.com/Lew-Morris/filter2D

import cv2 as cv
import numpy as np


def my_filter_2d(input_image, kernel):
    # Get size of kernel
    m = kernel.shape[0]
    n = kernel.shape[1]

    # Pad image with 1px of 0's on each side
    input_image = cv.copyMakeBorder(input_image, 1, 1, 1, 1, cv.BORDER_REFLECT)

    # Store size of image minus the padding
    dim_y = input_image.shape[0] - m + 1
    dim_x = input_image.shape[1] - n + 1

    # Create a new, zeroed array (image)
    new_image = np.zeros((dim_y, dim_x))

    # Loop through each pixel and apply the filter
    for i in range(dim_y):
        for j in range(dim_x):
            # Take the sum of each pixel and then multiply by the kernel (filter)
            conv = (np.sum(input_image[i:i + m, j:j + n] * kernel))

            # Threshold image to prevent clipping
            if conv < 0:
                new_image[i][j] = 0
            elif conv > 255:
                new_image[i][j] = 255
            else:
                new_image[i][j] = conv
    return new_image

image = cv.imread('zebra.jpg')

image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


cv.imshow('zebra', image)

laplacian = np.array([[0, 0, -1, 0, 0],
                   [0, -1, -4, -1, 0],
                   [-1, -4, 24, -4, -1],
                   [0, -1, -4, -1, 0],
                   [0, 0 , -1, 0, 0]])


gaussian = np.array([[1, 8, 12, 8 , 1 ],
                     [8, 12, 20, 12, 8],
                     [12, 20, 40, 20, 12],
                     [8, 12, 20, 12, 8],
                     [1, 8, 12, 8, 1]])/80


print(laplacian)
print(gaussian)

log = gaussian - laplacian


image1 = cv.filter2D(image, -1, gaussian)
cv.imwrite('CV_gaussian.jpg', image1)

image1_myFilter = my_filter_2d(image, gaussian)
cv.imwrite('myFilter_gaussian.jpg', image1_myFilter)

image2 = cv.filter2D(image, -1, laplacian)
cv.imwrite('CV_laplacian.jpg', image2)

image2_myFilter = my_filter_2d(image, laplacian)
cv.imwrite('myFilter_laplacian.jpg', image2_myFilter)

image3 = cv.filter2D(image1, -1, laplacian)
cv.imwrite('CV_LoG.jpg', image3)

image3_myFilter = my_filter_2d(image1_myFilter, laplacian)
cv.imwrite('myFilter_LoG.jpg', image3_myFilter)
