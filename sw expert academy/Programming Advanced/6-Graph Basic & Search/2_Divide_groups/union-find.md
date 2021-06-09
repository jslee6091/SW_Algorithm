### 상호 배타 집합

- 서로 중복 포함된 원소가 없는 집합들
- **교집합이 없음**
- 집합에 속한 하나의 특정 원소를 통해 각 집합들을 구분
  - 특정 원소 - 대표자(representative)
- 상호 배타 집합을 표현하는 방법
  - 연결리스트
  - 트리



### 상호 배타 집합 연산

1. Make-Set(x) - 원소 x만으로 구성된 집합 생성 연산
2. Find-Set(x) - 임의의 원소 x가 속한 집합 알아내기 위해 사용, 집합의 대표자를 알기 위한 연산
3. Union(x,y) - x원소가 속한 집합과 y원소가 속한 집합을 하나의 집합으로 합치는 연산



### 트리를 이용한 표현

- 하나의 집합을 하나의 트리로 표현

- 자식 노드가 부모 노드를 가리키며 루트 노드가 대표자가 됨

- Make-Set(x)

  - ```python
    def Make_Set(x):
        p[x] = x
    ```

- Find-Set(x)

  - ```python
    def Find_Set(x):
        if x == p[x]:
            return x
        else:
            return Find_Set(p[x])
    ```

- Union(x,y)

  - ```python
    def Union(x,y):
        p[Find_Set(y)]+Find_Set(x)
    ```



### 트리로 표현시 문제점

1. 집합을 Union하는 과정에서 편향된 트리 구조 생성 가능
2. 간선의 수만큼 재귀 호출 필요



#### 해결책

모든 원소들이 루트를 부모로 가리키면 됨

- 간선 하나를 따라가면 바로 루트노드에 도달



### 연산 효율 높이는 방법

1. Rank를 이용한 union
   - 각 노드는 자신을 루트로 하는 서브트리의 높이를 Rank라는 이름으로 저장
   - 두 집합을 합칠 때 Rank가 낮은 집합을 Rank가 높은 집합에 붙임
   - 트리 높이가 같은 경우 아무 트리나 선택해서 다른 트리의 서브트리로 포함시키고 Rank값은 +1 함(높이가 증가하므로)
2. Path compression
   - Find-Set 하는 과정에서 만나는 모든 노드들이 직접 Root를 가리키도록 부모 정보를 변경



### Path compression을 적용한 알고리즘



1. Make_Set()

   - ```python
     # p[x]: 노드 x의 부모 저장
     # rank[x]: 루트 노드가 x인 트리의 Rank 값 저장
     def Make_Set(x):
         p[x] = x # 자기 자신
         rank[x] = 0
     ```

2. Find_Set()

   - ```python
     def Find_Set(x):
         if x != p[x]: # x가 루트가 아닌 경우
             p[x] = Find_Set(p[x]) # Path Compression
         return p[x]
     ```

   - 특정 노드에서 루트까지의 경로에 존재하는 모든 노드가 루트를 가리키도록 변경

3. Union()

   - ```python
     def Link(x,y):
         if rank[x]>rank[y]:
             p[y] = x
         else:
             p[x] = y
         if rank[x] == rank[y]:
             rank[y] += 1
     
     def Union(x,y):
         Link(Find_Set(x), Find_Set(y))
     ```



- 상호 배타 집합의 연산들은 `Kruskal Minimum Spanning Tree (MST)` 알고리즘에 활용됨
- 각 집합에 속한 원소의 수를 관리할 수 있고 이를 바탕으로 가장 큰 집합 찾기, 집합의 노드 개수가 몇 개 이상이 되는 시점 찾기 등이 가능하다.



