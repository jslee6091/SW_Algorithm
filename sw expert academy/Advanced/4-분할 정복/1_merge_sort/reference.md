### 참고 코드

> https://hongsj36.github.io/2020/01/30/Ad_DivideAndConquer/



```python
def merge(lst):
    cnt = 0
    len_lst = len(lst)
    if len_lst <= 1:
        return lst, cnt
    else:
        #분리
        left, left_cnt = merge(lst[ : len_lst//2])
        right, right_cnt = merge(lst[len_lst//2 : ])
        
        #리스트 병합
        my_lst = [] # 리턴 할 리스트
        left_idx = right_idx = 0 # 좌우측 인덱스
        right_is_small = False
        for _ in range(len_lst):
            if left_idx == len(left): # 좌측 리스트가 먼저 동났을 때
                my_lst.append(right[right_idx]) # 우측 리스트에서 가져옴
                right_idx += 1
                
            elif right_idx == len(right): # 우측 리스트가 먼저 동났을 때
                my_lst.append(left[left_idx]) # 좌측 리스트에서 가져옴
                left_idx += 1
                right_is_small = True # 오른쪽 마지막 원소가 작은 경우

            elif left[left_idx] <= right[right_idx]: # 좌측 리스트의 값이 작을 때
                my_lst.append(left[left_idx])  # 좌측 리스트에서 가져옴
                left_idx += 1

            else: # 우측 리스트의 값이 작을 때
                my_lst.append(right[right_idx]) # 우측 리스트에서 가져옴
                right_idx += 1
        
        #cnt 계산
        cnt = left_cnt + right_cnt
        if right_is_small: # 오른쪽 마지막 원소가 작은 경우
            cnt += 1

        return my_lst, cnt

def sorted_merge(lst):
    sorted_lst, cnt = merge(lst)
    return sorted_lst[N//2], cnt

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print('#{}'.format(test_case), *sorted_merge(lst))
```



### 의문점

- 내가 만든 코드는 실행 시간 초과로 실패했는데 이 코드는 왜 성공했는지 잘 모르겠다.
- 알고리즘이 비슷한 것 같은데 좀 더 공부를 해봐야 할 것 같다.