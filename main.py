from Dataset import Dataset
from DecisionTree import DecisionTree

# dataset = Dataset().readCSV('datasets/', 'weather', True)
# weatherDecissionTree = DecisionTree(dataset)
# print('\nWeather Tree:\n')
# weatherDecissionTree.DFSPrint()

dataset = Dataset().readCSV('datasets/', 'restaurant', True)
restaurantDecissionTree = DecisionTree(dataset)
print('\nRestaurant Tree:\n')
restaurantDecissionTree.DFSPrint()
restaurantDecissionTree.classifyMultipleExamples('testRestaurant')

# dataset = Dataset().readCSV('datasets/', 'iris', True)
# irisDecissionTree = DecisionTree(dataset)
# print('\nIris Tree:\n')
# irisDecissionTree.DFSPrint()
