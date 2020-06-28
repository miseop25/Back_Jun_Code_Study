import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    student = dict()
    for i in range(N) :
        temp = list(map(int, input().split()))
        student[i] = [temp, 0]
    
    grade = 1
    same = 1
    result = sorted(student.items(), key= lambda x: ( -x[1][0][0] , -x[1][0][1] ))
    student[result[0][0]][1] = grade
    tall = result[0][1][0][1]
    weight = result[0][1][0][0]
    for check in result[1:] :
        if check[1][0][0] < weight and check[1][0][1] < tall :
            if same == 1 :
                grade += 1
            else :
                grade += same
            student[check[0]][1] = grade 

            same = 1
        else :
            same += 1
            student[check[0]][1] = grade 
        weight = check[1][0][0]
        tall = check[1][0][1]

    answer = []
    for i in range(N) :
        answer.append(str(student[i][1]))
    print(" ".join(answer))

