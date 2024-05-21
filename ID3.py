import numpy as np

class ID3():  

    def __init__(self, dataset):
        self.dataset = dataset
        self.dataSetEntropy = self.__calcDatasetEntorpy()
        self.bestAtributte = self.__getBestGainAtributte()

    # Função calculo da entropia de determinado array com valores das classes 
    def __Entropy(self, X):
        sum = 0
        for i in X:
            if (X[i] == 1.0): return 0
            sum += -(X[i]) * np.log2(X[i])
        return sum
    
    # Função calculo da entropia do dataSet
    def __calcDatasetEntorpy(self):
        values = {}
        for line in range(0, self.dataset.lines):
            value = self.dataset.getValue(line, self.dataset.cols-1)
            if (not (value in values)):
                values[value] = 1
            else:
                values[value] += 1

        for key in values:
            values[key] /= self.dataset.lines

        return self.__Entropy(values)
    
    # Função de decissão e escolha do melhor atributo do dataset apresentado
    def __getBestGainAtributte(self):
        maxGain = float('-inf')
        colMax = 0
        valuesMax = {}
        for j in range(0, self.dataset.cols-1):
            values = {}
            gain = self.dataSetEntropy
            for i in range(0, self.dataset.lines):
                value = self.dataset.getValue(i, j)

                if (not (value in values)):
                    values[value] = {"total": 0}
                
                classVar = self.dataset.getValue(i, self.dataset.cols-1)

                if (not (classVar in values[value])):
                    values[value][classVar] = 1
                else:
                    values[value][classVar] += 1
                
                values[value]["total"] += 1

            for key in values:
                for key2 in values[key]:
                    if key2 != "total":
                        values[key][key2] /= values[key]["total"]
                total = values[key].pop("total")
                gain -= (total/self.dataset.lines) * self.__Entropy(values[key])
                values[key]["total"] = total

            if (gain > maxGain):
                maxGain = gain
                colMax = j
                valuesMax = values

        return colMax, valuesMax