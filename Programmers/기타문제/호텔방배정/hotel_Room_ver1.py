def solution(k, room_number):
    selected = set()
    for i in range(1, k+1) :
        selected.add(i)
    result = []
    for i in room_number :
        if i in selected :
            selected.remove(i)
            result.append(i)
        else :
            temp = sorted(selected, key= lambda x: x if x > i else 10**12)
            result.append(temp[0])
            selected.remove(temp[0])

    return result

print(solution(10**12, [1,2,3,4,45,3]))