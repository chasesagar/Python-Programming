
class Conversion:

    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = [] # this array is used aa a stack
        # Precedence settings
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # method to check if stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from top of the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return 'Stack is empty'

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check if the given character 
    # is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Method to check if the precedence of the operator is 
    # strictly less than top of the stack
    def notGreator(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
            
        except KeyError:
            return False

    # The main function to convert given infix expression 
    # to postfix expression
    def infixToPostfix(self, exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while ( not self.isEmpty() and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreator(i)):
                    self.output.append(self.pop())
                self.push(i)

        # pop all operators from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
        print ("Infix to postfix output expression is: "+ "".join(self.output))

# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)


    