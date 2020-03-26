import sys
input = sys.stdin.readline
string = str(input())
stack = []
brackets_stack = []
answer = ""

def save_to_stack() :
    buf = ""
    while stack :
        buf += stack.pop()
    return buf

for i in range(len(string)) :
    if string[i] == "<" :
        if stack :
            a = save_to_stack()
            answer += a
        brackets_stack.append(i)
        continue
    elif string[i] == ">" :
        index = brackets_stack.pop()
        answer += string[index : i+1]
        continue
    if brackets_stack :
        continue
    if string[i] == " ":
        a = save_to_stack()
        answer += a + " "
    elif string[i] == "\n" :
        continue
    else :
        stack.append(string[i])

a = save_to_stack()
answer += a
print(answer)