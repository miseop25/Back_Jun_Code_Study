class JobCosulting :
    def __init__(self, table, languages, preference):
        self.table = table
        self.languages = languages
        self.preference = preference

        self.jobDict = dict()
        self.applicantDict = dict()
        self.answer = ''
    
    def setDictInfo(self) :
        for job in self.table :
            arr = list(job.split(" "))
            self.jobDict[arr[0]] = dict()
            self.applicantDict[arr[0]] = 0

            langDict = self.jobDict[arr[0]]
            for i, lang in enumerate(arr[1:]) :
                langDict[lang] = 5 - i
    
    def setScore(self) :
        for k, v in self.jobDict.items() :
            for i in range(len(self.languages)) :
                if self.languages[i] not in v : 
                    continue 
                self.applicantDict[k] += ( self.preference[i] * v[self.languages[i]] )
    
    def getAnswer(self) :
        self.setDictInfo()
        self.setScore()
        result = sorted(self.applicantDict.items(), key = lambda x: (-x[1], x[0]) )
        self.answer = result[0][0]
        return self.answer


def solution(table, languages, preference):
    answer = ''
    jc = JobCosulting(table,languages,preference)
    answer = jc.getAnswer()
    return answer

t = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
l = ["PYTHON", "C++", "SQL"]
p = [7, 5, 5]
print(solution(t,l,p))