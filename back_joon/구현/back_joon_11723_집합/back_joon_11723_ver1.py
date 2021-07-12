import sys
input = sys.stdin.readline
class Set :
    def __init__(self):
        self.sets = [0 for _ in range(21)] 
    
    def add(self, num) :
        if not self.sets[num] : 
            self.sets[num] = 1
    
    def remove(self, num) :
        if self.sets[num] :
            self.sets[num] = 0
    
    def check(self, num) :
        return self.sets[num]
    
    def toggle(self,num) :
        if self.sets[num] :
            self.sets[num] = 0
        else :
            self.sets[num] = 1
    
    def all(self) :
        for i in range(1,21) :
            self.sets[i] = 1 
    
    def empty(self) :
        for i in range(1, 21) :
            self.sets[i] = 0


if __name__ == "__main__" :
    n = int(input())
    s = Set()
    for _ in range(n) :
        cmd = list(input().rstrip().split(" "))
        if cmd[0] == "add" :
            s.add(int(cmd[1]))
        elif cmd[0] == "remove" :
            s.remove(int(cmd[1]))
        elif cmd[0] == "check" :
            print(s.check(int(cmd[1])))
        elif cmd[0] == "toggle" :
            s.toggle(int(cmd[1]))
        elif cmd[0] == "all" :
            s.all()
        elif cmd[0] == "empty":
            s.empty()


