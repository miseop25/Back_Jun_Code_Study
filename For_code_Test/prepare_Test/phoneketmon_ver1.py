def solution(nums):
    answer = 0
    phoneketmon_list = []
    N = int(len(nums)/2)

    for i in nums :
        if i not in phoneketmon_list :
            phoneketmon_list.append(i)
            answer+=1
    if answer> N :
        answer = N
    
    return answer