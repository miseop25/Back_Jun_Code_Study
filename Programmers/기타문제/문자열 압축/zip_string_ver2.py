def solution(s):
    answer = 0
    ans_list = [len(s)]

    #  입축할 수 있는 최대 길이는 문자열 길이의 1/2 임
    for w in range(1, len(s)//2 + 1) :
        #  초기 비교한 문자열 저장
        temp = s[:w]
        cnt = 1
        buf = ""
        i = w 
        while i < len(s) :

            #  i + w 가 문자열보다 길 경우 하나씩 넣어주는 작업 진행
            if i + w > len(s) :
                buf += s[i]
                i += 1
            else :
                #  앞뒤가 같으면 cnt 값 하나씩 증가, i 값은 w 값 증가시킴
                if temp == s[i:i+w] :
                    cnt += 1
                    i = i + w
                else :
                    # 앞뒤가 일치해서 cnt 값이 1 이상인 경우 cnt 값 까지 포함해서 문자열 생성
                    if cnt != 1 :
                        buf += str(cnt) + temp
                        cnt = 1
                    else :
                        #  다른 경운 cnt 빼고 temp 만 문자열에 추가
                        buf += temp
                    # tmep 값 업데이트 
                    temp = s[i:i+w]
                    i = i + w

        # 마지막 부분 넣어주기
        if cnt != 1 :
            buf += str(cnt) + temp
        else :
            buf += temp
        #  buf 문자열의 길이만 답에 업로드
        ans_list.append(len(buf))
    #  정답에는 최솟값 출력
    answer = min(ans_list)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
