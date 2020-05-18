import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, C = map(int, input().split(" "))
    num = list(map(int, input().split(" ")) )
    num_dict = dict()
    for i in range(N) :
        if num[i] in num_dict :
            num_dict[num[i]][0] += 1
        else :
            num_dict[num[i]] = [1, i]
    
    result = sorted(num_dict.items(), key= lambda x: (-x[1][0], x[1][1] ))
    answer = []
    for i in result :
        for j in range(i[1][0]) :
            answer.append(str(i[0]))
    print(" ".join(answer))
        

