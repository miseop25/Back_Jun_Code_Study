import itertools
def solution(numbers):
    answer = set()
    result = itertools.combinations(numbers, 2)
    for i in result :
        answer.add(sum(i))
    answer = list(sorted(answer))
    return answer