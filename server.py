import socket
import sys

#create socket(to connect two computers)
def create_socket():
    try:
        global host
        global port 
        global sock

        host = ""
        port = 9998
        sock = socket.socket()
    except socket.error as msg:
        print("Socket creation error:" + str(msg))

#binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port 
        global sock

        print("Binding the socket with port: " + str(port))

        sock.bind((host,port))
        sock.listen(5)

    except socket.error as msg:
        print("Binding the socket error:" + str(msg) + "\n" + "Retrying....")
        bind_socket()

def socket_accept():
    conn, address = sock.accept()
    print("Connection Established!!" + "IP:" + address[0] + "Port:" + str(address[1]))
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            sock.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(9999), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()