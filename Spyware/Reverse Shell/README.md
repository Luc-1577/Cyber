# Reverse Shell

This repository includes two Python scripts facilitating remote command execution using socket communication.

## server.py

The `server.py` script acts as the server, waiting for incoming connections from clients. Upon connection, it sends commands to the target.

### Usage

1. Set up the server IP address (`LHOST`) and port (`PORT`) accordingly.
2. Run the `server.py` script on the server side.
3. Upon connection from a target, the server will prompt for commands to execute.

## reverse_shell.py

The `reverse_shell.py` script serves as the client, connecting to the server and accepting commands from the server and sendind back the output to the server.

### Usage

1. Ensure the `LHOST` and `PORT` variables in the `reverse_shell.py` script match the server's IP address and port.
2. Run the `reverse_shell.py` script on the target machine.
