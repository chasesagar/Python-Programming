
class Conversion:

    # Constructor to initialize class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.operators = []
        # Operand/output array
        self.top_output = -1
        self.output = []
        # Precedence settings
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # Method to check if stacks is empty
    def isEmpty(self, operand=False):
        if operand:
            return True if self.top_output == -1 else False
        return True if self.top == -1 else False
    
    # Method that returns top value of the stacks
    def peek(self, operand=False):
        
        return self.output[-1] if operand else self.operators[-1]
    
    # Method to pop element from top of the stacks
    def pop(self, operand=False):
        if operand:
            if not self.isEmpty(True):
                operand1 = self.output.pop()
                operand2 = self.output.pop()
                return operand2 + operand1
            else: 
                return 'Output stack is empty'
          
        if not self.isEmpty():
            self.top -= 1
            return self.operators.pop()
        else: 
            return 'Stack is empty'
    
    # Method to push given element into the stacks
    def push(self, att, operand=False):
        if operand:
            self.top_output += 1
            self.output.append(att)
        else:
            self.top += 1
            self.operators.append(att)

    # A utility function to check if the given character is an operand
    def isOperand(self, ch):
        return ch.isalpha() or ch.isnumeric()

    # Method to check if the precedence of the operator is 
    # strictly less than top of the stack
    def notGreator(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False

        except KeyError:
            return False

    # Main method that convert given expression into prefix experssion 
    def infixToPrefix(self, exp):
        for i in exp:
            # an operand is encountered
            if self.isOperand(i):
                self.push(i, True)
            
            # an closing parentheses/bracket is encountred
            elif i == '(':
                self.push(i)
            elif i == ')':
                while (not self.isEmpty() and self.peek() != '('):
                    operator  = self.pop()
                    operands = self.pop(True) 
                    self.push(operator + operands, True)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            # and operator is encountered
            else:
                while (not self.isEmpty() and self.notGreator(i)):
                    operator = self.pop()
                    operands = self.pop(True)
                    self.push(operator + operands, True)
                
                self.push(i)

        # pop all operators from the stack  
        while not self.isEmpty():
            operator = self.pop()
            operands = self.pop(True)
            self.push(operator + operands, True)
        print (f"Infix to prefix output expression is: {self.output[0]}")

            
# Driver program to test above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPrefix(exp)
            