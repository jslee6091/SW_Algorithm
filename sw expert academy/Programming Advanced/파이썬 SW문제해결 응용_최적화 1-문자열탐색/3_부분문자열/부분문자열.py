import sys
sys.stdin = open("부분문자열_inputs.txt", 'r')

T = int(input())

for test_case in range(1, 1 + T):
    N, arr = input().split()
    num = 1
    partial = []
    while num <= len(arr):
        start = 0
        while start + num <= len(arr):
            partial.append(arr[start:start+num])
            start += 1
        num += 1

    partial2 = list(set(partial))
    partial2.sort(key=lambda x: x)
    answer = partial2[int(N)-1]
    print(f'#{test_case} {answer[0]} {len(answer)}')
