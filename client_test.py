import time
import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(("172.105.178.196",1337))
s.connect(("127.0.0.1",1337))
f = s.makefile("rw")
f.write("start\n")
f.write("tom\n")


def caesar_map(c,shift):
    a = ord("a")
    z = ord("z")
    A = ord("A")
    Z = ord("Z")

    c = ord(c)
    if c >=a and c <= z:
        c = ((c - a - shift) % 26) + a
    if c >=A and c <= Z:
        c = ((c - A - shift) % 26) + A
    
    return chr(c)

while True:
    f.flush()
    line = f.readline()
    if len(line) == 0:
        break
    
    print(line,end="") #,ord(line[0]),ord(line[-1])
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

        elif question_type == "CAESAR":
            i = line.find(" ")
            shift = int(line[:i])
            cipher_text = line[i:].strip()
            response = "".join([caesar_map(c,shift) for c in cipher_text])

        elif question_type == "PRIME":
            response = "True"
            n = int(line)
            for i in range(3,n//2+1):
                if n % i == 0:
                    response = "False"
                    break

        else:
            response = input()
        print(response)  
        f.write(response+"\n")
        
  

        


        

        
    