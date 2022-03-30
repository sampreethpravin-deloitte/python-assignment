class StringClass:
    def __init__(self,chars):
     self.chars=chars
    def CharsCnt(self):
        return(len(self.chars))
    def CharList(self):
       return([i for i in self.chars])



class PairsPossible(StringClass):
    def __init__(self, text_string):
        StringClass.__init__(self, text_string)
        self.text_string = text_string
        self.allPairs = []

    def getPairs(self):
       return self.allPairs

    def generatePairs(self):
        for s in list(self.text_string):
            for ss in list(self.text_string):
                self.allPairs.append(s + ss)
text_string = input("enter the string ")

a=StringClass(text_string)
print(a.CharsCnt())
print(a.CharList())

text_1 = PairsPossible(text_string)
text_1.generatePairs()
pair_list = text_1.getPairs()
print(pair_list)