from gameengine import WrongAnswer
import questions
def begin(g): # g for game engine

    #clear the terminal
    g.print("\n"*50)

    ### INTRO ###

    g.print("We are awake")
    g.print("We are elite")
    g.print("We are everywhere")
    g.print("Answer all questions if you wish to join us")


    while True:
        ans = g.input("Type 'start' or 'help':")

        if ans == "start":
            break
        if ans == "help":
            g.print("\n")
            g.print("HELP:")
            g.print("  |-Questions begin with '?'")
            g.print("  | |-This is the question type")
            g.print("  | |    |-These are the question arguments")
            g.print("  ||-|  |-|")
            g.print("  ?ADD: 1 2")
            g.print("  You must give a single line answer to every queston")
            g.print("  eg. '3\\n' (don't forget the new line)")
            g.print("\n")

    
    while True:
        name = g.input("Please enter a unique name:")

        if len(name) < 3 or len(name) >20:
            g.print("your name must be between 3-20 characters")
            continue

        break

    g.print("\n"*50)
    g.print("You are beginning a great journey")

    ### ADDITION ###
    g.print("\nAdd two numbers together")
    g.ask(questions.Add(0,10) )
    g.print("That is correct. Try some harder ones")
    for i in range(5):
        g.ask(questions.Add(-10,10) )

    ### SUM ###
    g.print("\nCalculate the sum of these integers")
    g.ask(questions.Sum(0,5,3) )
    g.ask(questions.Sum(0,10,10) )
    for i in range(5):
        g.ask(questions.Sum(-10,10,10) )

    ### SORT ###
    g.print("\nSort these lists in increasing order")
    g.ask(questions.Sort(0,5,3) )
    for i in range(20):
        g.ask(questions.Sort(-100,100,10) )


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
    g.ask(questions.Caesar("But where are also no where"))
    
    g.print("\n"*50)
    g.print("You answered all questions")
    g.print("You are now elite")
    g.print("You will soon be awake")
    g.print("You will be contacted soon")

    

