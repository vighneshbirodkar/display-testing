from GtkDisp import *
from SimpleCV import Camera

disp1 = GtkDisplay()
disp2 = GtkDisplay()
cam = Camera()

while(True):
    disp1.showImg(cam.getImage())
    disp2.showImg(cam.getImage())

