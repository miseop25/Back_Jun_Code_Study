import copy
class TravelRoot :
    def __init__(self):
        self.ticketSet = set()
        self.now = ''
        self.rootArr = []


class AriportInfo :
    def __init__(self, name):
        self.myArea = name
        self.dest = dict()

class Travel :
    def __init__(self, tickets) :
        self.ticket = tickets
        self.travelInfo = dict()
        
        self.ticketLen = len(tickets)
        self.answerList = []
    
    def makeInfo(self) :
        ticketIndex = 1
        for st,end in self.ticket :
            if st not in self.travelInfo :
                self.travelInfo[st] = AriportInfo(st)
            if end not in self.travelInfo :
                self.travelInfo[end] = AriportInfo(end)
            
            if end not in self.travelInfo[st].dest : 
                self.travelInfo[st].dest[end] = []
            self.travelInfo[st].dest[end].append(ticketIndex)
            ticketIndex += 1
    
    def doTravel(self, nowTrRoot : TravelRoot) :
        if len(nowTrRoot.ticketSet) == self.ticketLen :
            self.answerList.append(nowTrRoot.rootArr)
            return
        curV = self.travelInfo[nowTrRoot.now]
        for dest, tkIndex in curV.dest.items() :
            for i in tkIndex : 
                if i not in nowTrRoot.ticketSet : 
                    nextTravelRoot = TravelRoot()
                    nextTravelRoot.rootArr = nowTrRoot.rootArr.copy()
                    nextTravelRoot.rootArr.append(dest)
                    nextTravelRoot.now = dest
                    nextTravelRoot.ticketSet = nowTrRoot.ticketSet.copy()
                    nextTravelRoot.ticketSet.add(i)
                    self.doTravel(nextTravelRoot)
    
    def getAnswer(self) :
        self.makeInfo()
        nowTr = TravelRoot()
        nowTr.now = "ICN"
        nowTr.rootArr.append("ICN")
        self.doTravel(nowTr)
        self.answerList = sorted(self.answerList, key = lambda x: x)
        return self.answerList[0]


def solution(tickets):
    answer = []
    t = Travel(tickets)
    answer = t.getAnswer()
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# print(solution( [['ICN','A'],['ICN','A'],['A','ICN']]))