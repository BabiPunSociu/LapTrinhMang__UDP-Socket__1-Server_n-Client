
import socket
import threading
from time import sleep

diachi_server = ('localhost', 9050)
lstClient = []

def send_data(sk, addr, data):
    data1 = data + '\0'
    sk.sendto(str.encode(data1), addr)

def recv_data(sk):# return (msg, addr)
    data = bytearray()
    msg = ''
    while not msg:
        data1, addr = sk.recvfrom(1024)
        if not data1:
            raise ConnectionError()
        data = data + data1
        if b'\0' in data1:
            data = data.rstrip(b'\0')
            msg = data.decode('utf-8')
            return (msg, addr)

def thread_client(sk):
    while True:
        # Nhan 1:
        data, addr = recv_data(sk)
        print('Client {}:{}'.format(addr, data))
        if addr not in lstClient:
            lstClient.append(addr)
        if data=='bye':
            break
        # gui 2:
        #=======================================
        # neu gui lai cho dia chi addr:
        data = input('server send to client {}:'.format(addr)).strip()
        send_data(sk, addr, data)
        #=======================================
        # neu gui cho tat ca cac may trong lstClient:
        # for address in lstClient:
        #     send_data(sk, addr, data)

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.bind(diachi_server)
    print('Server san sang ...')
    
    thread = threading.Thread(target=(thread_client), args=[sk],daemon=1)
    thread.start()
    while True:
        sleep(1)