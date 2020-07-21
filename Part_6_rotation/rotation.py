import numpy as np
import cv2
import imutils

#translation -> shifting the image on x and y palne

img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

h,w= img.shape[:2]
cX,cY = w//2,h//2

#using cv2 functions
#by 45 degree and scale 1.0
M=cv2.getRotationMatrix2D((cX,cY),45,1.0)
rotated = cv2.warpAffine(img,M,(w,h))
cv2.imshow("rotated",rotated)


#by 90 degree and scale 0.5
M=cv2.getRotationMatrix2D((cX,cY),90,0.5)
rotated2 = cv2.warpAffine(img,M,(w,h))
cv2.imshow("rotated2",rotated2)

#by -90 degree and scale 2.0 (double)
M=cv2.getRotationMatrix2D((cX,cY),-90,2.0)
rotated3 = cv2.warpAffine(img,M,(w,h))
cv2.imshow("rotated3",rotated3)


#using image utils lib

rotated_utils = imutils.rotate(img,180,None,0.5)
cv2.imshow("rotated_utils",rotated_utils)

"""
def rotate(img,angle,center=None,scale=1.0):
    h,w = img.shape[:2]

    if center is None:
        center = (w//2,h//2)

    M = cv2.getRotationMatrix2D(center,angle,scale)
    rotate = cv2.wrapAffine(img,M,(w,h))

    return rotate

"""

k = cv2.waitKey(0) & 0xFF
#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("shifted.jpg",shifted)
    cv2.imwrite("shifted_imutils.jpg",shifted_imuitls)
    cv2.destroyAllWindows()