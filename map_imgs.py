import numpy as np
import cv2


img = cv2.imread('img/fire/fire.tiff')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_resize = cv2.resize(gray,(600,400))

gray8 = np.zeros((400,600), dtype=np.uint8())
gray8 = cv2.normalize(gray_resize, gray8, 0 ,255, cv2.NORM_MINMAX)
gray8 = np.uint8(gray8)  

inferno_palette = cv2.applyColorMap(gray8,cv2.COLORMAP_INFERNO)
jet_palette = cv2.applyColorMap(gray8,cv2.COLORMAP_JET)
viridis_palette = cv2.applyColorMap(gray8,cv2.COLORMAP_VIRIDIS)

#cv2.imshow("gray8", gray8)
#cv2.imshow("inferno", inferno_palette)
cv2.imshow("jet", jet_palette)
#cv2.imshow("viridis", viridis_palette)

cv2.waitKey(0)