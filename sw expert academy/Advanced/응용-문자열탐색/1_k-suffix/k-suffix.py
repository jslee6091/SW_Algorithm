import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 주어진 문자열의 접미어들을 모두 나열한 후 K번째 문자열을 출력하는 문제
for test_case in range(1, 1 + T):
    K = int(input())
    word = input()
    suffix = []

    for i in range(len(word)):
        suffix.append(word[i:])

    # 문자열 사전순 정렬
    suffix.sort()

    print(f'#{test_case} {suffix[K - 1]}')
