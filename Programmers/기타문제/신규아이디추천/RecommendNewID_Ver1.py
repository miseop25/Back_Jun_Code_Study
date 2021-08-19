def applyAllowWord(word) :
    result = ''
    allowWord = 'abcdefghizjlmnopqrstuvwxyz0123456789-_.'
    alSet = set(list(allowWord))
    for c in word :
        if c in alSet :
            result += c
    return result

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = applyAllowWord(new_id)

    temp = new_id
    new_id = new_id.replace('..', '.')
    while temp != new_id :
        temp = new_id
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip(".")
    if new_id == '' :
        new_id = 'a'
    if len(new_id) >= 15 :
        new_id = new_id[ :15]
        new_id = new_id.strip(".")
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id += new_id[-1]
    answer = new_id
    return answer


print(solution("abcdefghijklmn.p"))