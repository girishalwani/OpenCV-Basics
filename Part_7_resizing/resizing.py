import cv2
import numpy as np
import imutils

#read image
img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

h,w = img.shape[:2]
print(w)

#width resize
r = 150.0/w
dim=(150,int(h*r))

resize = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("resized",resize)
print(dim)

#height resize
r2 = 200.0/h
dim2=(int(w*r2),200)

resize2 = cv2.resize(img,dim2,interpolation=cv2.INTER_AREA)
cv2.imshow("resized2",resize2)


# using imutils functions

resize_utils = imutils.resize(img,width=300)
#cv2.imshow("resized_utils",resize_utils)

resize_utils2 = imutils.resize(img,height=300)
#cv2.imshow("resized_utils2",resize_utils2)


methods =[
    ("inter neartes",cv2.INTER_NEAREST),
    ("inter linear",cv2.INTER_LINEAR),
    ("inter area",cv2.INTER_AREA),
    ("inter cubic",cv2.INTER_CUBIC)
]

for (name,method) in methods:
    resized_img = imutils.resize(img,width=w*3,inter=method)
    cv2.imshow("method :{}".format(name),resized_img)
    cv2.waitKey(0)


k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("newImage.jpg",img)
    cv2.destroyAllWindows()