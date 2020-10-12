class Hotel :
    def __init__(self, room_number) :
        self.room_number = room_number
        self.roomDict = dict()
        self.answer = []
    
    def findEmptyRoom(self, num) :
        if num not in self.roomDict :
            self.roomDict[num] = num + 1
            return num 
        else :
            newNum = self.findEmptyRoom(self.roomDict[num])
            self.roomDict[num] = newNum + 1

            return newNum
    
    def getAnswer(self) :
        for i in self.room_number :
            n = self.findEmptyRoom(i)
            self.answer.append(n)
        return self.answer


def solution(k, room_number):
    result = []
    h = Hotel(room_number)
    result = h.getAnswer()

    return result

print(solution(10**12, [1,1,1,1,1]))