import csv
import copy

class Dataset():

    def __init__(self, dataset = None, header = None):
        if ((dataset != None) and (header != None)):
            self.array = dataset
            self.header = header
            self.lines = len(self.array)
            self.cols = len(self.array[0])
    
    def readCSV(self, path, filename, hasId=False, hasHeader=True, headerInput = None, binCount = None):
        csvFile = open(path+filename+'.csv', 'r')
        reader = csv.reader(csvFile)

        if (hasHeader == True):
            self.header = next(reader)
            self.header.pop(0)
        else:
            self.header = headerInput

        self.array = []
        for row in reader:
            self.array.append(row)

        if (hasId):
            for i in range(len(self.array)): 
                self.array[i].pop(0)

        self.lines = len(self.array)
        self.cols = len(self.array[0])

        if (binCount != None):
            self.binning(binCount)
            
        return self
    
    def getValue(self, line, col):
        return self.array[line][col]

    def copy(self):
        return Dataset(copy.deepcopy(self.array), copy.deepcopy(self.header))
    
    def removeLine(self, line):
        self.array.pop(line)
        self.lines -= 1

    def removeColumn(self, col):
        if (self.header): self.header.pop(col)
        for i in range(len(self.array)): 
            self.array[i].pop(col)
        self.cols -= 1


    def binning(self, binCount):                                                       # Bins continuous data into discrete intervals.
        for col in range(self.cols - 1):                                                # Assuming last column is the target
            try:                                                                        # Check if column is numeric
                colData = [float(self.array[i][col]) for i in range(self.lines)]       # Convert column data to float
            except ValueError:                                                          # If column is not numeric, skip
                continue                                                                

            minVal, maxVal = min(colData), max(colData)                             # Get min and max values of column
            binWidth = (maxVal - minVal) / binCount                                 # Calculate bin width
            bins = [minVal + i * binWidth for i in range(binCount + 1)]              # Create bins

            for i in range(self.lines):                                                 # Iterate through rows
                value = float(self.array[i][col])                                       # Get value of cell
                for b in range(len(bins) - 1):                                          # Iterate through bins
                    if (bins[b] <= value < bins[b + 1]):                                # Check if value is within bin
                        self.array[i][col] = f"{bins[b]:.2f}-{bins[b + 1]:.2f}"         # Replace value with bin range
                        break                                                           # Exit loop
                    else:                                                               # If value is not within bin
                        self.array[i][col] = f"{bins[-2]:.2f}-{bins[-1]:.2f}"           # Replace value with last bin range