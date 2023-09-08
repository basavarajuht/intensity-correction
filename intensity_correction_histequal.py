import cv2
img = cv2.imread('C:\\Users\\Lenovo\\Desktop\\a\\b\\11.jpeg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equ = cv2.equalizeHist(img1)
cv2.imshow('hist_image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('hist_equ11.jpg', equ)
