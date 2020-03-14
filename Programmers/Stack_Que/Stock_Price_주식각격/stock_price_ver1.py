import collections

def solution(prices):
    answer = []
    prices = collections.deque(prices)
    while prices :
        buf = prices.popleft()
        cnt = 0
        for i in prices :
            if i < buf :
                cnt +=1
                break
            else :
                cnt += 1
        answer.append(cnt)

    return answer

print(solution([1,2,3,2,3]))
