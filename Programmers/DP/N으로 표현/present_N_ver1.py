def solution(N, number):
    first = [int(str(N)+str(N)), N*N, N//N, N+N]
    if N == number :
        return 1
    elif number in first :
        return 2

    for i in range(3, 9):
        num_list = []
        for j in first :
            num_list.append(int(str(j)+str(N)))
            num_list.append(j*N)
            num_list.append(j//N)
            num_list.append(j+N)
            num_list.append(j-N)
        num_list = list(set(num_list))
        if number in num_list :
            return i
        else :
            first = num_list.copy()

    return -1


print(solution(3,4))