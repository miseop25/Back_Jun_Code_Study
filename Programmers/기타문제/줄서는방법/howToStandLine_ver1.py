import itertools
def solution(n, k):
    answer = []
    result = list(itertools.permutations([str(i) for i in range(1, n+1)], n))
    temp = []
    for i in result :
        temp.append(''.join(i))
    temp = sorted(temp)
    for i in temp[k-1] :
        answer.append(int(i))
    return answer


print(solution(4,10))