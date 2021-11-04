import cv2 as cv

#Re-escalado de Imagen

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int( frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions, interpolation= cv.INTER_AREA)

#Lectura de Imagenes

img= cv.imread('Photos/Lunar.jpg')

img_resized=rescaleFrame(img,1.3)

cv.imshow('Lunar', img)
cv.imshow('Lunar Re escalado',img_resized)

cv.waitKey(0)





# =============================================================================
# #Lectura de Videos
# 
# capture=cv.VideoCapture('Videos/Eevee.mp4')
# 
# while True:
#     isTrue,frame=capture.read()
#     frame_resized=rescaleFrame(frame,1.2)
#     cv.imshow('Video',frame)
#     cv.imshow('Video Re escalado', frame_resized)
#     
#     if cv.waitKey(20) & 0xFF==ord('x'):
#         break
#     
# capture.release()
# cv.destroyAllWindows()
# =============================================================================
