import cv2 as cv

img=cv.imread('Photos/Esfera.jpg')
cv.imshow('Lunar',img)

#Blanco y negro

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



cv.waitKey(0)