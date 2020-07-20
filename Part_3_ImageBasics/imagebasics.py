import cv2
import numpy as np

img = cv2.imread("./new.jpg")

cv2.imshow("image",img)

print(img.shape)


# get  height,weight
h,w = img.shape[:2]
print("height => ",h)
print("width => ",w)


# get the b,g,r value at pixel (0,0)
b,g,r = img[0,0]
print("pixel at (0,0) is Blue:{b},Green:{g},Red:{r}".format(b=b,g=g,r=r))



#change the value of (0,0) to red
# for blue use (255,0,0)
# for green use (0,255,0)

img[0,0] = (0,0,255)  
b,g,r = img[0,0]
print("pixel at (0,0) is Blue:{b},Green:{g},Red:{r}".format(b=b,g=g,r=r))
cv2.imshow("image with red at (0,0) ",img)


#get the centre point,, so now the image is divided into four parts,
#top_left, top_right, bottom_left, Bottom_right

X,Y = w//2,h//2

top_left = img[0:Y,0:X]
cv2.imshow("top left Corner ",top_left)

top_right = img[0:Y,X:w]
cv2.imshow("top right corner ",top_right)

bottom_left = img[Y:h,0:X]
cv2.imshow("bottom left Corner ",bottom_left)

bottom_right = img[Y:h,X:w]
cv2.imshow("bottom right corner ",bottom_right)

k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("top_left.jpg",top_left)
    cv2.imwrite("top_right.jpg",top_right)
    cv2.imwrite("bottom_left.jpg",bottom_left)
    cv2.imwrite("bottom_right.jpg",bottom_right)
    cv2.destroyAllWindows()