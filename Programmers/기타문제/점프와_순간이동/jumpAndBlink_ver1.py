def solution(n):
    ans = 0
    n, r = divmod(n,2)
    ans += r
    while n != 0 :
        n, r = divmod(n,2)
        ans += r
    return ans