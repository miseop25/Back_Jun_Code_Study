class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s :
            if i == "(" or i == "{" or i == "[" :
                stack.append(i)
            else :
                if stack :
                    check = stack.pop()
                    if abs(ord(check) - ord(i)) <= 2 :
                        pass
                    else : 
                        return False
                else :
                    return False
        if stack :
            return False
        else :
            return True