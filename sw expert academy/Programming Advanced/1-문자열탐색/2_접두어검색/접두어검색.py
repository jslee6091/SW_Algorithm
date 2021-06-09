import sys
sys.stdin = open('접두어검색_inputs.txt', 'r')

T = int(input())

# 접두어를 비교하는 문제
for test_case in range(1, 1 + T):
    A_num, B_num = map(int, input().split())
    A = []
    B = []
    answer = 0

    # A와 B의 문자열들을 리스트에 저장
    for i in range(A_num):
        A.append(input())

    for i in range(B_num):
        B.append(input())

    # B의 각 문자열의 길이만큼 A의 문자열들을 슬라이싱하여 비교
    for i in B:
        for j in A:
            if j[:len(i)] == i:
                answer += 1
                break

    print(f'#{test_case} {answer}')
