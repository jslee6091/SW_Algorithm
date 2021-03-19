import sys

sys.stdin = open("binary_inputs.txt", 'r')

T = int(input())

# 소수를 2진수로 나타내는 문제
for test_case in range(1, T + 1):
    number = float(input())
    start = -1
    answer = ''

    # 2진수 변환하기
    while True:
        
        # 13자리 이상부터는 overflow 처리
        if start == -13:
            answer = 'overflow'
            break
        
        # 2의 제곱이 입력 받은 숫자보다 작거나 같으면 해당 자릿수는 1이 됨
        if 2**start <= number:
            answer += '1'
            number -= 2**start
        # 그렇지 않으면 0이 됨
        else:
            answer += '0'
        
        # 입력 받은 숫자가 0이 되면 다 끝났으므로 break
        if number == 0:
            break
        
        start -= 1

    print(f'#{test_case} {answer}')
