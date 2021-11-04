import cv2 as cv

img=cv.imread('Photos/Esfera.jpg')
cv.imshow('Lunar',img)


# =============================================================================
# #HSL
# hsl = cv.cvtColor(img,cv.COLOR_BGR2HLS)
# cv.imshow('HSL',hsl)
# =============================================================================

#Binary
grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh, blackAndWhiteImage = cv.threshold(grayImage, 127, 255, cv.THRESH_BINARY)
cv.imshow('Black white image', blackAndWhiteImage)

cv.waitKey(0)