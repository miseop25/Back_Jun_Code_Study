def solution(key, lock):
    sum_key = 0
    sum_lock = 0
    for i in range(len(key)) :
        sum_key += sum(key[i])
    for i in range(len(lock)) :
        sum_lock += sum(lock[i])
    
    if sum_key > sum_lock :
        return False



    answer = True
    return answer