from multiprocessing import Pipe,Process
from time import sleep
from sys import exit
import socket

#comment this to make it work in older versions
socket.setdefaulttimeout(120.0)

string = 'x'*800000
class Worker(Process):

    def __init__(self,conn):
        Process.__init__(self)
        self.connection = conn
        
    def run(self):
        while(True):
            dataThere = self.connection.poll(0.1)
            if(dataThere):
                print len(self.connection.recv())
                exit()
                
                
p1,c1 = Pipe()
w1 = Worker(c1)
w1.start()
print "Processes started"
sleep(2)
print "Sending to 1"
p1.send(string)
sleep(2)
exit()
