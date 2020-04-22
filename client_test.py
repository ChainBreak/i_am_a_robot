import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1",1337))
f = s.makefile("rw")
f.write("yes\n")
f.write("101010\n")


while True:
    f.flush()
    line = f.readline()
    if len(line) == 0:
        break

    line = line.strip()
    print(line)

    if "?ADD:" in line:
        a,b = line[5:].strip().split(" ")
        c = int(a) + int(b)
        response = str(c)+"\n"
    
        f.write(response)

    time.sleep(0.1)
        


        

        
    