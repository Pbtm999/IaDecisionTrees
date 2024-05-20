from Dataset import Dataset
from DecisionTree import DecisionTree

def genHeader():
    header = []

    #formato -> coluna-linha
    for i in range (7):
        for j in range (6):
            pos = str(i) + '-' + str(j)
            header.append(pos)

    return header


weatherDecissionTree = DecisionTree(Dataset().readCSV('datasets/', 'weather', True))
restaurantTree = DecisionTree(Dataset().readCSV('datasets/', 'restaurant', True))
irisDecissionTree = DecisionTree(Dataset().readCSV('datasets/', 'iris', True))
fourgameTree = DecisionTree(Dataset().readCSV('datasets/', 'connect4', False, False, genHeader()))

def ChooseTree():
    print("Choose one tree: \n [1] Weather Tenis Tree \n [2] Restaurant Stay Tree \n [3] Iris Tree \n [4] Connect Four Tree (Can't be read or its hard to read)")
    choose = input("Insert: ")
    match choose:
        case '1':
            return weatherDecissionTree
        case '2':
            return restaurantTree
        case '3':
            return irisDecissionTree
        case '4':
            return fourgameTree
        case _:
            print('Invalid Input!')
            ChooseTree()
        

def main():
    print("\nDecision Trees using ID3 Algorithm!\n")
    print("Choose one action: \n [1] Print \n [2] Classify one input \n [3] Classify a csv file with examples \n [4] Leave")
    choose = input("Insert: ")
    
    match choose:
        case '1':
            tree = ChooseTree()
            print("\nTree: \n")
            tree.DFSPrint()
        case '2':
            tree = ChooseTree()
        case '3':
            tree = ChooseTree()
            path = input("\nInsert the path: ")
            file = input("\nInsert the filename (without .csv): ")
            tree.classifyMultipleExamples(path, file)
        case '4':
            return
        case _:
            print("Invalid Input!")
        
    main()

if __name__ == '__main__':
    main()