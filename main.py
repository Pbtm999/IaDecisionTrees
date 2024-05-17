from Dataset import Dataset
from DecisionTree import DecisionTree

dataset = Dataset().readCSV('weather', True)
weatherDecissionTree = DecisionTree(dataset)
print('\nWeather Tree:\n')
weatherDecissionTree.DFSPrint()

dataset = Dataset().readCSV('restaurant', True)
restaurantDecissionTree = DecisionTree(dataset)
print('\nRestaurant Tree:\n')
restaurantDecissionTree.DFSPrint()

dataset = Dataset().readCSV('iris', True)
irisDecissionTree = DecisionTree(dataset)
print('\nIris Tree:\n')
irisDecissionTree.DFSPrint()

# decisionTree = DecisionTree()
# decisionTree.setRoot(Node(attribute))
# do the ID3

