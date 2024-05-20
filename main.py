from Dataset import Dataset
from DecisionTree import DecisionTree
from fourgame.fourGame import FourGame
import copy

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

def PlayFourGame():
    game = FourGame(7, 6)  # Cria uma nova instância da classe FourGame
    end = False  # Inizializa end como False e usa-o para indicar que o jogo ainda não terminou

    move = input('Escolhe o símbolo com que queres jogar (X ou O): ') # Escolher com que símbolo se quer jogar 

    # Escolhe o símbolo com que o jogador quer jogar
    try:
        if move != 'X' and move != 'O':
            raise ValueError
    except ValueError:
        print('O símbolo deve ser X ou O')
        return
    
    match move:
        case 'X':
            iaSymbol = 'O'
        case 'O': 
            iaSymbol = 'X'

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

                dataset = Dataset(dataset, [])
                
                classify = fourgameTree.classifyExample(dataset, 0)
                if (moveValue == -1):
                    moveValue = classify
                    iaMove = i
                elif (moveValue == 'draw' and classify != 'draw'):
                    moveValue = classify
                    iaMove = i

            result, winner = game.makeMove(iaMove, iaSymbol)  # Faz um movimento na coluna col

            end, invalid = showResults(game, result, winner) # Analisa e retorna a resposta junto com o tabuleiro atual
        
    main()
        

def main():
    print("\nDecision Trees using ID3 Algorithm!\n")
    print("Choose one action: \n [1] Print \n [2] Classify one input \n [3] Classify a csv file with examples \n [4] Play Fourgame \n [5] Leave")
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
            PlayFourGame()
            return
        case '5':
            return
        case _:
            print("Invalid Input!")
        
    main()

if __name__ == '__main__':
    main()