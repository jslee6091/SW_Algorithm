import sys
sys.stdin = open("반복문자_지우기_inputs.txt", 'r')

T = int(input())


for test_case in range(1, T + 1):
    num_list = list(input())

    check = []
    for var in num_list:
        if len(check) == 0:
            check.append(var)
        elif check[len(check)-1] == var:
            check.pop()
        else:
            check.append(var)

    answer = len(check)

    print(f'#{test_case} {answer}')
