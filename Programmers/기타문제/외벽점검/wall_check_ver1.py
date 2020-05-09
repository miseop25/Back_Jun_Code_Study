def solution(n, weak, dist):
    answer = 0
    left = []
    right = []
    for i in range(len(weak)) :
        left.append(weak[i] - n)
        right.append(n + weak[i])
    weak = left + weak + right
    print(weak)

    result_dict = dict()
    for i in dist :
        buf_dict = dict()
        for j in range(len(weak) - 1) :
            cnt = 1
            temp = []
            if weak[j] < 0 :
                temp = [weak[j] + n]
            elif weak[j] > n :
                temp = [weak[j] - n]
            else :
                temp = [weak[j]]
            for k in weak[j+1 :] :
                if abs(weak[j] - k) <= i :
                    cnt += 1
                    if k < 0 :
                        temp.append(k + n)
                    elif k > n :
                        temp.append(k - n)
                    else :
                        temp.append(k)
                else :
                    if cnt in buf_dict :
                        buf_dict[cnt].append(sorted(temp))
                    else :
                        buf_dict[cnt] = [sorted(temp)]
                    break
        max_i = list(sorted(buf_dict.items(), key= lambda x: -x[0]))
        item = max_i[0][1]
        item  = list(set([tuple(set(item) ) for item in item ]))
        result_dict[i] = [ max_i[0][0] , item]
    print(result_dict)
    return answer


print(solution(12, [1,5,6,10], [1,2,3,4]))