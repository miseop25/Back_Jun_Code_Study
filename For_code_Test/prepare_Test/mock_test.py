from numpy import asarray

def solution(answers):
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]

    
    per_1_mult= int(len(answers)/len(person_1))
    per_2_mult= int(len(answers)/len(person_2))
    per_3_mult= int(len(answers)/len(person_3))

    per_1_mod= int(len(answers)%len(person_1))
    per_2_mod= int(len(answers)%len(person_2))
    per_3_mod= int(len(answers)%len(person_3))

    person_1 = person_1*per_1_mult + person_1[ :per_1_mod]
    person_2 = person_2*per_2_mult + person_2[ :per_2_mod]
    person_3 = person_3*per_3_mult + person_3[ :per_3_mod]

    score_1 = list(asarray(answers)/asarray(person_1))
    score_2 = list(asarray(answers)/asarray(person_2))
    score_3 = list(asarray(answers)/asarray(person_3))

    a =score_1.count(1)
    b =score_2.count(1)
    c =score_3.count(1)
    score_dict = {1 : a, 2:b, 3:c}


    key_max = max(score_dict.values())

    print(key_max)
    answer = []
    for i in score_dict :
        if key_max == score_dict[i] :
            answer.append(i)
    answer.sort()
    return answer