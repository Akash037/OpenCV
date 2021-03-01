import cv2
import numpy as np
from matplotlib import pyplot as plt

# Rather than using IMREAD_COLOR...etc, you can also use simple numbers.
# You should be familiar with both options, so you understand what the person is doing.
# For the second parameter, you can use -1, 0, or 1. Color is 1, grayscale is 0, and the unchanged is -1.
# Thus, for grayscale, one could do img = cv2.imread('watch.jpg', 0)

img = cv2.imread('watch.jpg', 0)  # , cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
