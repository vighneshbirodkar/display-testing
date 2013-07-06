from GtkDisp import *
from SimpleCV import Camera

disp = GtkDisplay()
cam = Camera()

while(True):
    disp.showImg(cam.getImage())

