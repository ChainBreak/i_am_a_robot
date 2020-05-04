
class WrongAnswer(Exception):pass

from socketserver import StreamRequestHandler
import gamestory



class GameEngine(StreamRequestHandler):

    #handle is called from the init method in the base class
    def handle(self):
        try:
            gamestory.begin(self)
        except WrongAnswer as e:
            self.print("\n\n")
            self.print("+--------------- TEST TERMINATED ---------------+")
            self.print(str(e))
            self.print("\n\n")
            self.print("+------------------ THANK YOU ------------------+")
            self.print("Thank you for your application.\nPlease try again.\n\n")

    def print(self,text):
        text += "\n"
        text = text.replace("\n","\n\r")
        self.wfile.write(text.encode("utf-8"))

    def input(self,text):
        self.print(text)
        response = self.rfile.readline().strip().decode("utf-8")
        return response

    def ask(self,question_obj):
    
        question_text = f"?{question_obj.name}: {question_obj.question}"
        
        answer = self.input(question_text)
        self.print("")
        correct = question_obj.try_check(answer)

        if not correct:

            raise WrongAnswer( 
f"""For the question:
{question_obj.name}: {question_obj.question}
You answered:
{answer}
The correct answer is:
{question_obj.answer}"""
            )


