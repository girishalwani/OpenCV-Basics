import numpy as np
import cv2

#read image
img = cv2.imread("./new.jpg")
cv2.imshow("img",img)

h,w = img.shape[:2]

mask = np.zeros([h,w],dtype="uint8")
cv2.rectangle(mask,(0,90),(290,450),255,-1)
cv2.imshow("masking",mask)


masked = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("masking image 1",masked)

mask2= np.zeros([h,w],dtype="uint8")
cv2.circle(mask2,(140,200),100,255,-1)
cv2.imshow("circle mask",mask2)

masked2 = cv2.bitwise_and(img,img,mask=mask2)
cv2.imshow("masked2",masked2)
k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("masked rectangle.jpg",masked)
    cv2.imwrite("masked circle.jpg",masked2)
    
    cv2.destroyAllWindows()