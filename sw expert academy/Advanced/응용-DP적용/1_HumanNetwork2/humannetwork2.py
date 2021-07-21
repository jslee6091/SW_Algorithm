import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    personInfo = list(map(int, input().split()))
    N = personInfo.pop(0)
    personMatrix = []
    for idx, var in enumerate(personInfo):
        if idx % N == 0:
            temp = []
            for j in range(N):
                temp.append(personInfo[idx + j])
            
            personMatrix.append(temp)
    
    
