if __name__ == "__main__":
    word = input().rstrip()
    alpa = ['0']*26
    for i in word :
        alpa[ord(i)- 97] = str(int(alpa[ord(i)- 97]) + 1)
    answer = " ".join(alpa)
    print(answer)

    