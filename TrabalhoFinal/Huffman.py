from Node import Node
import collections
import heapq

file = open('E:\Aulas\Algoritmos de Programação\Python\Algoritmos de Programação 3\Aula 18\hino.txt','r', encoding="utf8")
read = file.read()

class Huffman:
    
    def Frequency(self, stringFile):
        # Cria o dicionário da frequência
        # Começa vazio
        frequency = {}
        # Para cada caracter no arquivo já transformado em string
        for char in stringFile:
            # Se o caracter não está no dicionário
            if not char in frequency:
                # Inicializa a posição
                frequency[char] = 0
            # Soma 1 para a contagem
            frequency[char] += 1
        # Printa a frequêcia
        print(frequency, '\n')
        frequency = self.SortFrequency(frequency)
        return frequency

    def SortFrequency(self, frequencyList):
        sortedFrequency = {}
        
        print(sorted(frequencyList, key = frequencyList.get), '\n')
        # Ordena a frequência pelo Valor, em ordem Crescente
        for i in sorted(frequencyList, key = frequencyList.get):
             # Se o caracter não está no dicionário
            if not i in sortedFrequency:
                # Inicializa a posição no novo dict
                sortedFrequency[i] = 0
            # Chave do novo dicionário, recebe o valor do dicionário de frequência original
            sortedFrequency[i] = frequencyList[i]
        # Printa
        print(sortedFrequency)
        # Retorna ela
        return sortedFrequency

    def HuffmanAlgorithm(self):
        tree = []
        frequency = {}
        frequency = self.Frequency(read)

        counter = 0
        currentValue = 0
        labelValue = 0
        for i in frequency.values():
            counter+=1
            currentValue = i
            labelValue += i

            node = Node()
            node.SetLabel(labelValue)

            if counter == 2:
                value = 0
                break
            



                
        #node = Node(frequency.get(0), frequency.get(1),frequency
        #node.ShowNode()
        




test = Huffman()
test.HuffmanAlgorithm()

