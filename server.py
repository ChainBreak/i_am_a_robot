#https://docs.python.org/2/library/socketserver.html

import time
import socket
import socketserver
import threading


def game_entry():
    yield "\r\n\r\nHello \r\n$Are you a robot (yes/no)?"


def client_handler(client_socket,client_address,server):
    client_socket.settimeout(30.0)
    try:
        f = client_socket.makefile("rw")
        
        generator = game_entry()
        f.write(generator.send(None) )
        f.flush()
        while True:
            line = f.readline().strip()
            f.write(line.upper() + " "+threading.current_thread().name+"\n")
            f.flush()
    except Exception as e:
        print(e)
        


#This is the socketserver funky way of joining threading with a tcp server
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True
    

if __name__ == "__main__":

    HOST, PORT = "0.0.0.0", 1337

    #lets do this forever mate
    while True:
        #catch any shit and just keep trying
        try:

            with ThreadedTCPServer((HOST,PORT),client_handler) as server:
                server.serve_forever()

        except KeyboardInterrupt:
            break        
        except Exception as e:
            print(e)
            time.sleep(5)