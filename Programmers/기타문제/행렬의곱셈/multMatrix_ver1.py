import numpy
def solution(arr1, arr2):
    answer = []
    result = numpy.matmul(arr1, arr2)
    for i in result :
        answer.append(list(i))
    # for value in arr1 :
    #     temp = []
    #     for i in range(len(value)) :
    #         buf = 0
    #         for j in range(len(value)) :
    #             buf += value[j]*arr2[j][i]
    #         temp.append(buf)
    #     answer.append(temp)

    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))