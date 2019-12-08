answer = 0
a = input()


for i in a :
    asc_code = ord(i) 
    if asc_code >= 65 and asc_code <68 :
        answer += 3 
    elif asc_code >=68 and asc_code< 71:
        answer += 4
    elif asc_code >=71 and asc_code< 74:
        answer += 5
    elif asc_code >=74 and asc_code< 77:
        answer += 6
    elif asc_code >=77 and asc_code< 80:
        answer += 7
    elif asc_code >=80 and asc_code< 84:
        answer += 8
    elif asc_code >=84 and asc_code< 87:
        answer += 9
    elif asc_code >=87 and asc_code< 91:
        answer += 10
    
print(answer)

