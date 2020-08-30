import copy
def rotate90(array) :
    lentgh = len(array)
    result = []
    for _ in range(lentgh) :
        result.append([])
    for i in range(lentgh-1, -1, -1) :
        j = 0
        for c in array[i] :
            result[j].append(c)
            j += 1
    return result

def makeCompArray(key, lock) :
    N = len(lock)
    M = len(key)
    T = N + 2*M - 2 
    result = [[0 for _ in range(T)] for _ in range(T)]
    for i in range(M-1, M+N - 1) :
        for j in range(M-1, M+N - 1) :
            result[i][j] = lock[i-(N-1)][j-(N-1)]
    return result

def unlock(key, comp, x, y) :
    result = copy.deepcopy(comp)
    for i in range(x, x + len(key)) :
        for j in range(y, y + len(key)) :
            result[i][j] += key[i-x][j-y]
    return result

def checkIsUnlock(array, N, M) :
    for i in range(M-1, M+N - 1) :
        for j in range(M-1,M+N - 1) :
            if array[i][j] != 1 :
                return False
    return True
            

def solution(key, lock):
    answer = True
    sums = 0
    for i in lock :
        sums += sum(i)
    if sums == len(lock)*len(lock) : return True
    #  모두 1 인경우 True를 리턴
    compArray = makeCompArray(key, lock)
    for _ in range(4) :
        for i in range(len(key)+len(lock) - 1): 
            for j in range(len(key)+len(lock) - 1):
                temp = unlock(key, compArray, i, j)
                answer = checkIsUnlock(temp, len(lock), len(key))
                if answer :
                    return answer
        key = rotate90(key)
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]] ))
# print(solution([[0,0,0,1], [0,0,0,1], [0,0,0,1],[0,0,0,1]],[[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0] ]  ) )
# print(rotate90([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))
# print(rotate90([[1,2,3], [4,5,6], [7,8,9]]))
