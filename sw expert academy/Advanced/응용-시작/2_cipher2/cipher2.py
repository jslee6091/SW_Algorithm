import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    # arr = [input().replace('0', '') for _ in range(N)]
    arr = [input() for _ in range(N)]

    # while 문에서 2로 나누면서 구하는 방식은 시간이 매우 오래 걸리므로 dictionary 를 활용
    hexabinary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                  '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    cipherSet = set()
    cipherBinarySet = set()
    cipherBinaryAll = ''

    for i in arr:
        j = i.replace('0', '')
        if len(j) > 0:
            cipherSet.add(i)

    print('cipherSet : ', cipherSet)

    # 암호코드 식별 - 한 행에 여러 암호 코드가 있는 경우까지 식별
    cipherRecognize = set()
    cipherRecognizeChar = ''

    for i in cipherSet:
        for j in i:
            if j != '0':
                cipherRecognizeChar += j
            elif len(cipherRecognizeChar) > 0:
                cipherRecognize.add(cipherRecognizeChar)
                cipherRecognizeChar = ''

    print('cipherRecognize : ', cipherRecognize)

    for i in cipherRecognize:
        for j in i:
            cipherBinaryAll += hexabinary[j]

        # 끝의 숫자 0들 지우기
        num = -1
        while cipherBinaryAll[num] == '0':
            num -= 1

        cipherBinaryAll = cipherBinaryAll[:num + 1]
        cipherBinarySet.add(cipherBinaryAll)

        cipherBinaryAll = ''

    if test_case <= 5:
        print(cipherBinarySet)
