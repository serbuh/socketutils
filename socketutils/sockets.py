import socket
import json

class Socket():
    def __init__(self, channel, big_buffer=False, reuse_addr=False):
        self.channel = channel
        self.recv_buf_size = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if big_buffer:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF,2**23)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF,2**23)
        if reuse_addr:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Send commands
    def send_serialized(self, msg_serialized):
        self.sock.sendto(msg_serialized, self.channel)
    
    def send_json(self, msg):
        msg_serialized = str.encode(json.dumps(msg))
        self.sock.sendto(msg_serialized, self.channel)
    
    def send_from_port(self, send_from_port):
        '''Set sending port'''
        self.sock.bind(('0.0.0.0', send_from_port))

    # Receive commands
    def bind_receive(self, recv_buf_size=65535):
        self.sock.bind(self.channel)
        self.recv_buf_size = recv_buf_size

    def blocking_recv(self):
        data, _ = self.sock.recvfrom(self.recv_buf_size) # Blocking. Should be in thread
        return data
