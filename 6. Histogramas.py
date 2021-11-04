import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photos/cats.jpg')
cv.imshow('Lunar',img)


#Black and White
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

#GRAY SCALE HISTOGRAM

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])

#COLOUR HISTOGRAM
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    
cv.waitKey(0)