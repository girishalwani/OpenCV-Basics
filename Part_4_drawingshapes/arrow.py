import cv2
import numpy as np

img = np.zeros((300,300,3),dtype="uint8")

cv2.imshow("canvas",img)

#create line 
start=(10,10)
end = (200,200)
green = (0,255,0)
thichkness = 5
arrowedline = cv2.arrowedLine(img,start,end,green,thichkness)
cv2.imshow("arrowedLine",arrowedline)


k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("arrowedLine.jpg",arrowedline)
    cv2.destroyAllWindows()