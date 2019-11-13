def change_date(date) :
    month_31_list = [1,3,4,7,8,10,12]
    year = date[0:4]
    month = date[4:6]
    month_int = int(month)
    day = (date[6:8])
    day_int = int(day)
    if month_int < 1 or month_int >12 :
        return -1 
    elif month_int in month_31_list :
        if day_int <1 or day_int >31 :
            return -1
    else :
        if month_int == 2 :
            if day_int < 1 or day_int > 29 :
                return -1
        elif day_int < 1 or day_int >30 :
            return -1
    answer = str(year) + '/' + str(month) + '/' + str(day)
    return answer





N = int(input())
for i in range(N) :
    date = input()
    buf = change_date(date)
    answer = '#' + str(i+1) + ' ' + str(buf)
    print(answer)



