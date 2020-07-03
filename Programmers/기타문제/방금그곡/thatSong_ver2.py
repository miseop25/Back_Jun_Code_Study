def solution(m, musicinfos):
    ans_list = []
    l = len(m)
    for song in musicinfos :
        st, ed, title, melody = map(str, song.split(","))
        time = (int(ed[:2])-  int(st[:2]))*60 + int(ed[3:]) - int(st[3:])
        if time < l : continue

        shap = melody.count("#")
        shap2 = m.count("#")
        val, mods = divmod(time, len(melody) - shap) 
        if val == 0 : val = 1
        melody = melody*val + melody[:mods]
        i = 0
        j = 0
        flag = False
        left = ''
        right = ''
        def chageMelody() :
            if i < len(melody)-shap - 1 :
                if melody[i+1] == "#" :
                    left = melody[i:i+2]
                else : left = melody[i]
            else : left = melody[i]
            return left
        def changeListen() :
            if j < l-shap2 - 1 :
                if m[j+1] == "#" :
                    right = m[j:j+2]
                else : right = m[j]
            else : right = m[j]
            return right
        shap = melody.count("#")
        while i < (len(melody)-shap) and not flag:
            left = chageMelody()
            if left == m[0] :
                flag = True
                j = 0
                right = changeListen()
                
                for _ in range(l - shap2 - 1) :
                    i += len(left)
                    j += len(right)
                    if i > len(melody) :
                        flag = False 
                        break
                    if j > l : 
                        flag = False 
                        break
                    left = chageMelody()
                    right = changeListen()
                    if left != right :
                        flag = False
                        break
                if flag :
                    if left != right :
                        flag = False
            i += len(left)
        if flag :
            ans_list.append([title, time])

    if ans_list :
        ans_list = sorted(ans_list, key= lambda x : -x[1])
        return ans_list[0][0]
    else :
        return "`(None)`"

# print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))