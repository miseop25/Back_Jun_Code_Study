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

def makeCompArray(lock) :
    N = len(lock)
    T = N*3
    result = [[0 for _ in range(T)] for _ in range(T)]
    for i in range(N,N+N) :
        for j in range(N,N+N) :
            result[i][j] = lock[i-(N)][j-(N)]
    return result

def unlock(key, comp, x, y) :
    result = copy.deepcopy(comp)
    for i in range(x, x + len(key)) :
        for j in range(y, y + len(key)) :
            result[i][j] += key[i-x][j-y]
    return result

def checkIsUnlock(array, N) :
    for i in range(N,N+N) :
        for j in range(N,N+N) :
            if array[i][j] != 1 :
                return False
    return True
            

def solution(key, lock):
    answer = True
    compArray = makeCompArray(lock)
    for _ in range(4) :
        for i in range(len(lock) -len(key) + 1, len(lock)*2 + 1): 
            for j in range(len(lock) -len(key) + 1, len(lock)*2 + 1):
                temp = unlock(key, compArray, i, j)
                answer = checkIsUnlock(temp, len(lock))
                if answer :
                    return answer
        key = rotate90(key)
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]] ))
# print(solution([[0,0,0,1], [0,0,0,1], [0,0,0,1],[0,0,0,1]],[[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0] ]  ) )
# print(rotate90([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))
# print(rotate90([[1,2,3], [4,5,6], [7,8,9]]))
