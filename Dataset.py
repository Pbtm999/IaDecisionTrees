import csv
import copy

class Dataset():

    def __init__(self, dataset = None, header = None):
        if ((dataset != None) and (header != None)):
            self.array = dataset
            self.header = header
            self.lines = len(self.array)
            # if (len(self.array) > 0):
            self.colls = len(self.array[0])
            # else:
            #     self.colls = 0
    
    def readCSV(self, filename, hasId=False):
        csvFile = open('datasets/'+filename+'.csv', 'r')
        reader = csv.reader(csvFile)
        
        self.header = next(reader)
        self.header.pop(0)

        self.array = []
        for row in reader:
            self.array.append(row)

        if (hasId):
            for i in range(len(self.array)): 
                self.array[i].pop(0)
        
        self.lines = len(self.array)
        self.colls = len(self.array[0])
        return self
    
    def getValue(self, line, coll):
        return self.array[line][coll]

    def copy(self):
        return Dataset(copy.deepcopy(self.array), copy.deepcopy(self.header))
    
    def removeLine(self, line):
        self.array.pop(line)
        self.lines -= 1

    def removeCollum(self, coll):
        self.header.pop(coll)
        for i in range(len(self.array)): 
            self.array[i].pop(coll)
        self.colls -= 1
    