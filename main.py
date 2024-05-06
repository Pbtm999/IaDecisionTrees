from Dataset import Dataset
from DecisionTree import DecisionTree

# decissionTree = ID3(CSVRead('weather'))
dataset = Dataset().readCSV('weather', True)
decissionTree = DecisionTree(dataset)

# dataset = Dataset().readCSV('restaurant', True)
# decissionTree = DecisionTree(dataset)

# dataset = Dataset().readCSV('iris', True)
# decissionTree = DecisionTree(dataset)

# print(decissionTree.dataSetEntropy)
# print(decissionTree.chooseRoot())
    

# decisionTree = DecisionTree()
# decisionTree.setRoot(Node(attribute))
# do the ID3

