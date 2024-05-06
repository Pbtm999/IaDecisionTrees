from ID3 import ID3
from Node import Node

class DecisionTree():

    def __init__(self, dataset):
        self.root = self.__generateNode(dataset, 0)

    def __generateNode(self, dataset, tabI):
        attribute, values = ID3(dataset).bestAtributte
        node = Node(dataset.header[attribute])
        print('\t'*tabI + '<'+dataset.header[attribute]+'>')
        for key in values:
            isClass = False
            for key2 in values[key]:
                if (key2 != "total"):
                    if (values[key][key2] == values[key]["total"]):
                        node.addValue(Node(key2, True))
                        isClass = True
                        print(('\t'*(tabI+1))+key+': ' + key2)
                        break
            if (not isClass):
                print(('\t'*(tabI+1))+key+':')
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
                node.addValue(self.__generateNode(datasetCopy, tabI+2))


