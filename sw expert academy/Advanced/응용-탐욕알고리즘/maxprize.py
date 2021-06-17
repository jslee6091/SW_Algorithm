import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    arr, N = map(str, input().split())
    arr_number = list(map(int, arr))
    N_int = int(N)

    index = 0
    start = 0
    while index != N_int:
        card1 = arr_number[start]
        card2 = arr_number[start + 1]
        max_index = start + 1

        for i in range(start + 2, len(arr_number)):
            if arr_number[i] >= card2:
                card2 = arr_number[i]
                max_index = i

        print('card1 : ', card1)
        print('card2 : ', card2)
        print('max_index : ', max_index)

        if card1 >= card2:
            start += 1
            if start == len(arr_number) - 1:
                break
            else:
                continue
        else:
            print('arr_number before : ', arr_number)
            arr_number[start], arr_number[max_index] = card2, card1
            index += 1
            start += 1
            print('arr_number after : ', arr_number)

    print(f'#{test_case} {arr_number}')
