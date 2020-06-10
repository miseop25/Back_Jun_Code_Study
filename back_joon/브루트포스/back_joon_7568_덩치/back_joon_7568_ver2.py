import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    student = dict()
    for i in range(N) :
        temp = list(map(int, input().split()))
        student[i] = [temp, 0]
    
    grade = 1
    same = 0
    result = sorted(student.items(), key= lambda x: -x[1][0][0] )
    tall = 0
    weight = 0
    for i in range(N) :

        weight = result[i][1][0][0]
        tall = result[i][1][0][1]
        same = 0
        if student[result[i][0]][1] > 0 :
            continue
        for j in result[i+1 :] :
            if student[j[0]][1] != 0 :
                continue
            if weight <= j[1][0][0] or tall <= j[1][0][1] :
                student[j[0]][1] = grade
                same += 1
        student[result[i][0]][1] = grade
        grade += same + 1
    
    answer = []
    for i in range(N) :
        answer.append(str(student[i][1]))
    print(" ".join(answer))
