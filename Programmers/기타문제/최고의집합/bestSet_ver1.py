import itertools
def solution(n, s):
    answer = []
    num = [i for i in range(1, s)]
    num = num * n
    example = list(itertools.combinations(num, n))
    for i in example :
        if sum(i) != s :
            continue
        mult = 1
        for j in i :
            mult *= j
        answer.append([mult, i])
    answer = sorted(answer, key= lambda x: -x[0])
    return answer[0]

print(solution(4,18))
print(solution(2,9))