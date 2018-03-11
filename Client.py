# Group Network need some Carry
#       58070501006 Karntawan   Udomluksopin
#       58070501046 Peerakit    Boonkittiporn
#       58070501054 Methawat    Thanapairin
#       58070501069 Sirapong    Phoosawan
 
from socket import * 
import sys

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

addr = ('127.0.0.1', 50000)
s = socket(AF_INET, SOCK_DGRAM)
s.connect(addr) #Socket Connected to Server

print ('----- Subscriber is started -----')

while(1):
    subscribe = input('\tEnter your Subscribe Topic > ') #Enter Subscribe topic

    while(1):
        txtin = ''  #Clear Data in txtin Variable
        txtout = 'sub,'+subscribe+','+''+','+'' #Pattern Data for send to server
        s.sendto(txtout.encode('utf-8'), addr)  #Convert to byte type and send to server
        txtin , addre = s.recvfrom(MAX_BUF) #Received Data from server
        txtin = txtin.decode('utf-8') #Decode Data 
        print('\t-> Message from '+subscribe+ ' > ' +txtin+'\n') #print data from server
        txtin = '' #Reset data from server is null
        break #Stop subscriber

s.close()