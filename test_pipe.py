from multiprocessing import Pipe

dic = {'abc':'def'}
p,q = Pipe()
p.send(dic)
print q.recv()
q.send(dic)
print p.recv()
