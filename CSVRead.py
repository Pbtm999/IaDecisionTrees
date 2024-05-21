import pandas as pd

class CSVRead():

    def __init__(self, filename):
        self.trainData = pd.read_csv('datasets/'+filename+'.csv')
        self.lines = self.trainData.shape[0]
        self.cols = self.trainData.shape[1]
        
    def getLine(self, line):
        return self.trainData.iloc[[line]]
    
    def getValue(self, line, col):
        return self.trainData.iloc[line, col]
    
    def getAllData(self):
        return self.trainData