def solution(k, room_number):
    hotel = dict()
    answer = []
    for i in range(k) :
        hotel[i+1] = 0
    for i in room_number :
        if hotel[i] == 0 :
            hotel[i] = 1
            answer.append(i)
        else :
            buf = i +1
            while True :
                if hotel[buf] == 0 :
                    hotel[buf] = 1
                    answer.append(buf)
                    break
                else :
                    buf = buf +1
    return answer