import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("172.105.178.196",1337))
s.connect(("127.0.0.1",1337))
f = s.makefile("rw")
f.write("start\n")
f.write("tom\n")


while True:
    f.flush()
    line = f.readline()
    if len(line) == 0:
        break
    
    print(line,end='')
    line = line.strip()
    

    if len(line) <= 0:
        continue

    if line[0] == "?":
        i = line.find(":")
        question_type = line[1:i]
        line = line[i+1:].strip()
        response = "Durp"


        if question_type == "ADD":
            a,b = line.split(" ")
            c = int(a) + int(b)
            response = str(c)

        elif question_type == "SUM":
            c = sum([int(v) for v in line.split(" ")])
            response = str(c)

        elif question_type == "SORT":
            sorted_list = sorted([int(v) for v in line.split(" ")])
            response = " ".join([str(v) for v in sorted_list])

        elif question_type == "BINARY":
            v = int(line,2)
            response = str(v)
        else:
            response = input()
        print(response,end='')  
        f.write(response+"\n")
        
  

        


        

        
    