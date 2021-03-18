import sys
sys.stdin = open("Bracket_Matching_inputs.txt", 'r')


for test_case in range(1, 11):
    length = int(input())
    brackets = input()
    num_stack = []
    answer = 1

    for st in brackets:
        if st == '<' or st == '(' or st == '{' or st == '[':
            num_stack.append(st)
        else:
            check = num_stack.pop()
            if check == '<' and st != '>':
                answer = 0
                break

            elif check == '(' and st != ')':
                answer = 0
                break

            elif check == '{' and st != '}':
                answer = 0
                break

            elif check == '[' and st != ']':
                answer = 0
                break

    if len(num_stack) != 0:
        answer = 0

    print(f'#{test_case} {answer}')
