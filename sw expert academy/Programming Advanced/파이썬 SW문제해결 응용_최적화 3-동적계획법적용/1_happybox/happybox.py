import sys
from collections import namedtuple

sys.stdin = open("happybox_inputs.txt", 'r')


# 참고 : https://daep93.github.io/2020/05/04/SW-5258/
# 동적 계획법 활용하여 최대 가격으로 상자를 고르는 문제
def Knapsack(matrix, inven, W, K):
    if matrix[K][W] != -1:
        return matrix[K][W]

    elif W == 0 or K == 0:
        matrix[K][W] = 0
        return 0
    else:
        case1 = 0
        if W >= inven[K].w:
            case1 = Knapsack(matrix, inven, W - inven[K].w, K - 1) + inven[K].v
        case2 = Knapsack(matrix, inven, W, K - 1)
        matrix[K][W] = max(case1, case2)
        return matrix[K][W]


Item = namedtuple('Item', 'w, v')


for t in range(1, int(input()) + 1):
    # Given size of box which can include items and number of items
    box_size, items_num = map(int, input().split())

    # Initialize inventory : Store items made by namedtuple(field: weight 'w' and value 'v')
    inventory = [None for _ in range(items_num)]

    # Receive information of items
    for idx in range(items_num):
        item = Item._make(map(int, input().split()))
        inventory[idx] = item
    print(inventory, type(inventory[0]))

    # sort items in inventory with value per weight
    inventory.sort(key=lambda item: item.v / item.w)
    print(inventory)
    inventory.insert(0, Item._make([0, 0]))
    Acc_matrix = [[-1 for _ in range(box_size + 1)] for _ in range(items_num + 1)]

    result = Knapsack(Acc_matrix, inventory, box_size, items_num)
    print(f'#{t} {result}')
