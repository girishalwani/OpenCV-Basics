import numpy as np
import cv2


rectangle = np.zeros([300,300],dtype="uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("rectangle",rectangle)

circle = np.zeros([300,300],dtype="uint8")
cv2.circle(circle,(150,150),150,255,-1)
cv2.imshow("circle",circle)

#bitwise and
bitwise_and = cv2.bitwise_and(rectangle,circle)
cv2.imshow("and",bitwise_and)

bitwise_or = cv2.bitwise_or(rectangle,circle)
cv2.imshow("or",bitwise_or)

bitwise_xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("xor",bitwise_xor)

bitwise_not = cv2.bitwise_not(circle)
cv2.imshow("not",bitwise_not)

k = cv2.waitKey(0) & 0xFF

#pres ESC to exit
if k==27:
    cv2.destroyAllWindows()

#press 's' to save and exit
elif k == ord("s"):
    cv2.imwrite("and.jpg",bitwise_and)
    cv2.imwrite("or.jpg",bitwise_or)
    cv2.imwrite("xor.jpg",bitwise_xor)
    cv2.imwrite("not.jpg",bitwise_not)
    cv2.destroyAllWindows()