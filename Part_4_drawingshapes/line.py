import cv2
import numpy as np

img = np.zeros((300,300,3),dtype="uint8")

cv2.imshow("canvas",img)

#create line 
start=(10,10)
end = (300,300)
green = (0,255,0)
thichkness = 5
line = cv2.line(img,start,end,green,thichkness)
cv2.imshow("line",line)


k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("line.jpg",line)
    cv2.destroyAllWindows()