import cv2 

img = cv2.imread('C:/Users/naina/Downloads/Pyhton programs of PRO! classes/Pro104/images (1).jpeg')

if img is not None:
    rocket = img[120: 360, 400: 500] 
    img[0: 240, 500: 600] = rocket
    text = 'OpenCV Pro'
    cv2.putText(img, text, (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)
    cv2.imshow('img', img) 
    cv2.waitKey(0)
else:
    print("Error: Unable to read the image file.")