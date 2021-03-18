import sys
sys.stdin = open("회문2_inputs.txt", 'r')


def palindrome(array, n):
    result = 0
    for k in range(100-n+1):
        if array[k:k+n] == list(reversed(array[k:k+n])):
            result = 1
            break
    return result


for test_case in range(1, 11):
    N = input()
    num_array = [list(map(str, list(input()))) for _ in range(100)]
    answer = 0

    for number in range(100, 0, -1):
        number1 = 0
        number2 = 0
        for i in num_array:
            if palindrome(i, number):
                number1 = 1
                break
        else:
            for j in zip(*num_array):
                if palindrome(list(j), number):
                    number2 = 1
                    break

        if number1 or number2:
            answer = number
            break

    print(f'#{test_case} {answer}')
