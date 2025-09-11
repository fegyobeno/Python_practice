import numpy as np
import cv2 # pip3 install opencv-python

image_path = 'people2.jpg'
modellnames = 'objectdataset.data' 
modell = 'pretrained.modell'

min_confidence = 0.2

classes = []
classFile = 'coco.name.two'

with open(classFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')
print("Classes", classes)

net = cv2.dnn.readNetFromCaffe(modellnames, modell)
# readNetFromCaffe() reads a network model stored in Caffe framework's format.

image = cv2.imread(image_path)
height, width = image.shape[0], image.shape[1]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)
# blobFromImage() creates 4-dimensional blob from image. Optionally resizes and crops image from center, 
# subtract mean values, scales values by scalefactor, swap Blue and Red channels.

net.setInput(blob)
detected_objects = net.forward()

for i in range(detected_objects.shape[2]):
        
    confidence = detected_objects[0][0][i][1]

    if confidence > min_confidence:

        class_index = int(detected_objects[0, 0, i, 1])

        x1 = int(detected_objects[0, 0, i, 3] * width)
        y1 = int(detected_objects[0, 0, i, 4] * height)
        x2 = int(detected_objects[0, 0, i, 5] * width)
        y2 = int(detected_objects[0, 0, i, 6] * height)
        print(x1)
        prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
        cv2.rectangle(image, (x1, y1), 
                        (x2, y2), 
                        (255, 255, 255))
        cv2.putText(image, prediction_text, (x1, 
                        y1 - 10 if y1 > 30 else y1 + 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
                        (255, 255, 255), 2)
            
cv2.imshow('Output', image)    
cv2.waitKey(0)
cv2.destroyAllWindows()

