def solution(n, build_frame):
    answer = [[]]


    for i in range(len(build_frame)):
        answer[i].append(build_frame[i][0]) 
        answer[i].append(build_frame[i][1]) 
        answer[i].append(build_frame[i][2]) 

        
    return answer