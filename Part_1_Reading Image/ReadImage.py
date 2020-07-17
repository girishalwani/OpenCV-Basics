import cv2
import numpy as np

#read image
img = cv2.imread("./new.jpg")

#width , height and channels for image
print("width => ",img.shape[0])
print("height => ",img.shape[1])
print("channels =>",img.shape[2])

cv2.imshow("img",img)

k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("newImage.jpg",img)
    cv2.destroyAllWindows()