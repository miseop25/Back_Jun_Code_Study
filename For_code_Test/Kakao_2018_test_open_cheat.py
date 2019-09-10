def solution(record):
    analysis = []
    output_id_list =[]
    ouput_option_list = []
    answer = []

    cheat_record = dict()
    for i in record :
        analysis.append(i.split(' '))
        if analysis[0][0] == "Enter"  :
            cheat_record[analysis[0][1]] = analysis[0][2]
            output_id_list.append(str(analysis[0][1]))
            ouput_option_list.append(1)
        elif analysis[0][0] == "Change" :
            cheat_record[analysis[0][1]] = analysis[0][2]
        else :
            output_id_list.append(str(analysis[0][1]))
            ouput_option_list.append(0)

        analysis.clear()


    for i in range(len(output_id_list)) :
        if ouput_option_list[i] == 1 :
            ans = str(cheat_record[output_id_list[i]] +  '님이 들어왔습니다.')
            answer.append(ans)
        else :
            ans = str(cheat_record[output_id_list[i]] +  '님이 나갔습니다.')
            answer.append(ans)

    print(answer)
    return answer