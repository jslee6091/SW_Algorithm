import sys
sys.stdin = open("Sum_inputs.txt", 'r')

for test_case in range(1, 11):
    N = int(input())

    num_array = []
    answer = []

    for i in range(100):
        num_array.append(list(map(int, input().split())))

    # 행의 합
    for j in num_array:
        answer.append(sum(j))

    # 열의 합
    for i in range(100):
        col = 0
        for j in num_array:
            col += j[i]
        answer.append(col)

    # 오른쪽 아래로 대각선의 합 \
    r_diagonal = 0
    for i in range(100):
        r_diagonal += num_array[i][i]
    answer.append(r_diagonal)

    # 왼쪽 아래로 대각선의 합 /
    l_diagonal = 0
    for i in range(100):
        l_diagonal += num_array[i][99-i]
    answer.append(l_diagonal)

    answer = sorted(answer, reverse=True)

    print(f'#{test_case} {answer[0]}')
