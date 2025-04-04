def plus(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
class calculator:
    def __init__(self,internState):
        self.internState=0
    def get_internState(self):
        return self.internState
    def run(self , command , a,b):
        if command=="+":
            return plus(a,b)
        elif command=="-":
            return substract(a,b)
        elif command=="x":
            return multiply(a,b)
        elif command=="/":
            return divide(a,b)
        else:
            return "Not valid"

