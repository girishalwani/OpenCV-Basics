import cv2
import numpy as np

img = np.zeros((300,300,3),dtype="uint8")

cv2.imshow("canvas",img)

#create line 
start=(50,50)
end = (250,250)
green = (0,255,0)
thichkness = -1
rect = cv2.rectangle(img,start,end,green,thichkness)
cv2.imshow("rectangle",rect)


k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("rectangle.jpg",rect)
    cv2.destroyAllWindows()