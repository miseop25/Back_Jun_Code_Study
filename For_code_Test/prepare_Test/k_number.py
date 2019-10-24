def solution(array, commands):
    answer = []
    for i in commands :
        buf_list = array[ i[0]-1 : i[1] ]
        buf_list.sort()
        print(buf_list)
        answer.append(buf_list[i[2]-1])

    return answer