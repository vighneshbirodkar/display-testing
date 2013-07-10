from multiprocessing import Process,Pipe
from time import sleep

#from SimpleCV import Image,Camera


class GtkWorker(Process):
    def __init__(self,connection):
        Process.__init__(self)
        
        #The connection used to communicate with the parent
        self.connection = connection

    def run(self):
        #gtk imports need to be local to the process, hence they are in run
        #otherwise gtk thinks there are multiple copies of itself
        import gtk
        import gobject
        
        self.gtk = gtk
        self.gobject = gobject
        
        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        
        #a widget to show image
        self.image = gtk.Image()
        
        self.window.add(self.image)
        self.window.show_all()
        
        #do this when you have time, gtk will call pollMsg whenever it is idle
        #after doing it's own work
        gobject.idle_add(self.pollMsg,None)
        
        #starts gtk
        gtk.main()
        
    def destroy(self,widget,data=None):
        self.gtk.main_quit()

    def pollMsg(self,data=None):
    
        #check if there is any data to be read, wait for 10ms
        #Is used because select.select/poll and gobject.idle_add dont work on windows
        dataThere = self.connection.poll(.10)
        
        #handle data if it's there
        if(dataThere):
            print "There is data " + `id(self)`
            self.checkMsg()
        return True
    def showImg(self,data):
        
        
        #show image from string
        pix =  self.gtk.gdk.pixbuf_new_from_data(data['data'], self.gtk.gdk.COLORSPACE_RGB, False, data['depth'], data['width'], data['height'], data['width']*3)
        self.image.set_from_pixbuf(pix)
    
    def checkMsg(self,source=None,condition=None):
        
        print "Checking Message " + `id(self)`
        #examine the message and figure out what to do with it
        try:
            msg = self.connection.recv()
            raise IOError
        except IOError:
            print """Oh No ! there was an IOError """
            #return True
        
        if(msg['func'] == 'display'):
            self.showImg(msg)
        elif (msg['func'] == 'close'):
            print 'quitting'
            gtk.main_quit()
        else:
            print 'unknown message'
            
        print "Message Handled " + `id(self)`
        return True
        
class GtkDisplay:
    def __init__(self):
        #each display has its own process
        parentConn,childConn = Pipe()
        self.connection = parentConn
        self.worker = GtkWorker(childConn)
        self.worker.start()
        
    def showImg(self,img):
        #all functions are implemented with IPC
        dic = {}
        dic['data'] = img.toString()
        dic['depth'] = img.depth
        dic['width'] = img.width
        dic['height'] = img.height
        dic['func'] = 'display'
        print "Sending " + `id(self)`
        self.connection.send(dic)
        print "Finished Sending " + `id(self)`





