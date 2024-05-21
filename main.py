from Dataset import Dataset
from DecisionTree import DecisionTree
from fourgame.fourGame import FourGame
import copy

# Gera e retorna o header para o dataset connect4
# returns: type: array[7*6] | Retorna o array que representa as posições do jogo no estilo coluna-linha
def genHeader():
    header = []

    #formato -> coluna-linha
    for i in range (7):
        for j in range (6):
            pos = str(i) + '-' + str(j)
            header.append(pos)

    return header

#Geração das árvores de decissão | datasets na pasta datasets
weatherDecissionTree = DecisionTree(Dataset().readCSV('datasets/', 'weather', True)) # Árvore do dataset (weather.csv)
weatherDecissionBining = DecisionTree(Dataset().readCSV('datasets/', 'weather', True, True, None, 3), True) # Árvore do dataset (weather.csv) com os valores numéricos discretizados
restaurantTree = DecisionTree(Dataset().readCSV('datasets/', 'restaurant', True)) # Árvore do dataset (restaurant.csv)
irisDecissionTree = DecisionTree(Dataset().readCSV('datasets/', 'iris', True)) # Árvore do dataset (iris.csv)
irisDecissionTreeBining = DecisionTree(Dataset().readCSV('datasets/', 'iris', True, True, None, 3), True) # Árvore do dataset (iris.csv) com os valores numéricos discretizados
fourgameTree = DecisionTree(Dataset().readCSV('datasets/', 'connect4', False, False, genHeader())) # Árvore do dataset (connect4.csv)

# Abre um prompt que requesita a decissão de que árvore de decissão usar
# returns: type: DecissionTree Instance | Retorna o objeto da árvore de decissão escolhida pelo utilizador
def ChooseTree():
    print("Choose one tree: \n [1] Weather Tenis Tree \n [2] Weather Tenis Tree with Bining \n [3] Restaurant Stay Tree \n [4] Iris Tree \n [5] Iris Tree with Bining \n [6] Connect Four Tree (Can't be read or its hard to read)")
    choose = input("Insert: ")
    match choose:
        case '1':
            return weatherDecissionTree
        case '2':
            return weatherDecissionBining
        case '3':
            return restaurantTree
        case '4':
            return irisDecissionTree
        case '5':
            return irisDecissionTreeBining
        case '6':
            return fourgameTree
        case _:
            print('Invalid Input!')
            ChooseTree()
        
# Analisa e retorna a resposta junto com o tabuleiro atual
# params: 
#
#       game | matrix (list of lists): matrix de caracteres | representa o estado atual do tabuleiro do jogo
#       result | type: int | representa o códdigo daquilo que aconteceu no jogo (-1 -> a coluna está cheia | 0 -> Caso não acha fim no jogo | 1 -> Caso de empate | 2 -> Caso de vitória)
#       winner | type: string | representa o símbolo que venceu no caso de vitória
#
# returns: type: boolean | Retorna se o jogo terminou ou não
def showResults(game, result, winner):

    print(game)  # Print do estado atual do tabuleiro

    match result:
        case -1:  # Caso quando a coluna está cheia
            print("Invalid Move! Please choose another column.")
            return False, True
        case 0:  # Caso para quando o movimento é valido mas não resulta no fim do jogo
            print("Nice Move!")
            return False, False
        case 1:  # Caso de empate
            print("It's a Draw!!")
            return True, False
        case 2:  # Caso de vitória
            print('The symbol ' + winner + ' just won!')
            return True, False

# Trata da interface e decissão do jogo user vs Ia (decission Tree)
# returns: void
def PlayFourGame():
    game = FourGame(7, 6)  # Cria uma nova instância da classe FourGame
    end = False  # Inizializa end como False e usa-o para indicar que o jogo ainda não terminou

    move = 'X' # Escolher com que símbolo se quer jogar 
    iaSymbol = 'O'

    # Faz moves até que o jogo tenha um fim
    while not end:
        invalid = False
        while True:  # Loop para verificar o input até ser dado um movimento válido
            try:
                col = int(input('Column: '))
                if col < 1 or col > 7:
                    raise ValueError  # Raise a ValueError se o input não estiver entre 1-7
                break
            except ValueError:
                print("Invalid Input! Please enter a number from 1 to 7.")

        result, winner = game.makeMove(col-1, move)  # Faz um movimento na coluna col

        end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual

        if not end and not invalid:

            iaMove = col
            moveValue = -1 
            while (game.state[0][iaMove] != '-'):
                iaMove = iaMove + 1

            for i in range(7):
                state = copy.deepcopy(game.state)
                j = 5
                while (j >= 0):
                    if (state[j][i] == '-'):
                        state[j][i] = 'x'
                        break
                    j -= 1
                
                dataset = [[]]
                for x in range(7):
                    for y in range(5, -1, -1):
                        symb = state[y][x].lower()
                        if (symb == '-'): symb = 'b'
                        dataset[0].append(symb)

                #Cria o dataset e classifica-o
                dataset = Dataset(dataset, [])
                
                classify = fourgameTree.classifyExample(dataset, 0)
                if (moveValue == -1):
                    moveValue = classify
                    iaMove = i
                elif (moveValue == 'loss' and classify != 'loss'):
                    moveValue = classify
                    iaMove = i
                elif (moveValue == 'draw' and classify == 'win'):
                    moveValue = classify
                    iaMove = i

            result, winner = game.makeMove(iaMove, iaSymbol)  # Faz um movimento na coluna col

            end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual
        
    main()
        
# Main | Abre um prompt para escolha de que operação usar
# returns: void
def main():
    print("\nDecision Trees using ID3 Algorithm!\n")
    print("Choose one action: \n [1] Print \n [2] Classify a csv file with examples \n [3] Play Fourgame \n [4] Leave")
    choose = input("Insert: ")
    
    match choose:
        case '1': #Print da árvore de decissão a ser escolhida pelo user
            tree = ChooseTree()
            print("\nTree: \n")
            tree.DFSPrint()
        case '2': #Classificação de um dataset de exemplos (sem class)
            tree = ChooseTree()
            path = input("\nInsert the path: ")
            file = input("\nInsert the filename (without .csv): ")
            tree.classifyMultipleExamples(path, file)
        case '3': #Jogo FourGame contra a árvore de decissão
            PlayFourGame()
            return
        case '4': #Saída do prompt 
            return
        case _:
            print("Invalid Input!")
        
    main()

if __name__ == '__main__':
    main()