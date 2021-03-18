import sys

sys.stdin = open("ciphertext3_inputs.txt", 'r')

# 특정 위치에 여러 개의 숫자를 삽입, 삭제, 추가하여 암호문 완성하는 문제
for test_case in range(1, 11):
    length = int(input())
    cipher = list(map(int, input().split()))
    command_len = int(input())
    commands = input().split()
    index = 0

    while index < len(commands):
        # 수행할 연산의 종류 - 삽입(I), 삭제(D), 추가(A)
        operation = commands[index]

        # 추가 연산
        if operation == 'A':
            append_len = int(commands[index + 1])
            index += 1

            for j in range(1, append_len + 1):
                cipher.append(int(commands[index + j]))
            index += append_len + 1

        # 삽입 또는 삭제 연산
        else:
            # 암호문에 삽입 또는 삭제할 위치
            cipher_loc = int(commands[index + 1])
            # 삽입 또는 삭제할 숫자의 개수
            insert_len = int(commands[index + 2])
            index += 2

            # 숫자 삽입
            if operation == 'I':
                plus = 0

                for i in range(1, 1 + insert_len):
                    cipher.insert(cipher_loc + plus, int(commands[index + i]))
                    plus += 1
                index += insert_len + 1

            # 숫자 삭제
            else:
                del cipher[cipher_loc: cipher_loc + insert_len]
                index += 1

    print(f'#{test_case} ', end='')
    print(*cipher[:10])
