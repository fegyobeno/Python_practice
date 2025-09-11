#A feladatot lehet python szrkript vagy jupiter notebook

#Importáld be a cv2 modult

#Olvasd be a coco.name.two class fájlt, és tárold el a benne található osztályokat egy listában

#A readNetFromCaffe() függvény segítségével olvasd be a modellneveket és a modellt

#Olvasd be a képet a cv2.imread() függvénnyel

#A kép magasságát és szélességét tárold el változókban

#A cv2.dnn.blobFromImage() függvény segítségével alakítsd át a képet blob formátumra

#Állítsd be a blob változót a hálózat bemenetének

#A hálózat forward() függvényével készítsd el a detektált objektumokat

#Végigiterálva a detektált objektumokon, ha a detektált objektum bizonyossága nagyobb, mint a min_confidence, akkor:
#- tárold el a detektált objektum osztályindexét
#- számold ki az objektum pozícióját az x1, y1, x2, y2 változókba
#- írd ki a detektált objektum osztályát és bizonyosságát a képre
#- rajzold ki a detektált objektumot a képre

#Végezetül jelenítsd meg a képet a cv2.imshow() függvénnyel, és várj a cv2.waitKey() függvénnyel a kilépésre