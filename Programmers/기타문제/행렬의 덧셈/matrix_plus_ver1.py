def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        answer.append([])
        for j in range(len(arr1[0])) :
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer


solution([[1],[2]], [[3],[4]])