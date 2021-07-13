from os import write
from Node import Node

file = open('C:\\Users\\Marco\\Documents\\GitHub\\AlgoritmosDePrograma-oIII\\TrabalhoFinal\\hino.txt','r', encoding="utf8")
read = file.read()

class Huffman:

    def __init__(self):
        self.binCodes = {}
    
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
            print(i, frequencyList[i])
            node = Node(frequencyList[i])
            node.SetChar(i)        
            sortedFrequency.append(node)
        # Retorna ela
        return sortedFrequency

    def HuffmanAlgorithm(self):
        tree = []
        tree = self.Frequency(read)

        print("Start Tree")
        self.ShowTree(tree)
        print('\n')

        while len(tree) > 1:
            # Pega os 2 primeiros nodes da lista
            node1 = tree[0]
            node2 = tree[1]

            # Agrupa os 2 em um nó pai        
            parentNode = Node(node1.GetLabel() + node2.GetLabel())
            
            #  Deixa o nó de menor frequência à esquerda do nó pai.
            parentNode.SetLeft(node1)
            #  Deixa o nó de maior frequência à direita do nó pai.
            parentNode.SetRight(node2)

            # Retirar os dois nós de menor frequência da lista
            tree.remove(tree[0])
            tree.remove(tree[0])

            # Adicionar novo pai na lista,
            tree.append(parentNode)
            # mantendo ordenada
            tree.sort(key=self.SortHelper)

            print("Updated Tree")
            self.ShowTree(tree)   

        # Compress
        rootNode = tree[0]
        binCode = ""
        self.Compress(rootNode, binCode)  

        '''if len(tree) == 0:
                tree.append(parentNode)
            elif len(tree) == 1:
                if parentNode.GetLabel() <= tree[0].GetLabel():                 
                    tree.insert(0, parentNode)  
                else:
                    tree.append(parentNode)
            else:
                lastNode = tree[len(tree)-1]
                print(lastNode.GetLabel())
                for currentNode in tree:
                    if currentNode.GetLabel() > parentNode.GetLabel():
                        tree.insert(tree.index(currentNode), parentNode)
                        break
                    if currentNode.GetLabel() > lastNode.GetLabel():
                        tree.append(parentNode)
                        break'''
          
    def ShowTree(self, tree):
        for i in tree:
            print(i.GetLabel())
        print('\n')

    def Compress(self, root, binCode):
        if (root == None):
            return

        if(root.GetChar() != None):
            self.binCodes[root.GetChar()] = binCode
            return
        
        self.Compress(root.GetLeft(), binCode + "0")
        self.Compress(root.GetRight(), binCode + "1")

    def GetEncodedText(self, text):
	    encodedText = ""
	    for char in text:
		    encodedText += self.binCodes[char]
	    return encodedText

    def SortHelper(self, node):
        return node.GetLabel()

    def WriteCompressedFile(self):
        newFile = open('bincode.bin', 'w+b')
        newFile.write(str.encode(self.GetEncodedText(read)))
        newFile.close()

test = Huffman()
test.HuffmanAlgorithm()

test.WriteCompressedFile()
