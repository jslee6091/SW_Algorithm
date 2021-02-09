### Queue



- 선입 선출 구조 : 먼저 들어온 데이터가 먼저 나가는 자료 구조
- 뒤쪽 : rear, 앞쪽 : front
- Queue의 주요 연산
  - enQueue(item) : 큐의 뒤쪽에 원소를 삽입
  - deQueue() : 큐의 앞쪽에서 원소 삭제 후 반환
  - createQueue() : 공백의 큐 생성
  - isEmpty() : 공백 상태인지 확인
  - isFull() : 포화 상태인지 확인
  - Qpeek() : 큐의 앞쪽에서 원소를 삭제 없이 반환



### Queue 의 종류

1. 선형 큐

   - 간단하고 기본적인 형태

   - *리스트* 사용

   - 1차원 리스트 이용한 큐

     - 큐의 크기 = 리스트의 크기

   - 상태 표현

     - 초기 상태: front = rear = -1
     - 공백 상태: front = rear
     - 포화 상태: rear = n-1(n: 리스트의 크기, n-1: 리스트의 마지막 인덱스)

   - 구현

   - 1. 초기 공백 큐 생성 (createQueue())

     2. 마지막 원소 뒤에 새로운 원소 삽입(enQueue(item))

        - ```python
          def enQueue(item):
              global rear
              if isFull():
                  print("Queue Full")
              else:
                  rear += 1
                  Q[rear] = item
          ```

     3. 가장 앞의 원소 삭제(deQueue())

        - ```python
          def deQueue(item):
              global front
              if isEmpty():
                  print("Queue Empty")
              else:
                  front += 1
                  return Q[front]
          ```

     4. 공백, 포화 상태 검사 (isEmpty(), isFull())

        - ```python
          def isEmpty():
              return front==rear
          
          def isFull():
              return rear == len(Q)-1
          ```

     5. 검색 (Qpeek())

        - ```python
          def Qpeek():
              if isEmpty():
                  print("Queue Empty")
              else:
                  return Q[front+1]
          ```

   - 선형 큐의 문제점

     - 리스트의 크기가 고정되어 메모리 낭비가 발생할 수 있다.
     - 삽입, 삭제가 계속될 때 데이터 공간이 있음에도 포화 상태로 잘못 인식하는 경우 발생할 수 있음
     - ex) 4 size 배열에서 rear = 인덱스 3, front = 인덱스 2 일때 앞의 0과 1 공간에 데이터를 넣을 수 있지만 포화상태로 잘못 인식한다.

   - 문제점 해결 방법

     1. 원형 큐 사용 - 메모리 절약
     2. 파이썬 리스트 사용 - 메모리 절약
     3. 단순 연결 리스트로 구현한 큐 사용 - 메모리 동적 확보
     4. 큐 라이브 사용

   - 선형 큐의 장점

     - 삽입, 삭제 속도 빠름

2. 원형 큐

   - 선형에서 발전된 형태

   - *리스트* 사용

   - 1차원 리스트를 사용하되 처음과 끝이 연결되어 원형을 이루고 있음

   - 초기 공백 상태

     - front = rear = 0

   - index 순환

     - front, rear가 마지막 인덱스인 n-1 이후에 첫번째 인덱스인 0으로 이동
     - 나머지 연산자 사용하여 구현

   - front 변수

     - 공백과 포화 상태를 구분하기 위해 front가 있는 자리는 항상 빈자리로 둠

   - ```python
     # 삽입 위치
     rear = (rear + 1) % n
     
     # 삭제 위치
     front = (front + 1) % n
     ```

   - 구현

     1. 초기 공백 큐 생성

     2. 공백 및 포화 상태 검사

        - 공백 : front = rear

        - 포화 : rear 다음 위치 = 현재 front

        - (rear + 1) % n = front

        - ```python
          def isEmpty():
              return front == rear
          
          def isFull():
              return (rear + 1) % len(cQ) == front
          ```

     3. 삽입

        - ```python
          def enQueue(item):
              global rear
              if isFull():
                  print("Queue Full")
              else:
                  rear = (rear + 1) % len(cQ)
                  cQ[rear] = item
          ```

     4. 삭제

        - ```python
          def deQueue():
              global front
              if isEmpty():
                  print("Queue Empty")
              else:
                  front = (front + 1) % len(cQ)
                  return cQ[front]
              
          def delete():
              global front
              if isEmpty():
                  print("Queue Empty")
              else:
                  front = (front + 1) % len(cQ)
          ```

     5. 파이썬으로 확인하는 코드

        - ```python
          cQ_SIZE = 3
          cQ = [0]
          
          front = rear = 0
          
          enQueue('A')
          enQueue('B')
          enQueue('C')
          print(deQueue())
          print(deQueue())
          print(deQueue())
          ```

        

