from CSVRead import CSVRead
from DecisionTree import DecisionTree
from Node import Node

reader = CSVRead('weather')

# Gets the header
header = reader.next()
lenght = len(header)

print(header, "len: " + str(lenght))
for row in reader.getRawReader():
    print(row)

# decisionTree = DecisionTree()
# decisionTree.setRoot(Node(attribute))
# do the ID3

