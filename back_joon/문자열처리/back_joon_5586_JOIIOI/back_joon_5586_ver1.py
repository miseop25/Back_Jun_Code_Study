if __name__ == "__main__":
    word = input()
    joi = 0
    ioi = 0
    for i in range(len(word) - 2) :
        if word[i : i+3] == "JOI" :
            joi += 1
        if word[i : i+3] == "IOI" :
            ioi += 1
    print(joi)
    print(ioi)