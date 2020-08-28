from typing import List
class Solution:
    def getAnagrams(self, word) :
        tmep = list(word) 
        tmep = sorted(tmep)
        result = "".join(tmep) 
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = dict()
        for i in strs :
            ana = self.getAnagrams(i)
            if ana in anagramsDict :
                anagramsDict[ana].append(i)
            else :
                anagramsDict[ana] = [i]
        
        answer = list(anagramsDict.values())
        return answer

        