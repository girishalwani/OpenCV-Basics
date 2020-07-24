import cv2
import numpy as np

#read image
img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

#splitting and merging channels
b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)


merge = cv2.merge([b,g,r])
cv2.imshow("merge",merge)

zero = np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow("red",cv2.merge([zero,zero,r]))
cv2.imshow("green",cv2.merge([zero,g,zero]))
cv2.imshow("blue",cv2.merge([b,zero,zero]))
cv2.imshow("gr",cv2.merge([zero,g,r]))

k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("newImage.jpg",img)
    cv2.destroyAllWindows()