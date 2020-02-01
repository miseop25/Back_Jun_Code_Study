# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    c = str(bin(A*B))
    answer = c[2:]
    cnt = 0
    for i in answer :
        if i == '1' :
            cnt +=1
    return cnt
    
print(solution(3,7))