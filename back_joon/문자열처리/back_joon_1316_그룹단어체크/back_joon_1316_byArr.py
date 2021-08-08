import sys
input = sys.stdin.readline

def GroupWordCheck(word) -> bool :
    alpa  = [-1 for _ in range(26)] #알파벳 a~z 까지, 해당 칸에는 인덱스가 들어갈 예정 
    for i, v in enumerate(word) :   #이게 어제 설명해 주었던 인덱스와 값 둘다 불러올 수 있는 것 
        ordAlpa = ord(v) - 97 # 아스키 코드로 바꾸어서 바로 배열 인덱스로 접근 가능할 수 있도록!, (a:97) - 97 = 0 , 바로 alpa 인덱스에 접근 가능 
        if alpa[ordAlpa] == -1 : # 처음 나오는거다 -> 현재 인덱스 바로 입력
            alpa[ordAlpa] = i 
            continue
        else :
            if alpa[ordAlpa] == (i-1) : #인덱스가 전에거랑 같다! (연속되어 있다는 소리임)
                alpa[ordAlpa] = i # 다시 해당 알파벳의 인덱스는 현재 인덱스로 최신화 
            else :
                return False #알파벡 인덱스가 이미 -1 이 아닌데 연속되지 않는다는건 이미 이전에 한번 나왔다는 소리!
    
    return True 

if __name__ == "__main__" :
    n = int(input().rstrip())
    answer = 0
    for _ in range(n) :
        if GroupWordCheck(input().rstrip()) :
            answer += 1
    print(answer)

