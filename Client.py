
import socket
import threading

diachi_server = ('localhost', 9050)

def send_data(sk, addr, data):
    data1 = data + '\0'
    sk.sendto(data1.encode('utf-8'), addr)

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

if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.connect(diachi_server)
    while True:
        # Gui 1
        data = input('Client:')
        send_data(sk, diachi_server, data)
        if data=='bye':
            break
        # Nhan 2
        data, addr = recv_data(sk)
        print('Server:', data)