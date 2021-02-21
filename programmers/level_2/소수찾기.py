from itertools import permutations


def prime_number(num_case):
    total_count = 0
    for n in num_case:
        count = 0
        for nn in range(2, n):
            if n%nn == 0:
                count += 1
                break
        if count == 0 and n > 1:
            total_count += 1
    return total_count


def solution(numbers):
    num_case = []
    for i in range(1, len(numbers)+1):
        perm = permutations(numbers, i)
        for num in perm:
            new_str = "".join(num)
            num_case.append(int(new_str))
    num_case = list(set(num_case))
    answer = prime_number(num_case)
    return answer


inputs = ['17', '011']
for i in inputs:
    primes = solution(i)
    print(primes)
