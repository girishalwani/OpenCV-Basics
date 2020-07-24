import cv2
import numpy as np

#read image
img = cv2.imread("./noise.png")
cv2.imshow("img",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

for i in range(0,3):
    eroded = cv2.erode(gray.copy(),None,iterations=i+1)
    cv2.imshow("eroded {}".format(i+1),eroded)

for i in range(0,3):
    dilate = cv2.dilate(gray.copy(),None,iterations=i+1)
    cv2.imshow("dilate {}".format(i+1),dilate)

cv2.destroyAllWindows()

cv2.imshow("gray",gray)


kernelSize = [(3,3),(5,5),(7,7)]

for k in kernelSize:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,k)
    opening = cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)
    cv2.imshow("opening {}{}".format(k[0],k[1]),opening)


for k in kernelSize:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,k)
    closing = cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
    cv2.imshow("clossing {}{}".format(k[0],k[1]),closing)

for k in kernelSize:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,k)
    gradient = cv2.morphologyEx(gray,cv2.MORPH_GRADIENT,kernel)
    cv2.imshow("gradient {}{}".format(k[0],k[1]),gradient)


k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("newImage.jpg",img)
    cv2.destroyAllWindows()