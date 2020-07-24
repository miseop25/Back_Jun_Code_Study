def solution(lines):
    answer = []

    start = []
    end = []
    for i in lines :
        d, t, w = i.split(" ")
        w = w[: -1]
        h, m, s = t.split(":")
        st = (int(h)*360 + int(m)*60 ) + float(s)
        ed = st + float(w) - 0.001
        start.append(st)
        end.append(ed)
    start.sort()
    end.sort()
    for i, val in enumerate(end) :
        comp = val + 1
        cnt = 1
        for j in range(i+1, len(start)) :
            if (start[j] <= comp or end[j] <= comp )and end[j] >= val :
                cnt += 1
            else :
                break
        answer.append(cnt)





    return max(answer)

a = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(a))