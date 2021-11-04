import cv2 as cv

img=cv.imread('Photos/Esfera.jpg')
cv.imshow('Lunar',img)

#Blanco y negro

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# =============================================================================
# #Blur
# blur= cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
# 
# #Edge Cascade
# cany = cv.Canny(img,25,75)
# cv.imshow('Canny Edges', cany)
# 
# #Dilating the image
# dilated = cv.dilate(cany,(3,3), iterations = -1)
# cv.imshow('Dilated', dilated)
# 
# =============================================================================

#HSL
hsl = cv.cvtColor(img,cv.COLOR_BGR2HLS)
cv.imshow('HSL',hsl)

cv.waitKey(0)