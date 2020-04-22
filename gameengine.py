
class WrongAnswer(Exception):pass

from socketserver import StreamRequestHandler
import questions



class GameEngine(StreamRequestHandler):

    #handle is called from the init method in the base class
    def handle(self):
        try:
            begin_game(self)
        except WrongAnswer as e:
            self.print("\n\n\n\n\n")
            self.print("############ FAILED ############")
            self.print(str(e))
            self.print("\n\n")

    def print(self,text):
        text += "\n"
        text.replace("\n","\n\r")
        self.wfile.write(text.encode("utf-8"))

    def input(self,text):
        self.print(text)
        response = self.rfile.readline().strip().decode("utf-8")
        return response

    def ask(self,question_obj):
    
        question_text = f"?{question_obj.name}: {question_obj.question}"
        
        answer = self.input(question_text)
        
        correct = question_obj.check(answer)

        if not correct:

            raise WrongAnswer( 
f"""For the question:
{question_text}
You answered:
{answer}
"The correct answer is:"
{question_obj.answer}"""
            )


def begin_game(g):

    g.print("\n"*50)
    ans = g.input("Are you a Robot (yes/no)?")
    if ans != "yes":
        raise WrongAnswer("The answer should be yes. Only robots are allowed")

    g.print("I'm not convinced.")

    ans = g.input("Say something a Robot would say.")

    if not( "1" in ans and "0" in ans):
        raise WrongAnswer("Robots say stuff like 1010101010")

    g.print("Well since you are a Robot you should have no trouble answers these questions")
    g.print("Here's how its going to work.")

    g.ask(questions.Add(0,10) )
    g.print("Not bad. How about some harder ones.")
    
    for i in range(2):
        g.ask(questions.Add(-99999,99999) )