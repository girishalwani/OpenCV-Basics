import numpy as np
import cv2

img = cv2.imread("./rbg.png")


# B,G,R using split function

"""
cv2.imshow("img",img)
cv2.waitKey(10)

b,g,r = cv2.split(img)

cv2.imshow("blue",b)
cv2.waitKey(10)

cv2.imshow("green",g)
cv2.waitKey(10)

cv2.imshow("red",r)
cv2.waitKey(10)
"""
#B,G,R using numpy array

blue = img[:,:,0]
green = img[:,:,1]
red = img[:,:,2]

cv2.imshow("blue",blue)
cv2.waitKey(10)

cv2.imshow("green",green)
cv2.waitKey(10)

cv2.imshow("red",red)
cv2.waitKey(10)

print(img.shape)


k=cv2.waitKey(0) & 0xFF

#ESC to exit 
if(k==27):
    cv2.destroyAllWindows()

#press 's' to save image
elif k == ord("s"):
    cv2.imwrite("blue.jpg",blue)
    cv2.imwrite("green.jpg",green)
    cv2.imwrite("red.jpg",red)
    cv2.destroyAllWindows()