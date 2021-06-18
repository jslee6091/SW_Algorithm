import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

# 탐욕 알고리즘 - 주어진 횟수만큼 숫자 위치를 바꾸어 가장 큰 수를 얻는 방법찾기
# 내가 만든 코드 - 하나의 숫자를 선택 후 나머지 숫자 중 가장 큰 숫자를 선택하여 바꾸는 방법으로 구현
# 32888의 경우 오류 발생
'''
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
'''


# https://mungto.tistory.com/212 에서 참고한 코드
# 깊이 우선 탐색과 가지치기 방법으로 최대수를 얻었다.
# 바꿀수 있는 모든 경우를 고려하되 이미 탐색한 숫자는 제외하는 방식으로 가지치기 실행
def dfs(count):
    global answer
    # 횟수를 다 사용한 경우
    if not count:
        # 숫자로 바꾸고 최대수인 경우 갱신
        temp = int(''.join(values))
        if answer < temp:
            answer = temp
        return
    # 횟수가 남아있으므로 숫자 바꾸기 실행
    for i in range(length):
        # 경우의 수를 찾는거니까 i보다 큰위치부터
        for j in range(i + 1, length):
            # 두개의 위치를 바꾸고 나서
            values[i], values[j] = values[j], values[i]
            # 가지치기 위한 숫자 합치기
            temp_key = ''.join(values)
            # 어떤수가 몇회차에 나왔는지 체크, 없는 경우 1 리턴하고 경우의수에 넣어주기
            if visited.get((temp_key, count - 1), 1):
                # 이숫자는 몇회차에 사용했으니까 0으로 변환
                visited[(temp_key, count - 1)] = 0
                # dfs 실행
                dfs(count - 1)
            # 완료 후 원상복귀 - 다음 탐색을 위해
            values[i], values[j] = values[j], values[i]


for t in range(T):
    answer = -1
    value, change = input().split()
    # 바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    # 계속 쓸꺼니까 캐스팅
    length = len(values)
    # 가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t + 1, answer))
