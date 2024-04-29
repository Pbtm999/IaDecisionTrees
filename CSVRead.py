import pandas as pd

class CSVRead():

    def __init__(self, filename):
        self.trainData = pd.read_csv('datasets/'+filename+'.csv')

    def getLine(self, line):
        return self.trainData.iloc[[line]]
    
    def getAllData(self):
        return self.trainData