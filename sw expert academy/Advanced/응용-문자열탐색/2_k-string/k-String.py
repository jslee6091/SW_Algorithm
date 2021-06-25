import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    K = int(input())
    word = input()

    backtracking = [0 for _ in range(len(word))]
    substring = []
