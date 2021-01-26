import sys

sys.stdin = open("문자열_비교.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    start1 = len(str1) - 1
    start2 = len(str1) - 1
    answer = 0

    while True:
        if str1[start1] == str2[start2]:
            start1 -= 1
            start2 -= 1
            if start1 == -1:
                answer = 1
                break
        else:
            start1 = len(str1) - 1
            start2 += len(str1) - 1 - str1.rfind(str2[start2], 0, start1)

        if start2 >= len(str2):
            answer = 0
            break

    print(f'#{test_case} {answer}')
