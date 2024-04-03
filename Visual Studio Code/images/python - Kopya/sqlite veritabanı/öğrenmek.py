class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.items.pop()
        
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
def evaluate_postfix(expression):
    stack=Stack()
    operators=["+","-","*","/"]    

    for item in expression.split():
        if item not in operators:
            stack.push(int(item))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if item == '+':
                stack.push(num1 + num2)
            elif item == '-':
                stack.push(num1 - num2)
            elif item == '*':
                stack.push(num1 * num2)
            elif item == '/':
                stack.push(num1 / num2)

    return stack.peek()
result=evaluate_postfix("3 4 + 5 * 6 -")
print(result)    