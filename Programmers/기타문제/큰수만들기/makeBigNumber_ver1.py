import itertools

def solution(number, k):
    n = len(number) - k
    num = [i for i in number]
    result = list(map(''.join,  itertools.combinations(num, n)))
    answer = max(result)
    return answer

print(solution("1231234", 3))