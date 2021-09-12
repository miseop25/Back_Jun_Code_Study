
class AriportInfo :
    def __init__(self, name):
        self.myArea = name
        self.dest = dict()

class Travel :
    def __init__(self, tickets) :
        self.ticket = tickets
        self.travelInfo = dict()
    
    def makeInfo(self) :
        ticketIndex = 1
        for st,end in self.ticket :
            if st not in self.travelInfo :
                self.travelInfo[st] = AriportInfo(st)
            if end not in self.travelInfo :
                self.travelInfo[end] = AriportInfo(end)
                
            self.travelInfo[st].dest[end]
            



        

def solution(tickets):
    answer = []
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution( [['ICN','A'],['ICN','A'],['A','ICN']]))