import collections

def solution(input):
    answer = True
    turn_deq = collections.deque()
    stack_deq = collections.deque()

    for i in input :
        if i =='['or i == '{' or i == '(':
            stack_deq.append(i)

        elif i ==']'or i == '}' or i == ')': 
            try :
                buf = ord(stack_deq.pop())
            except :
                return False

            
            if buf == (ord(i)-2) or buf == (ord(i) - 1) :
                if i ==']' :
                    for j in stack_deq :
                        if j == '(' or j == '{' or j == '[':
                            return False
                elif i == '}' :
                    for j in stack_deq :
                        if j == '(' or j == '{':
                            return False

                
            else :
                return False

    return answer