import cv2
import numpy as np
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\a\\b\\11.jpeg')
gamma=2.2
gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')
cv2.imwrite('gamma_transformed11.jpg', gamma_corrected)
