import collections


koong = [1,2,4,8]
deq_buf = collections.deque([1,2,4,8])

for i in range(64) :
    buf = sum(deq_buf)
    koong.append(buf)
    deq_buf.popleft()
    deq_buf.append(buf)

N = int(input())

for i in range(N) :
    k = int(input())
    if k < 2 :
        print(koong[0])
    else :
        print(koong[k-1])
