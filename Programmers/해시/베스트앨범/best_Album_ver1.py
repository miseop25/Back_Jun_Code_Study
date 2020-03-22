def solution(genres, plays):
    answer = []
    genres_dict = dict()
    plays_dict = dict()
    for i in range(len(genres)) :
        if genres[i] in genres_dict :
            genres_dict[genres[i]].append(i)
            plays_dict[genres[i]] += plays[i]
        else :
            genres_dict[genres[i]] = [i]
            plays_dict[genres[i]] = plays[i]
    
    sort_play = sorted(plays_dict.items(), key=(lambda x: x[1]), reverse= True)

    for i in sort_play :
        buf = genres_dict[i[0]]
        result_dict = dict()
        for j in buf :
            result_dict[j] = plays[j]
        result_sort = sorted(result_dict.items(), key=(lambda x: x[1]), reverse= True)
        for k in range(2) :
            try :
                answer.append(result_sort[k][0])
            except :
                pass
    
    return answer




print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))