import sys
sys.stdin = open("공통단어검색_inputs.txt", 'r')

T = int(input())

# A와 B가 가진 단어 중 공통으로 가진 단어의 개수 구하는 문제
for test_case in range(1, 1 + T):
    A, B = map(int, input().split())
    a_word = [input() for _ in range(A)]

    answer = 0
    for _ in range(B):
        if input() in a_word:
            answer += 1

    print(f'#{test_case} {answer}')
