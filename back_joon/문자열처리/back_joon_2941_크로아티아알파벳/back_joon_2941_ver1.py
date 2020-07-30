import sys
input = sys.stdin.readline

if __name__ == "__main__":
    word = input().rstrip()
    answer = 0
    array = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    for i in array :
        word = word.replace(i, "O")
    print(len(word))
