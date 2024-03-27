import time

from sockets import Socket

# Send
def sender_loop_exapmle(port_send_to, port_send_from=None):
    channel = ("127.0.0.1", port_send_to)
    my_sock = Socket(channel, big_buffer=False)
    if port_send_from is not None:
        my_sock.send_from_port(port_send_from)

    counter = 0
    try:
        while True:
            print(f"sending {counter}")
            my_sock.send_json({"counter":counter})
            counter += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Exit")

# Receive
def receiver_loop_example(port_listen_to):
    channel = ("127.0.0.1", port_listen_to)
    my_sock = Socket(channel, big_buffer=False)
    my_sock.bind_receive()

    # Receive loop
    to_listen = True
    try:
        while to_listen:
            data = my_sock.blocking_recv()
            print(data)
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Exit")

if __name__ == "__main__":    
    import threading
    from_port = 5670
    to_port = 5671
    threading.Thread(target=receiver_loop_example, args=(to_port,), daemon=True).start()
    
    sender_loop_exapmle(port_send_to=to_port, port_send_from=from_port)