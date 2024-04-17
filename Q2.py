def bracketsCheck(line):
    stack = []
    result = []

    for i, char in enumerate(line):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
                result.append(' ')
                result.append(' ')
            else:
                result.append('?')
        else:
            result.append(' ')

    for index in stack:
        result.insert(index, 'x')
        
    return ''.join(result)
 
while True:
    try:
        line = input()
        print(bracketsCheck(line))
    except EOFError:
        break
