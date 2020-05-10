import itertools

def calculating(x, y, op) :
    if op == "+":
        return x + y
    elif op == "-" :
        return x - y
    elif op == "*" :
        return x*y
    elif op == "/" :
        if x < 0 :
            return -(abs(x)//y)
        else :
            return x // y


N = int(input())
num = list(map(int, input().split(" ")))
op_num = list(map(int, input().split(" ")))
operator = []
#  +, -, *, / 
for _ in range(op_num[0]) :
    operator.append("+")
for _ in range(op_num[1] ):
    operator.append("-")
for _ in range(op_num[2]) :
    operator.append("*")
for _ in range(op_num[3] ):
    operator.append("/")

op_case = set((itertools.permutations(operator,N-1)))
print(len(op_case))
ans_set = set()
for case in op_case :
    buf = num[0]
    for i in range(1,len(num)) :
        buf = calculating(buf, num[i], case[i-1])
    ans_set.add(buf)

print(max(ans_set))
print(min(ans_set))
    




