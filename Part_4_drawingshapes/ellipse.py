import cv2
import numpy as np

img = np.zeros((300,300,3),dtype="uint8")

cv2.imshow("canvas",img)

#create line 
center=(100,100)
axes = (50,30)
green = (0,255,0)
startAngle = 0
endAngle = 360
thichkness = 5
ellips = cv2.ellipse(img,center=center,axes=axes,startAngle=startAngle,endAngle=endAngle,color=green,thickness=thichkness)
cv2.imshow("ellispse",ellips)


k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("arrowedLine.jpg",ellips)
    cv2.destroyAllWindows()