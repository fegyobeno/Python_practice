import numpy as np
import cv2

# pip install opencv-python

#image_path = 'people1.jpg'

modellnames = 'objectdataset.data' 
modell = 'pretrained.modell'

min_confidence = 0.2

classes = []
#classFile = 'coco.name.two'
#with open(classFile, 'rt') as f:
#    classes = f.read().rstrip('\n').split('\n')
#print("Classes", classes)

classes =  ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", 
            "bus", "car", "cat", "chair", "cow", 
           "diningtable",  "dog", "horse", "motorbike", "person", 
           "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
                      
np.random.seed(543210)
colors = np.random.uniform(0, 255, size = (len(classes), 3))

net = cv2.dnn.readNetFromCaffe(modellnames, modell)

#image = cv2.imread(image_path)

cap = cv2.VideoCapture(0)

while True:

    _, image = cap.read()

    height, width = image.shape[0], image.shape[1]
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007, (300, 300), 130)

    net.setInput(blob)
    detected_objects = net.forward()
    #print(detected_objects[0][0][1])

    for i in range(detected_objects.shape[2]):
        
        confidence = detected_objects[0][0][i][2]

        if confidence > min_confidence:

            class_index = int(detected_objects[0, 0, i, 1])

            x1 = int(detected_objects[0, 0, i, 3] * width)
            y1 = int(detected_objects[0, 0, i, 4] * height)
            x2 = int(detected_objects[0, 0, i, 5] * width)
            y2 = int(detected_objects[0, 0, i, 6] * height)

            prediction_text = f"{classes[class_index]}: {confidence:.2f}%"
            cv2.rectangle(image, (x1, y1), 
                        (x2, y2), 
                        colors[class_index])
            cv2.putText(image, prediction_text, (x1, 
                        y1 - 15 if y1 > 30 else y1 + 15), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, 
                        colors[class_index], 2)
            
    cv2.imshow('Output', image)
    if cv2.waitKey(1) == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()

