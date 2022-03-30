class StringClass:
    def __init__(self , value):
        self.string = value
    def length(self):
        length = len(self.string)
        return length
    def str_to_lst(self , str_lst):
        print(list(str_lst))

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

text_1 = PairsPossible(input())
text_1.generatePairs()
pair_list = text_1.getPairs()
print(pair_list)