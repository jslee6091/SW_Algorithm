import sys
sys.stdin = open("Calculator1_inputs.txt", 'r')

# 중위 표기식을 후위 표기식으로 변환 후 연산
for test_case in range(1, 11):
    length = int(input())
    expression = input()
    operator = []
    postfix = []
    calculator = []

    for i in expression:
        if i == '+' and len(operator) == 0:
            operator.append(i)
        elif i == '+' and len(operator) != 0:
            postfix.append(operator.pop())
            operator.append(i)
        else:
            postfix.append(int(i))
    postfix.append(operator.pop())

    for j in postfix:
        if j == '+':
            calculator.append(calculator.pop() + calculator.pop())
        else:
            calculator.append(j)
    
    print(f'#{test_case} {calculator[0]}')
