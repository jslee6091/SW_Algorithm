import sys

sys.stdin = open("sum_of_subset_inputs.txt", 'r')

T = int(input())


# 동적계획법 - 부분 집합의 합 찾기
# 참고 : https://daep93.github.io/2020/05/04/SW-5260/
def partial_sum(K, integers):
    potential = sum(integers)
    if potential < K:
        return 0
    elif potential == K:
        return 1
    else:
        last_ele = integers[-1]
        if last_ele == K:
            return 1 + partial_sum(K, integers[:-1])
        else:
            if K - last_ele > 0:
                return partial_sum(K - last_ele, integers[:-1]) + partial_sum(K, integers[:-1])
            else:
                return partial_sum(K, integers[:-1])


for t in range(1, T + 1):
    N, K = map(int, input().split())
    integers = [i for i in range(1, N + 1)]
    answer = partial_sum(K, integers)
    print(f'#{t} {answer}')
