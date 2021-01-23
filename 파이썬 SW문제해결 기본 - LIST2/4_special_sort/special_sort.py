import sys

sys.stdin = open("special_sort_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lists = list(map(int, input().split()))

    for i in range(0, len(lists)):
        ind = i
        for j in range(i + 1, len(lists)):
            if i % 2 == 0:  # 큰 수
                if lists[ind] < lists[j]:
                    ind = j
            else:  # 작은 수
                if lists[ind] > lists[j]:
                    ind = j
        lists[ind], lists[i] = lists[i], lists[ind]

    print(f'#{test_case}', end=' ')
    for num in lists[:10]:
        print(num, end=' ')
    print()
