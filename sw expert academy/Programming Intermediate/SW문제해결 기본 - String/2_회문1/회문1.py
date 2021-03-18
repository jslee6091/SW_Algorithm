import sys
sys.stdin = open("회문1_inputs.txt", 'r')


def palindrome(array):
    count = 0
    for k in range(8-N+1):
        if array[k:k+N] == list(reversed(array[k:k+N])):
            count += 1
    return count


for test_case in range(1, 11):
    N = int(input())
    num_array = [list(map(str, list(input()))) for _ in range(8)]
    answer = 0
    for i in num_array:
        answer += palindrome(i)

    for j in zip(*num_array):
        answer += palindrome(list(j))

    print(f'#{test_case} {answer}')
