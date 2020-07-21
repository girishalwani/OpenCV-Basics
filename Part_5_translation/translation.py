import numpy as np
import cv2
import imutils

#translation -> shifting the image on x and y palne

img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

h,w= img.shape[:2]

#using cv2 functions.
T = np.float32([[1,0,w//4],[0,1,h//4]])
shifted = cv2.warpAffine(img,T,(w,h))
cv2.imshow("shifted", shifted)



#using imutils functions
shifted_imuitls = imutils.translate(img,50,50)
cv2.imshow("shifted_imuitls", shifted_imuitls)


"""
imutil.translate behind the scenes

def translate(img,x,y):
    M=np.float32([[1,0,x],[1,0,y]])
    shifted = cv2.wrapAffine(img,M,(img.shape[1],img.shape[0]))
    return shifted

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