import cv2
import numpy as np
import imutils

#read image
img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

flip1 = cv2.flip(img,1)
cv2.imshow("horizonatl",flip1)

flip2 = cv2.flip(img,0)
cv2.imshow("vertical",flip2)

flip3 = cv2.flip(img,-1)
cv2.imshow("both",flip3)




k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("newImage.jpg",img)
    cv2.destroyAllWindows()