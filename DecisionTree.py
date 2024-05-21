from ID3 import ID3
from Node import Node
from Dataset import Dataset
import copy

class DecisionTree():

    def __init__(self, dataset):
        self.initialDataset = dataset
        self.root = self.__generateNode(dataset)

    def __generateNode(self, dataset, tabI=0, numRemovedColumns=0, value=None):
        attribute, values = ID3(dataset).bestAtributte
        node = Node(attribute, value, dataset.header[attribute])

        for key in values:
            isClass = False
            for key2 in values[key]:
                if (key2 != "total"):
                    if (values[key][key2] == 1.0):
                        node.addNeighbour(Node(key2, key, None, True))
                        isClass = True
                        break
            if (not isClass):
                #cuts the dataset
                datasetCopy = dataset.copy()
                linestoRemove = []
                for i in range(len(datasetCopy.array)):
                    if (datasetCopy.array[i][attribute] != key):
                        linestoRemove.append(i)

                for x in sorted(linestoRemove, reverse=True):
                    datasetCopy.removeLine(x)

                datasetCopy.removeColumn(attribute)

                # generates the child node
                node.addNeighbour(self.__generateNode(datasetCopy, tabI+2, numRemovedColumns+1, key))

        return node

    def DFSPrint(self, tabI = 0, node = None):
        
        if (node == None):
            node = self.root
        
        print('\t'*tabI + '<'+node.label+'>')
        
        for currentNode in node.getNeighbours():

            if (currentNode.isClass):
                print(('\t'*(tabI+1))+currentNode.getValue()+': ' + currentNode.getAttribute())

            else:
                print(('\t'*(tabI+1))+currentNode.getValue()+':')
                self.DFSPrint(tabI+2, currentNode)

    def classifyMultipleExamples(self, path, file):

        dataset = Dataset().readCSV(path, file, True, False)
        for line in range(dataset.lines):
            self.classifyExample(copy.deepcopy(dataset), line)

        return
    
    def classifyExample(self, dataset, line):

        actualNode = self.root
        value = dataset.array[line][actualNode.getAttribute()]

        while (actualNode.isClass != True):
            
            neighbours = actualNode.getNeighbours()
            
            found = False
            for node in (neighbours):
                if node.getValue() == value:
                    actualNode = node
                    found = True
                    break

            if (found == False): return -1

            if (actualNode.isClass != True):
                value = dataset.array[line][(actualNode.getAttribute())]
                dataset.removeColumn(actualNode.getAttribute())

        # print('Line ' + str(line+1) + ' Class: ' + actualNode.getAttribute())
    
        return actualNode.getAttribute()