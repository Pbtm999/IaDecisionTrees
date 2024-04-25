import csv

class CSVRead():

    def __init__(self, filename):
        self.csvFile = open('datasets/'+filename+'.csv', 'r')
        self.reader = csv.reader(self.csvFile)

    def next(self):
        return next(self.reader)

    def getRawReader(self):
        return self.reader

    def close(self):
        self.csvFile.close()
        return None

        