import json

class Credit():

    def __init__(self, term):
        with open("./weight.json") as fp:
            self.credit = {}
            self.term = term
            data = json.load(fp)
            for i, j in data[term].items():
                self.credit[i]=j 
    
    def find_course(self, cname):
        for i, j in self.credit.items():
            if i == cname:
                return j