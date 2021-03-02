### 순차 검색

- 정렬되지 않은 자료의 순차 검색

- ```c
  sequentialSearch(a[], n, key)
  	i <- 0;
  	while(i<n and a[i]!=key) do{
          i <- i + 1;
      }
  	if (i<n) then return i;
  	else return -1;
  end sequentialSearch();
  ```

- 시간복잡도 : O(n)



- 정렬된 자료의 순차 검색(오름차순 일때)

- ```c
  sequentialSearch(a[], n, key)
  	i <- 0;
  	while(a[i]<key) do{
          i <- i + 1;
      }
  	if (a[i]=key) then return i;
  	else return -1;
  end sequentialSearch();
  ```

- 시간복잡도: O(n)





### 이진 검색

```c
# example code
binarySearch(a[], key)
    start <- 0, end <- length(a)-1;
	while(start <= end){
        	middle = start + (end-start)/2;
        	if(a[middle] == key){
                return true;
            }
        	else if (a[middle] > key){
                end = middle - 1;
            }
        	else start = middle + 1;
    }
	return false;
end binarySearch();
```

```c
# 재귀 함수 이용
binarySearch(a[], low, high, key)
    middle <- (low+high)/2;
	if (key = a[middle]) then
        return true;
	else if (key < a[middle]) then
        binarySearch(a[], low, middle-1, key);
	else if (key > a[middle]) then
        binarySearch(a[], middle+1, high, key);
	else
        return false;
end binarySearch();
```





### Array 순회

> 지그재그 순회

```c
int i;
int j;

for i from 0 to n-1
    for j from 0 to m-1
        Array[i][j+(m-1-2*j)*(i%2)];
```

