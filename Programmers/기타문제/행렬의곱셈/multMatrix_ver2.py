def solution(arr1, arr2):
    answer = []
    y = len(arr1)
    x = len(arr2[0])

    for i in range(y) :
        answer.append([])
        for j in range(x) :
            value = 0
            for k in range(x) :
                value += arr1[i][k]*arr2[k][j]
            answer[i].append(value)

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))