
import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('C:/Users/Richard/Pictures/IMG/test1.tif',0)
print(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(img.ravel(),256,[0,256])
plt.show()

ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (ret2)
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (ret3)
plt.hist(blur.ravel(),256,[0,256])
plt.show()

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.hist(img.ravel(),256)
plt.subplot(223),plt.imshow(blur,'gray')
plt.subplot(224),plt.imshow(th3,'gray')

plt.show()
