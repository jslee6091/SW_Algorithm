import sys
sys.stdin = open("ElectronicCart_inputs.txt", 'r')


# 참고 : https://daep93.github.io/2020/05/14/SW-5265/
# 순회 외판원 문제(TSP)
# 동적 계획법을 적용하여 해결
def get_remains(digits):
    result = set()
    for i in range(N-1):
        if digits & (1 << i):
            result.add(i+1)
    return result


def tsp(Cost):
    # matrix N * 2^N
    Used = [[0 for _ in range(2 ** (N-1))] for _ in range(N)]

    for i in range(1, N):
        Used[i][0] = Cost[i][0]

    for remains in range(1, 2 ** (N - 1)-1):
        for start in range(N-1, 0, -1):
            candidates = set()
            remain_set = get_remains(remains)

            if start in remain_set:
                continue

            else:
                for next_start in remain_set:
                    next_remains = remains - (1 << (next_start-1))
                    candidates.add(Cost[start][next_start]+Used[next_start][next_remains])

                Used[start][remains] = min(candidates)

    remains=2**(N-1)-1
    candidates = set()
    remain_set = get_remains(remains)
    for next_start in remain_set:
        next_remains = remains - (1 << (next_start - 1))
        candidates.add(Cost[0][next_start] + Used[next_start][next_remains])

    return min(candidates)


for t in range(1, int(input())+1):
    N = int(input())
    Cost = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{t} {tsp(Cost)}')
