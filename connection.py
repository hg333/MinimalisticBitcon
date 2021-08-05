
from message import message
import struct
import time
import random
import hashlib
import socket
import os

version = struct.pack("i", 70002)
services = struct.pack("Q", 0)
timestamp = struct.pack("q", int(time.time()))

addr_recv_services = struct.pack("Q", 0) #services
addr_recv_ip = struct.pack(">16s", "127.0.0.1".encode("utf-8"))
addr_recv_port = struct.pack(">H", 8333)

addr_trans_services = struct.pack("Q", 0) #services
addr_trans_ip = struct.pack(">16s", "127.0.0.1".encode("utf-8"))
addr_trans_port = struct.pack(">H", 8333)

nonce = struct.pack("Q", random.getrandbits(64))
user_agent_bytes = struct.pack("B", 0)
starting_height = struct.pack("i", 0)
relay = struct.pack("?", False)

payload = version + services + timestamp + addr_recv_services + addr_recv_ip + addr_recv_port + addr_trans_services + addr_trans_ip + addr_trans_port + nonce + user_agent_bytes + starting_height + relay

magic = bytes.fromhex("F9BEB4D9")
command = bytes.fromhex("version".encode("utf-8").hex() + 5 * ("00"))
length = struct.pack("I", len(payload))

check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]

msg = magic + command + length + check + payload

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HOST = "45.95.64.55"
HOST = "24.64.72.174"
PORT = 8333

s.connect((HOST, PORT))

s.send(msg)
# print(msg)


def verackMessage():
    payload=''.encode('utf-8')
    magic = bytes.fromhex("F9BEB4D9")
    command = bytes.fromhex("verack".encode("utf-8").hex() + 6 * ("00"))
    length = struct.pack("I", len(payload))
    check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return (magic+command+length+check)
def pongMessage(k):
    payload=struct.pack('<Q',k)
    magic = bytes.fromhex("F9BEB4D9")
    command = bytes.fromhex("pong".encode("utf-8").hex() + 8 * ("00"))
    length = struct.pack("I", len(payload))
    check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return (magic+command+length+check+payload)


def pingMessage():
    k=8858864724027774750
    payload=struct.pack('<Q',k)
    magic = bytes.fromhex("F9BEB4D9")
    command = bytes.fromhex("ping".encode("utf-8").hex() + 8 * ("00"))
    length = struct.pack("I", len(payload))
    check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return (magic+command+length+check+payload)

k=1
while True:
    d = s.recv(1024)
    mg=d.hex()
 
    k+=1
    if(k==3):
        res = pingMessage()
        print("\n\nSENDING ", message(res.hex()),"\n\n")
        s.send(res)
    while(len(mg)>0):
        temp= message(mg)
        mg = temp.rem()
        print(temp)
        print("#################################",k)

        if(temp.command.startswith("version")):
            res = verackMessage()
            print("\n\nSENDING",message(res.hex()),"\n\n")
            s.send(res)
        elif(temp.command.startswith("ping")):
            res = pongMessage(temp.payload.nonce)
            print("\n\nSENDING ", message(res.hex()),"\n\n")
            s.send(res)
        elif(temp.command.startswith("pong")):
            print("OKOKOKOKOKOK")
