from multiprocessing import Process,Pipe
from time import sleep

from SimpleCV import Image,Camera



class GtkWorker(Process):
    def __init__(self,connection):
        Process.__init__(self)
        self.connection = connection

    def run(self):
        import gtk
        import gobject
        
        self.gtk = gtk
        self.gobject = gobject
        
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.image = gtk.Image()
        
        self.window.add(self.image)
        self.window.show_all()

        gobject.io_add_watch(self.connection.fileno(),gobject.IO_IN,self.checkMsg)
        gtk.main()
        
    def destroy(self,widget,data=None):
        self.gtk.main_quit()
    
    def showImg(self,data):


        pix =  self.gtk.gdk.pixbuf_new_from_data(data['data'], self.gtk.gdk.COLORSPACE_RGB, False, data['depth'], data['width'], data['height'], data['width']*3)
        self.image.set_from_pixbuf(pix)
    
    def checkMsg(self,source=None,condition=None):

        msg = self.connection.recv()
        
        
        if(msg['func'] == 'display'):
            self.showImg(msg)
        elif (msg['func'] == 'close'):
            print 'quitting'
            gtk.main_quit()
        else:
            print 'unknown message'
        return True
        
class GtkDisplay:
    def __init__(self):
        parentConn,childConn = Pipe()
        self.connection = parentConn
        self.worker = GtkWorker(childConn)
        self.worker.start()
        
    def showImg(self,img):
        dic = {}
        dic['data'] = img.toString()
        dic['depth'] = img.depth
        dic['width'] = img.width
        dic['height'] = img.height
        dic['func'] = 'display'
        self.connection.send(dic)
   





