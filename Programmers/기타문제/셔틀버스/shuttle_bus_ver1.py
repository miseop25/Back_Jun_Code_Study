import collections
def solution(n, t, m, timetable):
    answer = ''
    ans_time = 540
    bus_time = 540
    table_dict = dict()
    for i in timetable :
        hour, mins = map(int, i.split(":"))
        if hour in table_dict :
            table_dict[hour].append(hour*60 + mins)
        else : 
            table_dict[hour] = collections.deque([hour*60 + mins])
    
    while n > 1 :
        seat = m 
        for i in range(bus_time//60 + 1) :
            if i in table_dict :
                table_dict[i] = collections.deque(sorted(table_dict[i]))
                cnt = 0
                max_cnt = len(table_dict[i])
                while table_dict[i] and cnt < max_cnt:
                    if seat == 0 :
                        break
                    if table_dict[i][0] <= bus_time :
                        seat -= 1
                        table_dict[i].popleft()
                    cnt += 1
            if seat == 0 :
                break
        bus_time += t 
        n -= 1


    seat = m
    for i in range(bus_time//60 + 1 ) :
        if i in table_dict :
            table_dict[i] = collections.deque(sorted(table_dict[i]))
            cnt = 0
            max_cnt = len(table_dict[i])
            while table_dict[i] and cnt <= max_cnt:
                if seat == 1 :
                    if table_dict[i][0] == ans_time :
                        ans_time -= 1
                    if m == 1 :
                        if table_dict[i] :
                            if table_dict[i][0] <= ans_time :
                                ans_time = table_dict[i][0] - 1
                    break
                if table_dict[i][0] <= bus_time :
                    seat -= 1
                    ans_time = table_dict[i].popleft()
                cnt += 1
    
            if not table_dict[i] :
                ans_time = bus_time
        if seat != 1 :
            ans_time = bus_time

    if ans_time >= 1440 :
        ans_time = ans_time - 1440

    hour, mins = divmod(ans_time, 60)
    if hour < 10 :
        str_h = "0" + str(hour)
    else : 
        str_h = str(hour)
    if mins < 10 :
        str_m = "0" + str(mins)
    else :
        str_m = str(mins)
    answer = str_h + ":" + str_m
    return answer

# print(solution(17,60,11,["24:00","24:00","24:00","24:00","24:00","24:00","24:00","24:00","24:00","24:00"]))
print(solution(1,1,1,["00:01"]))