class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if isinstance(token, int):
            postfixList.append(token)
        else:
            #operators
            if token == '(':
                opStack.push(token)
            elif token == ')':
                while not opStack.isEmpty():
                    top = opStack.pop()
                    if top == '(':
                        break
                    postfixList.append(top)
            else:
                # operators other than parentheses
                if opStack.isEmpty():
                    opStack.push(token)
                elif prec[token] > prec[opStack.peek()]:
                    opStack.push(token)
                else:
                    while prec[token] <= prec[opStack.peek()]:
                        postfixList.append(opStack.pop())
                    opStack.pop(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if isinstance(token, int):
            postfixList.append(token)
        else:
            #operators
            if token == '(':
                opStack.push(token)
            elif token == ')':
                while not opStack.isEmpty():
                    top = opStack.pop()
                    if top == '(':
                        break
                    postfixList.append(top)
            else:
                # operators other than parentheses
                if opStack.isEmpty():
                    opStack.push(token)
                elif prec[token] > prec[opStack.peek()]:
                    opStack.push(token)
                else:
                    while not opStack.isEmpty() and prec[token] <= prec[opStack.peek()]:
                        postfixList.append(opStack.pop())
                    opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    stack = ArrayStack()
    for token in tokenList:
        if isinstance(token, int):
            stack.push(token)
        else:
            a,b = stack.pop(), stack.pop()
            if token == '+':
                stack.push(a+b)
            elif token == '-':
                stack.push(b-a)
            elif token == '*':
                stack.push(a*b)
            else:
                stack.push(b/a)
    return stack.pop()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
solution("7 * (9 - (3+2))")
