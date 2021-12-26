def evaluatePostfix(s):
    operands = []
    for i in s:
        if i.isnumeric():
            operands.append(i)
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.append(str(eval(op1+i+op2)))
    return operands.pop()
if __name__ == '__main__':
    s = ['2','1','+','3','*']
    s1 = ['4','13','5','/','+']
    # print(convertToPostfix(s))
    print(evaluatePostfix(s1))
