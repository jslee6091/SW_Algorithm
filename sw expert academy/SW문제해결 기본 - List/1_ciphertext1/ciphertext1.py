import sys

sys.stdin = open("ciphertext1_inputs.txt", 'r')

# 특정 위치에 여러 개의 숫자를 삽입하여 암호문 완성하는 문제
for test_case in range(1, 11):
    length = int(input())
    cipher = list(map(int, input().split()))
    command_len = int(input())
    commands = input().split()
    index = 0

    while index < len(commands):
        # 암호문에 삽입할 위치
        cipher_loc = int(commands[index + 1])
        # 삽입할 숫자의 개수
        insert_len = int(commands[index + 2])
        index += 2
        plus = 0
        
        for i in range(1, 1 + insert_len):
            cipher.insert(cipher_loc + plus, int(commands[index + i]))
            plus += 1
        index += insert_len + 1

    print(f'#{test_case} ', end='')
    print(*cipher[:10])
