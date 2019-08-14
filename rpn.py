stack = []

while(True):
    userInput = input()
    
    if(userInput.isalpha() or userInput == ''):
        print('invalid operation')
        continue
    
    if(userInput.isdigit()):
        stack.append(userInput)
        print(userInput)
    elif(userInput == '~'):
        try:
            number = int(stack.pop())
        except IndexError as error:
            print('invalid operation')
            continue
        number = number - (number * 2)
        stack.append(number)
        print(number)
    else:
        try:
            operand = userInput
        except EOFError as error:
            break
        
        try:
            num2 = int(stack.pop())
        except IndexError as error:
            print('invalid operation')
            continue

        try:
            num1 = int(stack.pop())
        except IndexError as error:
            print('invalid operation')
            stack.append(num2)
            continue

        if(operand == '+'):
            result = num1 + num2
            stack.append(result)
            print(result)
        if(operand == '-'):
            result = num1 - num2
            stack.append(result)
            print(result)
        if(operand == '*'):
            result = num1 * num2
            stack.append(result)
            print(result)
        if(operand == '/'):
            if num2 == 0:
                print("error: division by zero")
                stack.append(num1)
                stack.append(num2)
                continue
            result = num1 / num2
            stack.append(result)
            print(result)
