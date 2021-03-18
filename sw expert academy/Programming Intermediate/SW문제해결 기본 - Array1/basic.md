### 순열

- {1,2,3}을 포함하는 모든 순열

- ```python
  # 동일한 숫자가 포함되지 않았을 때 각 자리수별 loop을 이용
  for i1 from 1 to 3
  	for i2 from 1 to 3
      	if i2 != i1 then
          	for i3 from 1 to 3
              	if i3 != i1 and i3 != i2 then
                  	print i1, i2, i3
                  end if
              end for
          end if
      end for
  end for
  ```

- 



### Greedy Algorithm

> 탐욕적 알고리즘



- Baby-gin 문제 해결책

- ```python
  # pseudo code
  i <- 0, inp <- 0, tri <- 0, run <- 0;
  
  input_6_numbers # 입력 받은 6자리수
  c[12] <- {0,}; # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 Array
  while(i<6){
      c[inp%10] <- c[inp%10]+1;
      inp <- inp/10; i <- i+1;
  }
  i<-0;
  while(i < 10){
      if(c[i]>=3){
          c[i] <- c[i]-3; tri <- tri+1;
          continue;
      }
      if(c[i]>=1 and c[i+1]>=1 and c[i+2]>=1){
          c[i] <- c[i]-1;
          c[i+1] <- c[i+1]-1;
          c[i+2] <- c[i+2]-1;
          run <- run+1;
          continue;
      }
      i <- i+1;
  }
  if(run+tri==2)
  	print("baby gin")
  else
  	print("lose")
  ```

- 