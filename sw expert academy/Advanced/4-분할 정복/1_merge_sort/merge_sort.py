import sys
sys.stdin = open("merge_sort_inputs.txt", 'r')

T = int(input())

# 병합정렬을 사용하여 숫자들을 오름차순으로 정렬

# 두 리스트를 정렬하여 하나로 합치는 함수
def merge(left, right):
    result = []

    # 왼쪽과 오른쪽 리스트 중 하나가 완전히 비어있는 상태가 될때까지 실행
    while left and right:
        # 왼쪽과 오른쪽 리스트의 첫번째 원소중 작거나 같은 경우 result 리스트에 저장
        if left[0] >= right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    # 왼쪽과 오른쪽 리스트 중 남은 원소가 있을시 그대로 result 리스트에 통합
    if left:
        result.extend(left)
    elif right:
        result.extend(right)
    
    return result


# 병합 정렬 함수
def mergesort(array):
    global answer

    if len(array) == 1:
        return array
    
    # 리스트를 반으로 나눔
    mid = len(array) // 2
    
    # 왼쪽과 오른쪽 리스트를 병합 정렬
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크면 1 증가
    if left[len(left)-1] > right[len(right)-1]:
        answer += 1
    
    # 왼쪽과 오른쪽 리스트를 정렬시켜 하나의 리스트로 만들고 return
    return merge(left, right)


for test_case in range(1, 1 + T):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = 0

    # 병합 정렬 실행
    numbers = mergesort(numbers)

    print(f'#{test_case} {numbers[N//2]} {answer}')
