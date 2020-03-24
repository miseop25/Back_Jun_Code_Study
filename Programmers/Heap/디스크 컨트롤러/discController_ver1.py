import collections

def solution(jobs):
    answer = 0
    jobs = collections.deque(sorted(jobs , key= lambda x: x[1] ))
    print(jobs)
    time = 0
    check = False
    working = []
    ans_list = []

    while jobs :
        if not (working) :
            for _ in range(len(jobs)) :
                temp, buf = jobs.popleft()
                if temp <= time :
                    ans_list.append(time - temp + buf)
                    working.append(buf)
                    check = True
                    break
                else :
                    jobs.append([temp, buf])
            if check :
                jobs = collections.deque(sorted(jobs , key= lambda x: x[1] ))
                check = False
            else :
                time += 1

        else :
            time += working.pop()
    answer = int(sum(ans_list)/len(ans_list))
        
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))
