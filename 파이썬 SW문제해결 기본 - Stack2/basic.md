### 중위표기법

- 스택을 이용하여 연산자를 피연산자의 가운데 표기하는 방법
- A+B



### 후위표기법

- 연산자를 피연산자 뒤에 표기하는 방법
- AB+



### 중위표기법을 후위표기법으로 변환하는 방법

> 스택을 이용한 방법



1. 입력 받은 중위표기식에서 토큰을 읽음
2. 토큰이 피연산자이면 토큰을 출력
3. 토큰이 연산자(괄호포함)일 경우
   - 우선순위가 높으면 -> 스택에 push
   - 우선순위가 높지 않으면 -> 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push
   - top에 연산자가 없으면 -> push 
4. 토큰이 오른쪽 괄호 ')' 일 경우
   - 스택 top에 왼쪽 괄호 '(' 가 올때 까지 스택에 pop 연산 수행
   - pop한 연산자 출력
   - 왼쪽 괄호 만나면 pop만 함
5. 중위표기식에 더 읽을 것이 없다면 중지, 있다면 1부터 반복
6. 스택에 남아있는 연산자를 모두 pop하여 출력
   - 스택 밖의 왼쪽 괄호는 우선 순위 가장 높으며 
   - 스택 안의 왼쪽 괄호는 가장 낮음



### 후위표기법 수식을 연산하는 방법

1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고 결과를 다시 스택에 push
3. 수식이 끝나면 마지막으로 스택을 pop하여 출력



### eval()

> python 내장 함수



- 문자열로 된 수식을 계산하는 함수

- ```python
  eval("6+5*(2-8)/2")
  ```

- 위의 코드를 실행하면 문자열로 된 수식의 계산 결과를 반환함



### Backtracking

> 해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아가는 기법



- 어떤 노드가 유망하지 않으면 그 노드의 부모로 되돌아가 다음 자식 노드로 감
- 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않은 것이다.
- 반대로 해답의 가능성이 있으면 유망한 것이다.
- 가지치기(Pruning): 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않음



1. 미로 찾기
   - 입구와 출구가 주어진 미로에서 입구부터 출구까지 경로를 찾는 문제
   - 이동 방향은 4방향
   - 이동 상황을 스택에 push하면서 이동
   - 이동할 경로가 없어 막혔을 때 스택의 원소를 pop 하면서 이전에 지나간 경로를 다시 돌아가면서 이동 가능한 경로를 찾아감



2. n queen 문제

   > n*n 의 정사각형 안에 n개의 queen을 배치하는 문제
   >
   > 모든 queen은 자신의 일직선상과 대각선상에 아무 것도 놓이지 않아야 함

   ```python
   def checknode(v): # node
       if promising(v):
           if there is a solution at v:
               write the solution
           else:
               for u in each child of v:
                   checknode(u)
   ```

   - 이때 깊이 우선 탐색보다 백트래킹이 수행시간이 더 짧다



3. Power Set 문제

   > 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합
   >
   > 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2^n이 나옴

   - 백트래킹 기법으로 구하기

     - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때, True 또는 False값을 가지는 항목들로 구성된 n개의 리스트를 만드는 방법 이용

     - 리스트의 i번째 항목은 i번째 원소가 부분집합의 값인지 아닌지를 나타내는 값

     - ```python
       MAXCANDIDATES = 100
       NMAX = 100
       a = [0]*NMAX
       backtrack(a,0,3)
       
       def construct_candidates(a,k,input,c):
           c[0] = True
           c[1] = False
           return 2
       
       def backtrack(a,k,input):
           global MAXCANDIDATES
           c=[0]*MAXCANDIDATES
           
           if k==input:
               process_solution(a,k) #답이면 원하는 작업을 한다
           else:
               k+=1
               ncandidates = construct_candidates(a,k,input,c)
               for i in range(ncandidates):
                   a[k] = c[i]
                   backtrack(a,k,input)
       ```

   

4. 순열을 구하는 백트래킹 알고리즘

   - ```python
     MAXCANDIDATES = 100
     NMAX = 100
     a = [0]*NMAX
     backtrack(a,0,3)
     
     def construct_candidates(a,k,input,c):
         in_perm = [False]*NMAX
         
         for i in range(1,k):
             in_perm[a[i]]=True
         
         ncandidates = 0
         for i in range(1,input+1):
             if in_perm[i] == False:
                 c[ncandidates]=i
                 ncandidates += 1
         return ncandidates
     def backtrack(a,k,input):
         global MAXCANDIDATES
         c=[0]*MAXCANDIDATES
         
         if k==input:
             for i in range(1, k+1):
                 print(a[i], end=" ")
             print()
         else:
             k+=1
             ncandidates = construct_candidates(a,k,input,c)
             for i in range(ncandidates):
                 a[k] = c[i]
                 backtrack(a,k,input)
     ```



### 분할 정복 알고리즘

- 분할 : 문제를 여러개의 작은 부분으로 나눔
- 정복 : 나눈 문제를 각각 해결
- 통합 : 해결된 해답을 모음



1. 거듭 제곱 알고리즘 : O(log2n)

   - ```python
     def Power(Base, Exponent):
         if Exponent == 0 or Base == 0:
             return 1
         
         if Exponent % 2 == 0:
             NewBase = Power(Base, Exponent/2)
             return NewBase*NewBase
         else:
             NewBase = Power(Base, (Exponent-1)/2)
             return (NewBase*NewBase)*Base
     ```

2. 합병 정렬 & 퀵 정렬

   - 공통점

     - 주어진 리스트를 두 개로 분할하고 각각을 정렬

   - 차이점

     - 합병정렬

       - 분할할때 단순하게 두 부분으로 나눔
       - 각 부분 정렬이 끝난 후 '합병'이라는 후처리 작업이 필요

     - 퀵정렬

       - 분할할때 기준 아이템(Pivot Item)을 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴

       - 각 부분 정렬이 끝난 후 후처리작업이 필요하지 않음

       - ```python
         def quickSort(a,begin,end):
             if begin<end:
                 p = partition(a,begin,end)
                 quickSort(a,begin,p-1)
                 quickSort(a,p+1,end)
         ```

       - 주어진 리스트에서 피봇을 구하는 알고리즘

       - ```python
         def partition(a, begin, end):
             pivot = (begin+end)//2
             L=begin
             R=end
             while L<R:
                 while(a[L] < a[pivot] and L<R):
                     L += 1
                 while(a[R] >= a[pivot] and L<R):
                     R -= 1
                 if L<R:
                     if L==pivot:
                         pivot=R
                     a[L],a[R]=a[R],a[L]
             a[pivot],a[R] = a[R],a[pivot]
             return R
         ```

       - 시간복잡도 : O(n^2) - 최악, O(nlogn) - 평균