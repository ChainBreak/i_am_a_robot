from gameengine import WrongAnswer
import questions
def begin(g):
    #clear the terminal
    g.print("\n"*50)

    ### INTRO ###

    g.print("""
+-------- MILTECH RECRUITMENT SERVICES ---------+
|                                               |
| POSITION:                                     |
| Computer programmer for military navigational |
| and targeting systems.                        |
|                                               |
| SELECTION CRITERIA:                           |
| Must be an American citizen who is willing    |
| to live on base. Must past the testing below. |
|                                               |
| version: 1.2.63    date: 03/07/1978           |
+-----------------------------------------------+
""")

    g.print("You will be given a long series of challenges.")
    g.print("It is expected that only a computer programmer\ncould solve them.\n")

    while True:
        ans = g.input("Please type 'start' or 'help':")

        if ans == "start":
            break
        if ans == "help":
            g.print("\n")
            g.print("+------------------- HELP ----------------------+")
            g.print("|-Questions begin with '?'.")
            g.print("| |-This is the question type.")
            g.print("| |    |-These are the question arguments.")
            g.print("||-|  |-|")
            g.print("?ADD: 1 2")
            g.print("You must give a single line answer to every queston.")
            g.print("eg. '3\\n' (don't forget the new line)")
            g.print("\n")

    g.print("\n")
    g.print("+---------------- TEST STARTED -----------------+")
    while True:
        name = g.input("Please enter your unique call sign:")

        if len(name) == 0 or len(name) >20:
            g.print("your call sign must be between 0-20 characters.")
            continue

        break

    g.print("\n")
    g.print( "+-------------- RECORD UPDATED -----------------+")
    g.print(f"| NAME: {name:20}                    |")
    g.print( "+-----------------------------------------------+")

    ### ADDITION ###
    g.print("\nAdd two numbers together.")
    g.ask(questions.Add(0,10) )
    g.print("That is correct. Try some harder ones.")
    for i in range(5):
        g.ask(questions.Add(-10,10) )

    ### SUM ###
    g.print("\nCalculate the sum of these integers.")
    g.ask(questions.Sum(0,5,3) )
    g.ask(questions.Sum(0,10,10) )
    for i in range(5):
        g.ask(questions.Sum(-10,10,10) )

    ### SORT ###
    g.print("\nSort these lists in increasing order.")
    g.ask(questions.Sort(0,5,3) )
    for i in range(20):
        g.ask(questions.Sort(-100,100,10) )


    ### BINARY ###
    g.print("\nConvert these binary numbers into integers.")
    g.ask(questions.Binary(2,8) )
    g.ask(questions.Binary(0,16) )
    for i in range(4,32):
        g.ask(questions.Binary(0,2**i) )


    
    g.print("+---------------- TEST COMPLETE ----------------+")
    g.print(f"|   NAME: {name:20}                  |")
    g.print("| STATUS: successful                            |")
    g.print("|                                               |")
    g.print("| Don't contact us. We will contact you.        |")
    g.print("+-----------------------------------------------+")
    

