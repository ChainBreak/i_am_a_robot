import random
from essential_generators import DocumentGenerator
document_generator = DocumentGenerator()

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


class Binary(Question):
    name = "BINARY"
    def create(self,min_value,max_value):
        self.i = random.randint(min_value,max_value)

        return f"{self.i:b}", f"{self.i}"
        
    def check(self,answer):
        return int(answer) == self.i

class Caesar(Question):
    name = "CAESAR"

    def map(self,c,shift):
        a = ord("a")
        z = ord("z")
        A = ord("A")
        Z = ord("Z")

        c = ord(c)
        if c >=a and c <= z:
            c = ((c - a + shift) % 26) + a
        if c >=A and c <= Z:
            c = ((c - A + shift) % 26) + A
        
        return chr(c)


    def create(self,plain_text=None):
        shift = random.randint(1,25)
        if plain_text == None:
            self.plain_text= document_generator.sentence()
        else:  
            self.plain_text = plain_text
        cipher_text = "".join([self.map(c,shift) for c in self.plain_text])

        return f"{shift} {cipher_text}", f"{self.plain_text}"
        
    def check(self,answer):
        return answer.strip() == self.plain_text.strip()
