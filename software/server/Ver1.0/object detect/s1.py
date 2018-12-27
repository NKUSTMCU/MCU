import os
import cv2
#import Image
from  PIL  import Image


os.system("ls")
#os.system(" cd darknet")
os.chdir("/home/user/darknet")


#./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
os.system("./darknet detect cfg/yolov3.cfg yolov3.weights data/20181223_636812017286254328_P.jpg")

#show
im=Image.open("/home/user/darknet/predictions.jpg")
im.show()


