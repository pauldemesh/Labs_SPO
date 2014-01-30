import socket
import os

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print 'Connected by', addr
filepath = '/home/paul/12'
fileToSend = open(filepath, 'rb')
while True:
  data = fileToSend.readline(1024)
  if data:
    conn.send(data)
  else:
    break

conn.close()  

