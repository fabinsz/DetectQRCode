import cv2
import numpy as np
import math
from pyzbar.pyzbar import decode



def euclideanDistance(x, y, x1, y1):
    euclideanDist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return euclideanDist

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)



with open('Id_QRcode.txt') as f:
    myDatalist = f.read().splitlines()

while True: 
    success, img = cap.read()      
    
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        
        if myData in myDatalist:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
        
        print(myOutput)
        
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
        
        # Coordinates of the box points
        x, y, w, h = pts2
        x1, y1 = x + w, y + h
        qrWidth = euclideanDistance(x, y, x1, y1)
        
        
        # Calculate the center of the QR code.
        center_x = int((x + x1) / 2)
        center_y = int((y + y1) / 2)

        # Draw a red dot at the center of the QR code
        cv2.circle(img, (center_x, center_y), 5, (255, 0, 0), -1)

        
        cv2.putText(img, f"Center: ({center_x}, {center_y})", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

      
        print("Center:", center_x, center_y)

    cv2.imshow('Result', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

