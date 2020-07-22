import cv2
import numpy as np

img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

#print("max of 255"+str(cv2.add(np.uint8([200]),np.uint8([100]))))

#print("min of 0 "+str(cv2.subtract(np.uint8([50]),np.uint8([100]))))

M = np.ones(img.shape,dtype="uint8")*100
added = cv2.add(img,M)
cv2.imshow("added",added)



M = np.ones(img.shape,dtype="uint8")*50
subtract = cv2.subtract(img,M)
cv2.imshow("subtract",subtract)



k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("add.jpg",added)
    cv2.imwrite("subtract.jpg",subtract)
    cv2.destroyAllWindows()