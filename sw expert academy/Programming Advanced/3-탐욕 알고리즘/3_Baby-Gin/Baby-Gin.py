import sys
sys.stdin = open("Baby-Gin_inputs.txt", 'r')

# Baby-Gin 문제 - 입력 받은 숫자들 중 연속으로 3개의 숫자가 나오거나(run), 같은 숫자가 3개 이상 나오는지(triplet) 검사하는 문제
T = int(input())


def run_or_triplet(array):
    # triplet 검사
    if 3 in array:
        return 1
    
    # run 검사
    for i in range(8):
        if array[i] >= 1 and array[i+1] >= 1 and array[i+2] >= 1:
            return 1
    
    # triplet, run 모두 아니면 0 return
    return 0

for test_case in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1 = [0 for _ in range(10)]
    player2 = [0 for _ in range(10)]
    answer = 0

    for idx, num in enumerate(cards):
        
        if idx % 2 == 0:
            player1[num] += 1
            # player1 의 run, triplet 검사
            if run_or_triplet(player1):
                answer = 1
                break
        else:
            player2[num] += 1
            # player2 의 run, triplet 검사
            if run_or_triplet(player2):
                answer = 2
                break
    
    print(f'#{test_case} {answer}')
