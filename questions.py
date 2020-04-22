import random

class Question():
    name = "default"
    def __init__(self,*args,**kwargs):
        self.question, self.answer = self.create(*args,**kwargs)
    
    def create(self,*args,**kwargs):
        return "default_question", "default_answer"
    
    def check(self,answer):
        return answer == "default_answer"


class Add(Question):
    name = "ADD"
    def create(self,min_value,max_value):
        a = random.randint(min_value,max_value)
        b = random.randint(min_value,max_value)
        self.c = a+b

        return f"{a} {b}", f"{self.c}"
        
    def check(self,answer):
        try:
            return int(answer) == self.c
        except:
            return False


class Sum(Question):
    name = "SUM"
    def create(self,min_value,max_value,length):
        a = random.randint(min_value,max_value)
        b = random.randint(min_value,max_value)
        self.c = a+b

        return f"{a} {b}", f"{self.c}"
        
    def check(self,answer):
        try:
            return int(answer) == self.c
        except:
            return False
