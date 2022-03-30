class Stringclass:
    def __init__(self,chars):
        self.chars=chars
    def CharsCnt(self):
        return(len(self.chars))
    def CharList(self):
        return([i for i in self.chars])
a=Stringclass(input())
print(a.CharsCnt())
print(a.CharList())

