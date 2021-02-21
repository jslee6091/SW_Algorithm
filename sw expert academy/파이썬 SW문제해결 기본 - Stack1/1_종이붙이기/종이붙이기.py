import sys
sys.stdin = open("종이붙이기_inputs.txt", 'r')

T = int(input())


def fibo_converted(n, memo):
    if n >= 2 and len(memo) <= n:
        memo.append(2*fibo_converted(n-2, memo)+fibo_converted(n-1, memo))
    return memo[n]


for test_case in range(1, T + 1):
    N = int(input())
    fibo_list = [1, 3]
    answer = fibo_converted(int(N/10)-1, fibo_list)
    print(f'#{test_case} {answer}')
