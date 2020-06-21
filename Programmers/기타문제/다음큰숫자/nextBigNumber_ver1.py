def solution(n):
    oneLen = str(bin(n)).count("1")
    while True :
        n += 1 
        if oneLen == str(bin(n)).count("1") :
            return n 