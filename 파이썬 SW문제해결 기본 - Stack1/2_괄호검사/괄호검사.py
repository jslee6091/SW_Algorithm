import sys

sys.stdin = open("괄호검사_inputs.txt", 'r')

T = int(input())

ans_dict = {'}': '{', ')': '(', ']': '['}

for test_case in range(1, T + 1):
    sentence = list(input())
    check = []
    answer = 1

    for idx in sentence:
        # idx == '{' or idx == '(' or idx == '[' 을 values()로 표현
        if idx in ans_dict.values():
            check.append(idx)

        # idx == '}' or idx == ']' or idx == ')' 을 keys()로 표현
        elif idx in ans_dict.keys():
            if len(check) >= 1:
                num = check.pop()
            else:
                answer = 0
                break

            if ans_dict[idx] != num:
                answer = 0
                break

            # 아래의 if elif 구문을 dictionary 를 이용하여 하나의 if 문으로 표현
            # if idx == '}' and num != '{':
            #     answer = 0
            #     break
            # elif idx == ']' and num != '[':
            #     answer = 0
            #     break
            # elif idx == ')' and num != '(':
            #     answer = 0
            #     break

        else:
            pass

    if len(check) != 0:
        answer = 0

    print(f'#{test_case} {answer}')
