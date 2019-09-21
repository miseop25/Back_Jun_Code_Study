import operator


def solution(priorities, location):
    ans_key = priorities[location]
    ans_dict = {ans_key : location}
    cnt = 1
    while priorities :
        max_index, max_value = max(enumerate(priorities), key=operator.itemgetter(1))
        print(priorities)

        print(ans_dict)
        if max_index == 0 : 
            if max_index == ans_dict[ans_key] :
                return cnt
            priorities.pop(0)
            ans_dict[ans_key] -=1
            cnt +=1
        else :
            if priorities[0] == ans_key and ans_dict[ans_key] == 0 :
                buf = priorities.pop(0)
                priorities.append(buf)
                ans_dict[ans_key] = len(priorities)-1
            else : 
                buf = priorities.pop(0)
                priorities.append(buf)
                ans_dict[ans_key] -=1
    return cnt
