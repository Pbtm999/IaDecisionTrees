from Dataset import Dataset
from DecisionTree import DecisionTree

dataset = Dataset().readCSV('weather', True)
weatherDecissionTree = DecisionTree(dataset)

dataset = Dataset().readCSV('restaurant', True)
restaurantDecissionTree = DecisionTree(dataset)

dataset = Dataset().readCSV('iris', True)
irisDecissionTree = DecisionTree(dataset)

# decisionTree = DecisionTree()
# decisionTree.setRoot(Node(attribute))
# do the ID3

