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
    print(result)
    tall = 0
    weight = 0
    for i in range(N) :
        if i == 0 :
            weight = result[i][1][0][0]
            tall = result[i][1][0][1]
            continue
        if weight > result[i][1][0][0] and tall > result[i][1][0][1] :
            student[result[i-1][0]][1] = grade 
            grade += 1 + same
            same = 0
        else :
            student[result[i-1][0]][1] = grade
            same += 1
        weight = result[i][1][0][0]
        tall = result[i][1][0][1]
    student[result[i][0]][1] = grade
    
    answer = []
    for i in range(N) :
        answer.append(str(student[i][1]))
    print(" ".join(answer))
