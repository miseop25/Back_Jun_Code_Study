import sys
input=sys.stdin.readline
 
if __name__ == "__main__":
    arr = []
    for i in range(int(input())):
        age, name = input().split()
        arr.append([int(age), name, i])
    arr.sort(key = lambda x: (x[0], x[2]))
    for age, name, pre in arr:
        print(age,name)
