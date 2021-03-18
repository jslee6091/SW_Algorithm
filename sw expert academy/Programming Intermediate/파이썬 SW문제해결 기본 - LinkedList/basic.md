### LinkedList

- 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고 개별적으로 위치하는 원소의 주소를 연결하여 하나의 자료구조를 이룸
- 링크를 통해 원소에 접근하므로 물리적인 순서를 낮출 필요가 없음
- 크기를 동적으로 조절할 수 있어 메모리의 효율적인 사용이 가능
- 탐색 - 순차탐색



### 주요 함수





### 노드

> 하나의 원소에 필요한 데이터를 갖는 자료단위



- 데이터 필드 : 원소의 값을 저장
- 링크 필드 : 다음 노드의 주소 저장



### 헤드

> 리스트의 처음 노드를 가리키는 레퍼런스



### 단순 연결 리스트

- 노드가 링크 필드에 의해 다음 노드와 연결되는 구조
- 헤드가 가장 앞의 노드를 가리킴
- 각 노드의 링크 필드가 다음 노드를 연속적으로 가리킴
- 최종적으로 None을 가리키는 노드가 리스트의 마지막 노드

- 삽입 연산

  - ```python
    # 첫번째 노드로 데이터 삽입
    def addtoFirst(data):
        global Head
        Head = Node(data, Head)
        
    # 가운데 노드에 데이터 삽입 - pre 노드의 다음 위치
    def add(pre, data):
        if pre == None:
            print('error')
        else:
            pre.link = Node(data,pre.link)
            
    # 마지막 노드로 데이터 삽입
    def addtoLast(data):
        global Head
        if Head == None:
            Head = Node(data,None)
        else:
            p = Head
            while p.link != None:
                p = p.link
            p.link = Node(data, None)
    ```

- 삭제 연산

  - ```python
    # 첫번째 노드 삭제
    def deletetoFirst():
        global Head
        if Head == None:
            print('error')
        else:
            Head = Head.link
            
    # 가운데 노드 삭제 - pre 노드 다음 위치의 노드 삭제
    def add(pre, data):
        if pre == None or pre.link == None:
            print('error')
        else:
            pre.link = pre.link.link
    ```



### 이중 연결 리스트

> 양쪽 방향으로 순회할 수 있는 리스트
>
> 두개의 링크 필드와 한개의 데이터 필드로 구성



1. 새 노드 삽입 연산
   - 새로운 노드를 생성하여 데이터 저장
   - cur 이라는 노드의 다음 위치에 새로운 데이터를 넣고자 한다.
   - cur의 next를 new의 next에 저장하여 cur의 다음 노드를 new의 다음 노드로 연결
   - new의 값을 cur의 next에 저장하여 new 노드를 cur의 다음 노드로 연결
   - cur의 값을 new의 prev 필드에 저장하여 cur을 new의 이전 노드로 연결
   - new의 값을 new의 다음 노드의 prev 필드에 저장하여 new와 new 다음 노드를 연결
2. 노드 삭제 연산
   - cur 노드를 삭제하고자 한다.
   - 삭제할 노드의 다음 노드의 주소를 삭제할 노드의 이전 노드의 next 필드에 저장하여 링크를 연결
   - 삭제할 노드의 다음 노드의 prev 필드에 삭제할 노드의 이전 노드의 주소를 저장하여 링크를 연결
   - cur이 가리키는 노드에 할당된 메모리를 반환



### 삽입 정렬

> 연결리스트 활용한 정렬

- 모든 원소들을 앞에서부터 차례대로 이미 정렬된 부분과 비교하여 자신의 위치를 찾아냄으로써 정렬을 완성
- 정렬 방법
  - 부분집합 S : 정렬된 앞부분의 원소들
  - 부분집합 U : 아직 정렬되지 않은 나머지 원소들
    1. 정렬할 자료를 두개의 부분집합 S,U로 가정
    2. U의 원소를 하나씩 꺼내서 S의 마지막 원소부터 비교하면서 삽입
    3. 2번을 반복하면서 S의 원소는 늘리고 U의 원소는 감소함
- 시간복잡도: O(n^2)



### 병합 정렬

> 연결리스트 활용한 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 정렬하는 방식
- 분할 정복 알고리즘 활용
  - 자료를 최소 단위까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
  - Top-Down 방식
- 시간복잡도 : O(nlogn)

- 알고리즘

  - 분할 과정

    - ```python
      def merge_sort(m):
          # m 크기가 0 또는 1인 경우 바로 리턴
          if len(m) <= 1:
              return m
          
          # Divide
          mid = len(m)//2
          left = m[:mid]
          right = m[mid:]
          
          # 리스트 크기가 1이 될때까지 merge_sort 재귀호출
          left = merge_sort(left)
          right = merge_sort(right)
          
          # conquer : 분할된 리스트 병합
          return merge(left, right)
      ```

  - 병합 과정

    - ```python
      def merge(left, right):
          # 두 개의 분할된 리스트 병합하여 result 만듦
          result = []
          
          # 양쪽 리스트에 원소가 남아있는 경우 첫 원소들을 비교하여 작은 것부터 result에 추가
          while len(left) > 0 and len(right) > 0:
              if left[0] <= right[0]:
                  result.append(left.pop(0))
              else:
                  result.append(right.pop(0))
                  
          # 왼쪽 리스트에 원소가 남아있는 경우
          if len(left) > 0:
              result.extend(left)
          
          # 오른쪽 리스트에 원소가 남아있는 경우
          if len(right) > 0:
              result.extend(right)
          
          return result
      ```



### LinkedList 활용

1. Stack

   - push : 리스트의 마지막 노드에 삽입

   - pop : 리스트의 마지막 노드 반환/삭제

   - top: 리스트의 마지막 노드를 가리키는 변수

     - 초기 상태 : top = None

   - ```python
     # top에 노드를 삽입
     def push(i):
         global top
         top = Node(i, top)
     
     # top의 데이터를 반환하고 top의 링크를 다음 데이터로 바꿈
     def pop():
         global top
         
         if top == None:
             print('error')
         else:
             data = top.data
             top = top.link
             return data
     ```

2. 우선순위 큐

   - 원소 삽입 시 리스트 내 노드의 원소들과 비교하여 적절한 위치에 삽입
   - 리스트의 가장 앞쪽에 최고 우선순위가 위치함
   - 순차리스트(배열) 대비 장점
     - 삽입/삭제 연산 후 원소의 재배치 필요 없음
     - 메모리의 효율적 사용 가능

