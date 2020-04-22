import random

class Question():
    """This is a base class and is ment to be inherited"""
    name = "default"
    def __init__(self,*args,**kwargs):
        self.question, self.answer = self.create(*args,**kwargs)
    
    def create(self,*args,**kwargs):
        """Each question must implement a create method.
        The create method must return a tuple of a 
        question string and an answer string.
        eg ('1+2','3')
        
        The question and answer string can be accessed via 
        self.question and self.answer
        """
        raise NotImplementedError("Each question must implement the create method")

    def try_check(self,answer):
        try:
            return self.check(answer.strip())
        except Exception as e:
            print(e)
        return False

    def check(self,answer):
        """Each question must implement a check method that takes in a string and
        and returns true or false"""
        raise NotImplementedError("Each question must implement the check method")


class Add(Question):
    name = "ADD"
    def create(self,min_value,max_value):
        a = random.randint(min_value,max_value)
        b = random.randint(min_value,max_value)
        self.c = a+b

        return f"{a} {b}", f"{self.c}"
        
    def check(self,answer):
        return int(answer) == self.c
  


class Sum(Question):
    name = "SUM"
    def create(self,min_value,max_value,length):
        num_list = [random.randint(min_value,max_value) for i in range(length)]
        self.sum = sum(num_list)
        num_list_str = [str(v) for v in num_list]
        question = " ".join(num_list_str)
        return question, str(self.sum)
        
    def check(self,answer):
        return int(answer) == self.sum


class Sort(Question):
    name = "SORT"
    def create(self,min_value,max_value,length):
        num_list = [random.randint(min_value,max_value) for i in range(length)]
        self.sorted_num_list = sorted(num_list)

        num_list_str = [str(v) for v in num_list]
        question = " ".join(num_list_str)

        sorted_num_list_str = [str(v) for v in self.sorted_num_list ]
        answer = " ".join(sorted_num_list_str)

        return question, answer
        
    def check(self,answer):
        answer = [int(v) for v in answer.split(" ")]
        return answer == self.sorted_num_list
