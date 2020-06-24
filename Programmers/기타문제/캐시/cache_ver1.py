def solution(cacheSize, cities):
    answer = 0
    memory = dict()
    if cacheSize == 0 :
        return len(cities)*5
    for i in range(len(cities)) :
        temp = cities[i].lower()
        if temp in memory :
            memory[temp] = i
            answer += 1
        else :
            if len(memory) < cacheSize :
                memory[temp] = i
            else :
                lru = sorted(memory.items(), key= lambda x: x[1])
                memory.pop(lru[0][0])
                memory[temp] = i
            answer += 5

    return answer

print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] ))