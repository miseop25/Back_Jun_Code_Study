import copy
class TravelRoot :
    def __init__(self):
        self.ticketSet = set() #여정을 진행하면서 소비한 티켓들
        self.now = '' #현재 위치
        self.rootArr = [] #여태까지의 여정 

class AriportInfo :
    def __init__(self, name):
        self.myArea = name #해당 공항
        self.dest = dict() #해당 공항에서 갈수 있는 공항들(key)과 티켓번호(Value)

class Travel :
    def __init__(self, tickets) :
        self.ticket = tickets
        #TravelInfo에는 공항들의 정보가 들어간다.
        self.travelInfo = dict()
        
        self.ticketLen = len(tickets)
        self.answerList = []
    
    def makeInfo(self) :
        ticketIndex = 1
        for st,end in self.ticket :
            # 공항 정보가 없다면 만들어 준다.
            if st not in self.travelInfo : 
                self.travelInfo[st] = AriportInfo(st)
            if end not in self.travelInfo :
                self.travelInfo[end] = AriportInfo(end)

            #시작지 공항의 도착지 정보가 없다면 초기화를 시켜준다.
            if end not in self.travelInfo[st].dest : 
                self.travelInfo[st].dest[end] = []

            #시작공항에거 갈수 있는 공항들과 티켓번호를 넣어준다.
            self.travelInfo[st].dest[end].append(ticketIndex)
            ticketIndex += 1
    
    def doTravel(self, nowTrRoot : TravelRoot) :
        if len(nowTrRoot.ticketSet) == self.ticketLen :
            self.answerList.append(nowTrRoot.rootArr)
            #티켓을 모두 소진 했다면 정답리스트에 넣어준다.
            return
        curAirport = self.travelInfo[nowTrRoot.now] #현재공항의 정보
        for dest, tkIndex in curAirport.dest.items() :
            for i in tkIndex : 
                if i not in nowTrRoot.ticketSet :  #사용하지 않은 티켓이라면 사용해준다.
                    nextTravelRoot = TravelRoot()
                    nextTravelRoot.rootArr = nowTrRoot.rootArr.copy()
                    nextTravelRoot.ticketSet = nowTrRoot.ticketSet.copy()
                    #현재 여정을 복사한다.
                    nextTravelRoot.rootArr.append(dest)
                    nextTravelRoot.now = dest
                    nextTravelRoot.ticketSet.add(i)
                    #다음여정에 방문할곳과 사용한 티켓을 추가해주고 다시 여정을 시작한다. 
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