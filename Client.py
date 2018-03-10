from socket import * 
import sys

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

#def getport():
        #s = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
        #addr2 = ('127.0.0.1', 0)          # Socket address
        #s.bind(addr2)                    # Bind socket to address
        #addr2 , port = s.getsockname()
        #print(port)
        #return port

addr = ('127.0.0.1', 50000)
s = socket(AF_INET, SOCK_DGRAM)
s.connect(addr)

#port = getport()
#addre = ('127.0.0.1', port)
#s2 = socket(AF_INET, SOCK_DGRAM)
#s2.bind(addre)

#s.sendto(str(port).encode('utf-8'), addr)

print ('UDP server started ...')

while(1):
    subscribe = input('Enter your Subscribe : ')

    while(1):
        txtout = 'sub,'+subscribe+','+''+','+''
        s.sendto(txtout.encode('utf-8'), addr)  
        txtin , addre = s.recvfrom(MAX_BUF)
        txtin = txtin.decode('utf-8')
        print(subscribe+ '>' +txtin)
        print('sus')
        txtpayload , addre = s.recvfrom(MAX_BUF)
        txtpayload = txtpayload.decode('utf-8')

        if(txtpayload == 'cancel'):
            print('Unsubscriber ...')
            break
  
s.close()