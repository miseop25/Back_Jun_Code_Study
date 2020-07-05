def stReplace(m) :
    m = m.replace("C#", "c")
    m = m.replace("D#", "d")
    m = m.replace("F#", 'f')
    m = m.replace("A#", "a")
    m = m.replace("G#", "g")
    return m
def solution(m, musicinfos):
    answer = ''
    ans_list = []
    m = stReplace(m)
    for cnt, song in enumerate(musicinfos) :
        st, ed, title, melody = map(str, song.split(","))
        time = (int(ed[:2])-  int(st[:2]))*60 + (int(ed[3:]) - int(st[3:]))
        melody = stReplace(melody)
        if time == 0 : continue
        if time < len(melody) : 
            if m in melody[: time] :
                ans_list.append([title, time, cnt])
            continue
        val, mods = divmod(time, len(melody)) 
        if val == 0 : val = 1
        melody = melody*val + melody[:mods]
        if m not in melody :    continue

        ans_list.append([title, time, cnt])

    if ans_list :
        ans_list = sorted(ans_list, key= lambda x : (-x[1], x[2]))
        return ans_list[0][0]
    else :
        return "(None)"
    return answer

print(solution("CC",[ "04:00,04:02,ZERO,B#CC", "15:00,15:02,FIRST,B#CC", "04:04,04:06,SECOND,B#CC", "04:08,04:10,THIRD,B#CC"]))