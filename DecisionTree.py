from ID3 import ID3
from Node import Node

class DecisionTree():

    def __init__(self, dataset):
        self.initialDataset = dataset
        self.root = self.__generateNode(dataset)

    def __generateNode(self, dataset, tabI=0, value=None):
        attribute, values = ID3(dataset).bestAtributte
        node = Node(attribute, value)
        for key in values:
            isClass = False
            for key2 in values[key]:
                if (key2 != "total"):
                    if (values[key][key2] == 1.0):
                        node.addNeighbour(Node(key2, key, True))
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

                datasetCopy.removeCollum(attribute)

                # generates the child node
                node.addNeighbour(self.__generateNode(datasetCopy, tabI+2, key))

        return node

    def DFSPrint(self, tabI = 0, node = None):
        
        if (node == None):
            node = self.root
        
        print('\t'*tabI + '<'+self.initialDataset.header[node.getAttribute()]+'>')
        
        for currentNode in node.getNeighbours():

            if (currentNode.isClass):
                print(('\t'*(tabI+1))+currentNode.getValue()+': ' + currentNode.getAttribute())

            else:
                print(('\t'*(tabI+1))+currentNode.getValue()+':')
                self.DFSPrint(tabI+2, currentNode)