3. 연결 큐

   - *연결 리스트* 형식을 이용

   - 파이썬 리스트의 단점을 보완한 것

   - 파이썬 리스트로 구현한 큐

     - append(item)
     - pop(index)

   - front = -1

   - rear = len(arr) -1

   - ```python
     def enQueue(item):
         queue.append(item)
     
     def deQueue():
         if isEmpty():
             print("queue empty")
         else:
             return queue.pop(0)
     
     def isEmpty():
         return len(queue) == 0
     
     def Qpeek():
         if isEmpty():
             print("queue empty")
         else:
             return queue[0]
         
     queue = []
     # front : -1
     # rear : len(queue) -1
     
     enQueue('A')
     enQueue('B')
     enQueue('C')
     print(deQueue())
     print(deQueue())
     print(deQueue())
     ```

   - 연결 큐의 특징

     - 각 노드에 다음 노드를 가리키는 링크가 있음
     - front와 near가 노드의 처음과 끝에 있음

   - 연결 큐 구현

     1. 초기 공백 큐 생성 (createLinkedQueue())

        - ```
          front = None
          rear = None
          ```

     2. 공백 상태 검사 (isEmpty())

        - ```python
          def isEmpty():
              return front == None
          ```

     3. 삽입 (enQueue(item))

        - ```python
          def enQueue(item):
              global front, rear
              newNode = Node(item) # 새로운 노드 생성
              if isEmpty():
                  front = newNode
              else:
                  rear.next = newNode
              rear = newNode
          ```

     4. 삭제 (deQueue())

        - ```python
          def deQueue():
              global front, rear
              if isEmpty():
                  print("queue empty")
                  return Node
              
              item = front.item
              front = front.next
              if isEmpty():
                  rear = None
              return item
          ```

     5. 파이썬으로 확인하는 코드

        - ```python
          class Node:
              def __init__(self, item, n=None):
                  self.item = item
                  self.next = n
                  
              def Qpeek():
                  return front.item
              
              def printQ():
                  f = front
                  s = ""
                  while f:
                      s += f.item + " "
                      f = f.next
                  return s
              
              front = None
              rear = None
              
              enQueue('A')
              enQueue('B')
              enQueue('C')
              printQ()
              print(deQueue())
              print(deQueue())
              print(deQueue())
          ```

        

4. 우선순위 큐

   - 우선 순위가 높은 순서대로 나가는 큐
   - 활용 분야
     - 시뮬레이션 시스템
     - 네트워크 트래픽 제어
     - OS Task Scheduling
   - 리스트를 이용한 구현
     - 원소 삽입 과정에서 우선 순위 비교하여 적절한 위치에 삽입
     - 삽입, 삭제 연산 시 원소의 재배치가 발생하여 소요 시간이 크다.
   - PriorityQueue 모듈을 이용한 구현
     - 리스트의 단점 보완

5. 큐 모듈

   - queue.Queue(maxsize) : 선입선출 큐 객체 생성

   - queue.LifoQueue(maxsize) : 후입선출 큐 객체 생성

   - queue.PriorityQueue(maxsize) : 우선순위 큐 객체 생성

   - qsize() : 큐 객체에 입력된 아이템 개수 반환

   - put() : 큐 객체에 아이템 입력

   - get() : 아이템 1개 반환

   - empty() : 큐 객체 비어있으면 True 리턴

   - full() : 큐 객체 꽉 차있으면 True 리턴

   - 예시 코드

     - ```python
       import queue
       
       q = queue.Queue()
       q.put('A')
       q.put('B')
       q.put('C')
       
       while not q.empty():
           print(q.get())
       ```




### 버퍼

> 큐를 활용하여 구현



- 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 데이터를 저장하는 메모리 영역
- 입출력, 네트워크와 관련된 기능에서 사용됨
- 순서대로 입출력과 전달이 되어야 하므로 FIFO 방식인 Queue가 활용됨





### BFS(너비 우선 탐색)

> Queue 활용



- 시작점의 인접한 정점들을 모두 차례로 방문한 후 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

- 인접 정점들을 탐색한 후 차례로 너비 우선 탐색을 진행해야 하므로 Queue가 활용됨

- ```python
  def BFS(G,v): # 그래프 G, 탐색 시작점 v
      visited = [0]*n # n: 정점의 개수
      queue = []
      queue.append(v)
      while queue:
          t = queue.pop(0)
          if not visited[t]:
              visited[t] = True
              visit(t)
          for i in G[t]:
              if not visited[i]:
                  queue.append(i)
  ```



