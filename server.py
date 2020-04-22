#https://docs.python.org/2/library/socketserver.html

import time
import socket
import socketserver
import threading

from gameengine import GameEngine



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

            with ThreadedTCPServer((HOST,PORT),GameEngine) as server:
                server.serve_forever()

        except KeyboardInterrupt:
            break        
        except Exception as e:
            print(e)
            time.sleep(5)