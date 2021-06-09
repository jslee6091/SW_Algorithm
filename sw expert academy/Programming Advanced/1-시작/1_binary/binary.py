import sys
sys.stdin = open("binary_inputs.txt", 'r')

# 16진수를 2진수로 변환하는 문제

T = int(input())
hex_to_dec = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for test_case in range(1, T + 1):
    N, number = map(str, input().split())
    # 10 이상을 넘어가는 숫자인지 판별하기 위한 리스트
    is_hex = list(hex_to_dec.keys())
    stack = []
    answer = ''

    # 16진수의 각 자릿수를 2진수로 변환
    for ch in number:
        # 숫자가 10(A) 이상인 경우
        if ch in is_hex:
            temp = hex_to_dec[ch]
        else:
            temp = int(ch)

        # 숫자가 0이 될때까지 2로 나누고 나머지를 스택에 넣는다.
        while temp != 0:
            stack.append(temp % 2)
            temp //= 2

        # 만약 4자리 이진수가 아닌 경우 0을 추가로 더 채움
        while len(stack) != 4:
            stack.append(0)

        # 스택에 넣은 2진수 숫자들을 다시 꺼내면서 2진수 완성
        while stack:
            answer += str(stack.pop())

    print(f'#{test_case} {answer}')
