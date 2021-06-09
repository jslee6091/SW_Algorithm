import sys
sys.stdin = open("container_inputs.txt", 'r')

T = int(input())

# 화물이 실려 있는 일정량의 컨테이너를 적재 용량이 각기 다른 트럭들이 옮길때 최대로 옮길 수 있는 화물의 무게 구하기
for test_case in range(1, T + 1):
    # 컨테이너와 트럭의 개수
    container_num, truck_num = map(int, input().split())
    # 컨테이너마다 실린 화물의 무게를 입력받은 후 내림차순 정렬
    containers = sorted(list(map(int, input().split())), reverse=True)
    # 각 트럭 마다 적재가능한 용량
    trucks = list(map(int, input().split()))
    answer = 0

    # 트럭이 한번씩 모두 옮길때까지 수행
    while trucks:
        check = containers.pop(0)
        # 각 화물에 대하여 적재 가능한 트럭이 운반
        for i in trucks:
            if i >= check:
                answer += check
                trucks.remove(i)
                break

        # 운반 과정에서 조기에 컨테이너를 모두 옮겼다면 바로 break
        if not containers:
            break

    print(f'#{test_case} {answer}')
