import sys
sys.stdin = open("String_inputs.txt", 'r', encoding='UTF-8')

# Boyer-Moore Algorithm
# 내가 만들어본 코드

for test_case in range(1, 11):
    N = int(input())
    pattern = input()
    sentence = input()

    p_location = len(pattern) - 1
    s_location = len(pattern) - 1
    restore = 0
    count = 0

    while s_location < len(sentence):
        if sentence[s_location] == pattern[p_location]:
            s_location -= 1
            p_location -= 1
            restore += 1
        else:
            s_location += restore + p_location - pattern.rfind(sentence[s_location], 0, p_location)
            p_location = len(pattern) - 1
            restore = 0

        if restore == len(pattern):
            count += 1
            s_location += len(pattern)
            p_location = len(pattern) - 1

    print(f'#{test_case} {count}')
