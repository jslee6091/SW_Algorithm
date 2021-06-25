import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 부분문자열을 사전순으로 정렬한 후 K번째 문자열 구하기
# 부분 문자열은 전체 문자열에서 두 문자 사이의 모든 문자를 포함하는 문자열을 의미한다.
for test_case in range(1, 1 + T):
    K = int(input())
    word = input()

    # 부분 문자열 저장
    substring = set()
    num = 1
    # 크기가 1 부터 전체 문자열 크기까지의 부분 문자열 구하기
    while num <= len(word):
        start = 0
        # 처음부터 문자열 끝부분까지 num 크기의 문자열 저장
        while start + num <= len(word):
            substring.add(word[start:start + num])
            start += 1
        num += 1

    # set 을 list 로 변환, 사전순 정렬 후 K 번째 문자열 출력
    sublist = list(substring)
    sublist.sort()
    answer = sublist[K - 1]
    print(f'#{test_case} {answer}')
