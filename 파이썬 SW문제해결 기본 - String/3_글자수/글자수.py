import sys
sys.stdin = open("글자수_inputs.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    str1_only = []
    str2_dict = {}

    for i in str1:
        if i in str1_only:
            pass
        else:
            str1_only.append(i)

    for i in str2:
        if i in str1_only:
            if i in str2_dict:
                str2_dict[i] += 1
            else:
                str2_dict[i] = 1
        else:
            pass

    str2_tuple = sorted(str2_dict.items(), key=lambda x: x[1], reverse=True)
    print(f'#{test_case} {str2_tuple[0][1]}')

