# QR Code Detection and Authorization

This code is an implementation of QR code detection and authorization using OpenCV and the pyzbar library. It captures video from a webcam, detects QR codes in frames, and checks if the decoded data is authorized based on a list of authorized QR code IDs stored in a text file.

## Prerequisites
Before running this code, make sure you have the following libraries installed:

- OpenCV
- numpy
- math
- pyzbar

You can install these dependencies using pip:

```bash
pip install opencv-python numpy pyzbar


## Pré-requisitos
Antes de executar este código, certifique-se de ter as seguintes bibliotecas instaladas:

OpenCV
numpy
math
pyzbar
Você pode instalar essas dependências usando o pip:

```bash
pip install opencv-python numpy pyzbar
```
## Usage
1.Ensure your webcam is connected to the computer.
2. Save the IDs of authorized QR codes in a text file. Each ID should be on a separate line.
3. Update the file path in the code to point to your text file containing the IDs of authorized QR codes.
4. Run the script.

## Code Explanation
1. Import the necessary libraries:
```bash
import cv2
import numpy as np
import math
from pyzbar.pyzbar import decode
```
2. Define a function to calculate the Euclidean distance between two points:
```bash
def euclideanDistance(x, y, x1, y1):
    euclideanDist = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    return euclideanDist
```    
3. Initialize the video capture object and set the frame size:
```bash
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
```
4. Read the list of authorized QR code IDs from the text file:
```bash
with open('OPENCV/QrCode_project/Id_QRcode.txt') as f:
    myDatalist = f.read().splitlines()
```    
5. Start an infinite loop to continuously read frames from the webcam:
```bash
while True:
    success, img = cap.read()
```
6. Decode the QR codes in the captured frame and check for authorization:
```bash
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        
        if myData in myDatalist:
            myOutput = 'Autorizado'
            myColor = (0, 255, 0)
        else:
            myOutput = 'Não Autorizado'
            myColor = (0, 0, 255)
        
        print(myOutput)
```        
7. Draw the boundary of the QR code, display the authorization status, and calculate the center and width of the QR code:
```bash
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)
        
        # Coordenadas dos pontos da caixa
        x
```   
## Support
If you encounter any issues or have questions regarding the code, feel free to open an issue in this repository. We'll do our best to assist you.


## License
This project is licensed under the MIT License. Feel free to use it in accordance with the terms of the license.  