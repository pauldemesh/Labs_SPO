 
import socket
import threading
HOST = ''                
PORT = 50007 

class Connect(threading.Thread):
  def __init__(self, sock, addr):
    self.sock = sock
    self.addr = addr
    print 'Connected by', addr
    threading.Thread.__init__(self)
  def run (self):
    while True:
      data = self.sock.recv(1024)
      if not data:break
      self.sock.send(data)
    self.sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

while True:
  sock, addr = s.accept()
  Connect(sock, addr).start()