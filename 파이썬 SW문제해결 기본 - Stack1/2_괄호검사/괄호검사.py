import sys
sys.stdin = open("괄호검사_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    sentence = list(input())
    check = []
    answer = 1

    for idx in sentence:
        if idx == '{' or idx == '(' or idx == '[':
            check.append(idx)
        elif idx == '}' or idx == ']' or idx == ')':
            if len(check) >= 1:
                num = check.pop()
            else:
                answer = 0
                break

            if idx == '}' and num != '{':
                answer = 0
                break
            elif idx == ']' and num != '[':
                answer = 0
                break
            elif idx == ')' and num != '(':
                answer = 0
                break
        else:
            pass

    if len(check) != 0:
        answer = 0

    print(f'#{test_case} {answer}')
