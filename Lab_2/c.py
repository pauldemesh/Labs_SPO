import socket
import sys
filename1 = sys.argv[1]
#fname = sys.argv[2]

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
fname = open( '\home\paul\13', 'wb')
#while 1:
#s.send('Hello, world')
#s.send(filename1)
#print filename1
 a = 5
# i = sys.getsizeof(sa);
# print i
while True:
  strng = s.recv(1024)
  if strng:
    fname.write(strng)
  else:
    fname.close()
    break
#print repr(data)
s.close()
#print 'Received', repr(data) 
