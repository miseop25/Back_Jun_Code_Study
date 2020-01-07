while True :
    buf = input()
    stack = []
    cnt = 0
    if buf == '.' :
        break

    for i in buf :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' or i == ']' :
            try :
                check = stack.pop()
            except :
                cnt = -1 
                break


            if check == '(' and i == ')':
                cnt = 0
            elif check =='[' and i == ']' :
                cnt =0 
            else :
                cnt = -1
                break

    if stack :
        cnt = -1

    if cnt == 0 :
        print('yes')
    else :
        print('no')



