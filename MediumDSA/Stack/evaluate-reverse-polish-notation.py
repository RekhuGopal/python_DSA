def evalRPN(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            # If the token is an operand, push it onto the stack
            stack.append(int(token))
        else:
            # If the token is an operator, pop the last two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Perform the operation based on the operator
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                # Division truncates toward zero
                stack.append(int(operand1 / operand2))
    
    # The result will be the last element in the stack
    return stack[0]

# Example usage:
tokens1 = ["2","1","+","3","*"]
print(evalRPN(tokens1))  # Output: 9

tokens2 = ["4","13","5","/","+"]
print(evalRPN(tokens2))  # Output: 6

tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens3))  # Output: 22
