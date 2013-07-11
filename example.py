import socket
print socket.getdefaulttimeout()


from GtkDisp import *

import socket
socket.setdefaulttimeout(None)
from time import sleep



if ( __name__ == '__main__'):
    from SimpleCV import Image,Camera

    cam = Camera()

    disp1 = GtkDisplay()
    disp2 = GtkDisplay()

    while(True):
        img = cam.getImage()
        disp1.showImg(img)
        print "Timeout = ",socket.getdefaulttimeout()
        disp2.showImg(img.invert())
