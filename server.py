#https://docs.python.org/2/library/socketserver.html

import time
import socket
import socketserver
import threading


def client_handler(client_socket,client_address,server):
    
    while True:
        # self.request is the TCP socket connected to the client
        data = client_socket.recv(1024).strip()
        if len(data) > 0:
            print("{} wrote:".format(client_address[0]))
            print(data)
            # just send back the same data, but upper-cased
            client_socket.sendall(data.upper() + bytes(" "+threading.current_thread().name,"utf-8" ))
        else:
            break


#This is the socketserver funky way of joining threading with a tcp server
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":

    HOST, PORT = "0.0.0.0", 1337

    #lets do this forever mate
    while True:
        #catch any shit and just keep trying
        try:
            # Create the server object
            server = ThreadedTCPServer((HOST, PORT), client_handler)
      
            try:
                #start listening for clients. A new thread is spawned for each client
                server.serve_forever()
            except KeyboardInterrupt:
                break
            finally:
                server.shutdown()
                server.server_close()

        except KeyboardInterrupt:
            break        
        except Exception as e:
            print(e)
            time.sleep(5)