import numpy as np
import cv2


img = cv2.imread('img/fire.tiff')

x,y = 130,332#560,180

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray,(600,400))

pixel = gray_resize[y,x]

"""gray8 = np.zeros((400,600), dtype=np.uint8())
gray8 = cv2.normalize(gray_resize, gray8, 0 ,255, cv2.NORM_MINMAX)
gray8 = np.uint8(gray8)  """

cv2.circle(gray_resize,(x,y),2,(0,0,0),-1)
cv2.putText(gray_resize,"{0:.1f} C".format(pixel), (x - 80, y - 15),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)


cv2.imshow("temperatura", gray_resize)
cv2.waitKey(0)