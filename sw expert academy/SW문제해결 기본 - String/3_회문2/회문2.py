import sys
sys.stdin = open("회문2_inputs.txt", 'r')


def palindrome(array, n):
    for j in range(100-n+1):
        if array[j:j+n] == list(reversed(array[j:j+n])):
            return 1
    return 0


for test_case in range(1, 11):
    N = input()
    num_array = [list(map(str, list(input()))) for _ in range(100)]
    number = 0
    answer = 0

    for i in num_array:
        while number <= 100:
            if palindrome(i, number):
                answer = number
            number += 1

    number = 0
    for j in zip(*num_array):
        while number <= 100:
            if palindrome(j, number):
                answer = number
            number += 1

    print(f'#{test_case} {answer}')
