import cv2
import numpy as np

#read image
img = cv2.imread("./car.png")
cv2.imshow("img",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

rectkernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,5))
blackhat = cv2.morphologyEx(gray.copy(),cv2.MORPH_BLACKHAT,rectkernel)
cv2.imshow("backhat",blackhat)

whitehat = cv2.morphologyEx(gray.copy(),cv2.MORPH_TOPHAT,rectkernel)
cv2.imshow("whitehat",whitehat)



k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("blackhat.jpg",blackhat)
    cv2.imwrite("whitehat.jpg",whitehat)
    cv2.destroyAllWindows()