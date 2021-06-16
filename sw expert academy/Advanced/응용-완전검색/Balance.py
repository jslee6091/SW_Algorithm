import sys, math
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    N = int(input())
    info = list(map(int, input().split()))
    x, mass = info[:N], info[N:]

    for idx in range(N - 1):
        distance = (math.sqrt(mass[idx]) * (x[idx + 1] - x[idx])) / (math.sqrt(mass[idx]) + math.sqrt(mass[idx + 1]))
        distance2 = ((mass[idx] ** 0.5) * (x[idx + 1] - x[idx])) / ((mass[idx] ** 0.5) + (mass[idx + 1] ** 0.5))

        answer = x[idx] + distance
        print('%.10f' % (x[idx] + distance2))
        # strength = 0
        # for idd in range(idx + 1, N):
        #     strength += mass[idd] / (x[idd] - x[idx] - )

