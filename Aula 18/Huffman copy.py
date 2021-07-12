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
        sortedFrequency = []
        
        print(sorted(frequencyList, key = frequencyList.get), '\n')
        # Ordena a frequência pelo Valor, em ordem Crescente
        for i in sorted(frequencyList, key = frequencyList.get):
            node = Node(frequencyList[i])
            node.SetChar(i)            
            sortedFrequency.append(node)
        # Retorna ela
        return sortedFrequency

    def HuffmanAlgorithm(self):
        tree = []
        tree = self.Frequency(read)

        while True:
            
                
        #node = Node(frequency.get(0), frequency.get(1),frequency
        #node.ShowNode()
        




test = Huffman()
test.HuffmanAlgorithm()

