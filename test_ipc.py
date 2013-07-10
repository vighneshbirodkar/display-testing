from multiprocessing import Pipe,Process
from time import sleep
from sys import exit

dic = {'abc':'def'}
class Worker(Process):

    def __init__(self,conn):
        Process.__init__(self)
        self.connection = conn
        
    def run(self):
        while(True):
            dataThere = self.connection.poll(0.1)
            if(dataThere):
                print self.connection.recv()
                exit()
                
                
p1,c1 = Pipe()
w1 = Worker(c1)
p2,c2 = Pipe()
w2 = Worker(c2)
w1.start()
w2.start()
print "Processes started"
sleep(2)
print "Sending to 1"
p1.send(dic)
sleep(2)
print "Sending to 2"
p2.send(dic)
sleep(2)
exit()
