import cv2
import numpy as np

#read image
img = cv2.imread("./new.jpg")
cv2.imshow("img",img)
print(img.shape)

crop1 = img[100:200,100:250]
cv2.imshow("crop1", crop1)

crop2 = img[300:,300:]
cv2.imshow("crop2",crop2)




k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("newImage.jpg",img)
    cv2.destroyAllWindows()