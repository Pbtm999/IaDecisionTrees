import pandas as pd

class CSVRead():

    def __init__(self, filename):
        self.trainData = pd.read_csv('datasets/'+filename+'.csv')
        print(self.trainData.head())

    def getLine(self, line):
        print(self.trainData.iloc[[line]])
        return self.trainData.head(line)
    
    def getAllData(self):
        return self.trainData