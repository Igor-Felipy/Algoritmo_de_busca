import math

class VectorCompare:
    def magnitude(self, concordance):
        if type(concordance) != dict:
            raise ValueError('O argumento fornecido deve ser do tipo dict')
        total = 0
        for word,count in concordance.items():
            total += count **2
        return math.sqrt(total)

    
    def relation(self, concordance1, concordance2):
        if type(concordance1) != dict:
            raise ValueError('O argumento 1 fornecido deve ser do tipo dict')
        if type(concordance2) != dict:
            raise ValueError('O argumento 2 fornecido deve ser do tipo dict')
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:
                topvalue += count * concordance2[word]
        if (self.magnitude(concordance1)*self.magnitude(concordance2)) != 0:
            return topvalue / (self.magnitude(concordance1)*self.magnitude(concordance2))
        else:
            return 0


    def concordance(self,document):
        if type(document) != str:
            raise ValueError('O argumento fornecidodevve ser do tipo string')
        con = {}
        for word in document.split(' '):
            if word in con:
                con[word] = con[word] + 1
            else:
                con[word] = 1
        return con