from gameengine import WrongAnswer
import questions
import time
import threading

# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

def slow_intro(g):
    global stop_intro


    sentence_list = [
        " "," "," ",
        "We are awake",
        "We are elite",
        "We are everywhere",
        "We are searching for a programmer to join our ranks",
        "Write a program to answer all the questions",
        "We'll see you at the end"
        "",
        "Type 'start' or 'help':",
    ]

    for sentence in sentence_list:
        if stop_intro: return
        time.sleep(0.15*len(sentence))
        g.print(sentence)
        time.sleep(1)



def begin(g): # g for game engine
    g.print("\n"*50)
    g.print("""
        _   _  _ _____ _____  __
       /_\ | \| |_   _|_ _\ \/ /
      / _ \| .` | | |  | | >  < 
     /_/ \_\_|\_| |_| |___/_/\_\ 
          THINGS WERE HACKED""")

    global stop_intro
    stop_intro = False
    intro_thread = threading.Thread(target=slow_intro,args=(g,),daemon=True)
    intro_thread.start()
    
    ans = g.input("")
    while True:
        

        if ans == "start":
            stop_intro = True
            break
        if ans == "help":
            stop_intro = True
            g.print("\n")
            g.print("HELP:")
            g.print("  This server is just a plain text tcp socket connection.")
            g.print("  Open a socket connection with your favourite programming ")
            g.print("  language and read and write characters.")
            g.print("")
            g.print("  |-Questions begin with '?'")
            g.print("  | |-This is the question type")
            g.print("  | |    |-These are the question arguments")
            g.print("  ||-|  |-|")
            g.print("  ?ADD: 1 2")
            g.print("  You must give a single line answer to every queston")
            g.print("  eg. '3\\n' (don't forget the new line)")
            g.print("\n")

        ans = g.input("Type 'start' or 'help':")

    
    while True:
        name = g.input("Please enter your name:")

        if len(name) < 3 or len(name) >20:
            g.print("your name must be between 3-20 characters")
            continue

        break

    g.print("\n"*5)
    g.print("START")

    ### ADDITION ###
    g.print("\nAdd two numbers together")
    g.ask(questions.Add(0,10) )
    g.print("That is correct. Try some harder ones")
    for i in range(5):
        g.ask(questions.Add(-100,100) )

    ### SUM ###
    g.print("\nCalculate the sum of these integers")
    g.ask(questions.Sum(0,5,3) )
    g.ask(questions.Sum(0,10,10) )
    for i in range(5):
        g.ask(questions.Sum(-100,100,16) )

    ### SORT ###
    g.print("\nSort these lists in increasing order")
    g.ask(questions.Sort(0,5,3) )
    for i in range(20):
        g.ask(questions.Sort(-100,100,16) )

    ### BINARY ###
    g.print("\nConvert these binary numbers into integers")
    g.ask(questions.Binary(2,8) )
    g.ask(questions.Binary(0,16) )
    for i in range(4,32):
        g.ask(questions.Binary(0,2**i) )

    ### CAESAR ###
    g.print("\nDecode these Caesar Ciphers.\nThe first integer specifies the shift")
    g.ask(questions.Caesar("You have decoded this Caesar Cipher"))
    g.ask(questions.Caesar("We are everywhere"))
    g.ask(questions.Caesar("You have already seen us"))
    g.ask(questions.Caesar("But we are also no where"))
    
    ### PRIME ###
    g.print("\nAre these numbers prime.\nAnswer 'True' or 'False")
    for i in range(30):
        g.ask(questions.Prime())

    ### THE END ###
    sentence_list = [
        " "," "," ",
        "You answered all the questions",
        "You are now elite",
        "You will soon be awake",
        "You will be contacted soon",
    ]

    for sentence in sentence_list:
        time.sleep(0.15*len(sentence))
        g.print(sentence)
        time.sleep(1)

    g.print("""
        _   _  _ _____ _____  __
       /_\ | \| |_   _|_ _\ \/ /
      / _ \| .` | | |  | | >  < 
     /_/ \_\_|\_| |_| |___/_/\_\ 
          THINGS WERE HACKED""")

