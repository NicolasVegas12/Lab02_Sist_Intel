import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

img= cv.imread('Photos/Lunar.jpg')
cv.imshow('Lunar',img)

#Portion of pixels
blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank)

#Drawing a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=cv.FILLED)
cv.imshow('rectangle',blank)

#Draw a Circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)


cv.waitKey(0)