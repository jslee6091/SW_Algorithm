import sys
sys.stdin = open("Calculator3_inputs.txt", 'r')

# 괄호와 덧셈, 곱셈 연산이 포함된 계산식의 후위표기법 연산
for test_case in range(1, 11):
    length = int(input())
    expression = input()

    # 후위표기법 수식
    postfix = []

    # 연산자 저장
    operator = []

    # 후위표기법 연산
    calculator = []

    # 후위표기법 변환
    for ch in expression:
        # '(' 일때는 무조건 operator 에 삽입
        if ch == '(':
            operator.append(ch)

        # '+' 일때는 '('인 경우를 제외하고 무조건 postfix 에 옮기고 operator 에 삽입
        elif ch == '+':
            while True:
                check1 = operator.pop()
                if check1 != '(':
                    postfix.append(check1)
                else:
                    operator.append(check1)
                    break
            operator.append(ch)

        # '*' 일때는 같은 연산자인 경우를 제외하고 operator 에 무조건 삽입
        elif ch == '*':
            while True:
                check2 = operator.pop()
                if check2 == '*':
                    postfix.append(check2)
                else:
                    operator.append(check2)
                    break
            operator.append(ch)

        # ')' 일때는 '('가 나올때까지 무조건 빼서 postfix 에 삽입 후 괄호연산자는 제거
        elif ch == ')':
            while True:
                check3 = operator.pop()
                if check3 == '(':
                    break
                else:
                    postfix.append(check3)

        # 정수인 경우는 postfix 에 정수형 변환 후 삽입
        else:
            postfix.append(int(ch))

    # 남은 연산자들 postfix 에 삽입
    while len(operator) != 0:
        postfix.append(operator.pop())

    # 후위표기식 연산 - 괄호는 모두 제거되었으므로 없는 경우와 똑같이 계산
    for var in postfix:
        if var == '*':
            calculator.append(calculator.pop() * calculator.pop())
        elif var == '+':
            calculator.append(calculator.pop() + calculator.pop())
        else:
            calculator.append(var)

    print(f'#{test_case} {calculator.pop()}')
