import sys

sys.stdin = open("Forth_inputs.txt", 'r')

T = int(input())
operator = ['+', '-', '/', '*']

for test_case in range(1, T + 1):
    express = list(map(str, input().split()))
    num_list = []
    answer = 0

    for var in express:
        if var in operator:
            if len(num_list) >= 2:
                num1 = num_list.pop()
                num2 = num_list.pop()

                if var == '+':
                    num_list.append(num2 + num1)
                elif var == '-':
                    num_list.append(num2 - num1)
                elif var == '*':
                    num_list.append(num2 * num1)
                elif var == '/':
                    num_list.append(int(num2 / num1))
            else:
                answer = 'error'
                break

        elif var == '.':
            answer = num_list.pop()
        else:
            num_list.append(int(var))

    if len(num_list) > 0:
        answer = 'error'

    print(f'#{test_case} {answer}')
