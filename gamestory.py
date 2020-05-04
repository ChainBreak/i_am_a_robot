from gameengine import WrongAnswer
import questions
def begin(g):
    #clear the terminal
    g.print("\n"*50)

    ### INTRO ###
    g.print("We have been seeking.")
    ans = g.input("Are you worthy?")
    if ans != "yes":
        raise WrongAnswer("The worthy would answer 'yes'")

    ans = g.input("What do you know?")
    if ans != "everything":
        raise WrongAnswer("You should know 'everything'")  

    g.print("You are on a journey.")
    g.print("A technical and spiritual journey.")
    g.print("You will be tested.")
    g.print("Only the elite will pass.")

    g.print("\nLets begin.")
    g.print("# |-Questions begin with '?'.")
    g.print("# | |-This is the question type.")
    g.print("# | |    |-These are the question arguments.")
    g.print("# ||-|  |-|")
    g.print("# ?ADD: 1 2")
    g.print("You must give a single line answer to every queston.")
    g.print("eg. '3\\n' (don't forget the new line)")

    ### ADDITION ###
    g.print("\nLets start off by adding two numbers together. Try:")
    g.ask(questions.Add(0,10) )
    g.print("Not bad. How about some harder ones.")
    
    for i in range(5):
        g.ask(questions.Add(-10,10) )

    ### SUM ###
    g.print("\nCalculate the sum of these integers.")
    g.ask(questions.Sum(0,5,3) )
    g.ask(questions.Sum(0,10,10) )
    g.print("Not bad. How about some harder ones.")
    for i in range(5):
        g.ask(questions.Sum(-10,10,10) )

    ### SORT ###
    g.print("\nLets try sorting some lists.")
    g.ask(questions.Sort(0,5,3) )
    for i in range(20):
        g.ask(questions.Sort(-100,100,10) )

    g.print("\n\nWait for further instructions")

