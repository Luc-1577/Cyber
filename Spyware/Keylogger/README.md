# Keylogger

This repository contains two Python scripts related to a simple keylogger and socket communication. Below is a brief description of each script:

## keylogger.py

This script logs the keys pressed by the user and sends them via a socket connection to a remote server. It uses the `pynput` library to monitor and log the keys pressed. The logged keys are saved in a file named `keylog.txt`.

## server.py

This script acts as a server that accepts connections from clients and receives the data sent by the keylogger. It creates a socket connection and waits for client connections. Once a connection is established, the server receives the data and saves it to a file.

### Requirements

- Python 3.x
- Libraries: `pynput` (for `keylogger.py`)

### Usage

Before running the scripts, make sure to set up the correct IP address and port to establish communication between the keylogger and the server.

Run `server.py` on the server to wait for client connections.

Then, run `keylogger.py` on a client to start the keylogger and send the data to the server.
