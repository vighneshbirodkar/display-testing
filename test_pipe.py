from multiprocessing import Pipe
import socket

socket.setdefaulttimeout(120.0)


string = 'x'*800000
r,s = Pipe()
s.send(string)
print len(r.recv())
