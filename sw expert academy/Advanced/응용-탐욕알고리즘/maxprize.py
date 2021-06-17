import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    arr, N = map(str, input().split())
    arr_number = list(map(int, arr))
    N_int = int(N)
    print('arr : ', arr_number, type(arr_number))
    print('N : ', N_int, type(N_int))
    print(max(arr_number[1:]), type(max(arr_number[1:])), arr_number.index(max(arr_number[1:])))
    gg = arr_number.index(max(arr_number[1:]))
    arr_number[0], arr_number[gg] = arr_number[gg], arr_number[0]
    print(arr_number)

    # index = 0
    # while index != N_int:
    #     card1, card2 = arr_number[0], max(arr_number[1:])
    #     print('card1 : ', card1)
    #     print('card2 : ', card2)
    #     if card1 >= card2:
    #         continue
    #     else:
    #         arr_number[0], arr_number[arr_number.index(card2)] = card2, card1
    #         index += 1
