import sys
input = sys.stdin.readline

def soluction(num_list) :
    answer = 0
    ans_list = []
    cnt = 1
    stack = []
    buf = num_list[0]
    i = 0
    for i in range(1, len(num_list)) :
        if (num_list[i] - buf) == 1 :
            cnt += 1
            if cnt == 5 :
                break
        else :
            stack.append([i-1, cnt])
            cnt = 1
        buf = num_list[i]
    
    if cnt == 5 :
        return answer
    else :
        stack.append([i, cnt])
        stack = sorted(stack, key=lambda x: x[1])
        ans_list.append(5 - stack[0][1])
        # 지금 이 방식은 이어진 수가 계속되고 그 다음 값이 매우 클때 적용하는 방식이다.
        # 즉 1, 2, 4, 5 일때 1이 아니라 3을 출력하게 된다.
        stack = sorted(stack, key=lambda x: x[0])
        for i in stack :
            index = i[0]
            check = 0
            buf_cnt = i[1]

            try :
                check = num_list[index + 1] - num_list[index] - 1 
                if check >= 5 :
                        check = 5 - buf_cnt
                buf_cnt += check
                buf_num = num_list[index] + check
                while buf_cnt < 5: 
                    if num_list[index + 1] - buf_num == 1 :
                        buf_cnt += 1
                        index += 1
                        buf_num = num_list[index]
                    else :
                        check += num_list[index + 1] - buf_num - 1 
                        if check >= 5 :
                            check = 5 - buf_cnt
                        buf_cnt += check
                        buf_num = num_list[index] + check
                        index += 1
                a = True
            except :
                a = False
                
            if a :
                ans_list.append(check)
            else :
                ans_list.append(5-buf_cnt)

        return min(ans_list)


N = int(input())
num = []
for _ in range(N) :
    num.append(int(input()))
num = sorted(num)

print(soluction(num))