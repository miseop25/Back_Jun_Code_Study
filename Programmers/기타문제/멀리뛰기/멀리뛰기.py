def solution(n):
    arr = [1,2]
    if n <=2 :
        return arr[n-1]
    for i in range(1 , n-1) :
        temp = arr[i] + arr[i-1]
        arr.append(temp)
    return arr[-1]%1234567


print(solution(6))