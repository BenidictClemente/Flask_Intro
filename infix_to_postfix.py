def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    expression = expression.replace(" ", "")

    for ch in expression:
        if ch.isalnum():
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(ch, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

