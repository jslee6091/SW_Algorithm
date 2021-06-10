import sys
sys.stdin = open("Calculator2_inputs.txt", 'r')

# 덧셈과 곱셈이 포함된 후위표기식 연산
for test_case in range(1, 11):
    length = int(input())
    expression = input()

    # 후위표기식 저장 리스트
    postfix = []

    # operator 저장 리스트
    operator = []

    # 후위표기식 연산에 사용되는 리스트
    calculator = []

    # 후위표기식으로 변환
    for char in expression:
        # *인 경우 operator 리스트에 같은 * 연산자가 있을때 그것을 빼서 postfix에 넣는다.
        if char == '*':
            while len(operator) != 0:
                check = operator.pop()
                if check == '*':
                    postfix.append(check)
                else:
                    operator.append(check)
                    break
            operator.append(char)
        # +인 경우 operator 리스트에 들어있는 모든 연산자를 빼고 자신을 넣는다.
        elif char == '+':
            while len(operator) != 0:
                postfix.append(operator.pop())
            operator.append(char)
        else:
            postfix.append(int(char))

    # operator에 남아있는 연산자 모두 꺼내기
    while len(operator) != 0:
        postfix.append(operator.pop())

    # 변환된 후위표기식 연산
    for var in postfix:
        if var == '+':
            calculator.append(calculator.pop() + calculator.pop())
        elif var == '*':
            calculator.append(calculator.pop() * calculator.pop())
        else:
            calculator.append(var)

    print(f'#{test_case} {calculator.pop()}')
