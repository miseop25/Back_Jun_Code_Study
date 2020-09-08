import numpy
def solution(arr1, arr2):
    answer = []
    result = numpy.matmul(arr1, arr2)
    for i in result :
        answer.append(list(i))

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))