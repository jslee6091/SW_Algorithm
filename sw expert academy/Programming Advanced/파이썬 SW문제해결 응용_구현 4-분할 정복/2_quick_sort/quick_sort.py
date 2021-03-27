import sys
sys.stdin = open("quick_sort_inputs.txt", 'r')

T = int(input())


# 퀵 정렬을 이용한 배열 정렬
# pycharm, visual studio code 등 개발 도구에서는 문제가 없으나 sw expert academy 에서 실행하면 runtime error 가 발생한다.
# 검색을 해도 특별한 해결책이 없는데 사이트의 문제인 것 같다.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    index = 0
    small = []
    equal = []
    big = []

    while index < len(arr):
        if arr[index] < pivot:
            small.append(arr[index])
        elif arr[index] > pivot:
            big.append(arr[index])
        else:
            equal.append(arr[index])

        index += 1

    # pivot 을 기준으로 나눈 배열들을 정렬시킨 후 합쳐서 반환하는 재귀함수
    return quick_sort(small) + equal + quick_sort(big)


for test_case in range(1, T + 1):
    length = int(input())
    array = list(map(int, input().split()))

    answer = quick_sort(array)
    print(f'#{test_case} {answer[length//2]}')
