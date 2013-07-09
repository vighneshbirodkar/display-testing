from GtkDisp import *


from time import sleep


if ( __name__ == '__main__'):
    from SimpleCV import Image,Camera
    i = Image('lenna')
    c = 0
    disp1 = GtkDisplay()
    img1 = Image('lenna')
    disp2 = GtkDisplay()
    img2 = Image('logo')
    while(True):
        c = (c+1)%100
        d = c*5/100.0 + 1
        disp1.showImg(img1/d)
        disp2.showImg(img2/d)
