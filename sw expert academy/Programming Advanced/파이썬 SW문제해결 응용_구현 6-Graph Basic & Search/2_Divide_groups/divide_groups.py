import sys
sys.stdin = open('divide_groups_inputs.txt', 'r')

T = int(input())


# Union-find 을 이용하여 노드들의 집합의 개수를 구하는 문제
# 참고 : https://mungto.tistory.com/221
def get_parent(x):
    # x와 parent[x]의 값이 같으면 부모노드이고 다르면 부모노드가 아니므로 함수 재호출
    if parent[x] != x:
        parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    # x의 부모노드를 a에 할당
    a = get_parent(x)
    # y의 부모노드를 b에 할당
    b = get_parent(y)

    # a와 b중 더 큰 값이 더 작은 값의 자식이 됨
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    # 부모 노드를 판별하는 리스트 - 숫자가 같으면 같은 부모노드에 속한 자식들임
    parent = [i for i in range(N + 1)]
    votes = list(map(int, input().split()))

    # 노드 연결 정보 만들기
    for i in range(0, M * 2, 2):
        union_parent(votes[i], votes[i + 1])

    answer = set()
    for i in parent:
        answer.add(get_parent(i))

    print(f'#{test_case} {len(answer) - 1}')
