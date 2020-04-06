A = int(input())
B = int(input())
C = int(input())

num_str = str(A*B*C)
number_dict = dict()
for i in range(10) :
    number_dict[i] = 0

for check in num_str :
    number_dict[int(check)] += 1

for k in number_dict.values() :
    print(k)