from Node import Node

'''fileName = 'hino.txt'
path = 'C:\\Users\\Marco\\Documents\\GitHub\\AlgoritmosDePrograma-oIII\\TrabalhoFinal\\'
file = open( path + fileName,'r', encoding="utf8")
read = file.read()'''

class Huffman:

    # Construtor
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

        # Chama a função que ordena a frequencia
        frequency = self.SortFrequency(frequency)
        return frequency

    def SortFrequency(self, frequencyList):
        # Inicializa uma nova lista vazia
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

    # Código de Huffman
    def HuffmanAlgorithm(self,read):

        # Inicializa lista para criar a árvore
        tree = []
        # Recebe a lista de frequência já ordenada
        tree = self.Frequency(read)

        # Printa a árvore inicial
        print("Start Tree")
        self.ShowTree(tree)
        print('\n')

        # Enquanto houver mais de um nodo na lista
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

            # Adicionar novo nodo (pai) na lista,
            tree.append(parentNode)
            # Mantendo ordenada
            tree.sort(key=self.SortHelper)

            print("Updated Tree")
            self.ShowTree(tree)   

        # Compress
        # Como a árvore agora tem apenas 1 nodo
        # Salvo ele como root
        rootNode = tree[0]
        # Inicializa uma string para salvar o código binário
        binCode = ""

        # Chama a função que comprime
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

    # Função para printar a árvore      
    def ShowTree(self, tree):
        # Para cada nodo na lista
        for node in tree:
            # Printa o valor do nodo
            print(node.GetLabel())
        print('\n')

    # Função para comprimir
    def Compress(self, root, binCode):
        # Para evitar erros, se o root for vazio, retorna
        if (root == None):
            return

        # Se o caracter do nodo não for vazio
        if(root.GetChar() != None):
            # Salva o código binário da letra no dicionário e retorna
            self.binCodes[root.GetChar()] = binCode
            return
        
        # Recursão passando 0 para esquerda e 1 para direita
        self.Compress(root.GetLeft(), binCode + "0")
        self.Compress(root.GetRight(), binCode + "1")

    # Função para retornar o código
    def GetEncodedText(self, text):
	    encodedText = ""
        # Para cada caracter no hino
	    for char in text:
            # Pega no dicionário o código binário pelo caracter e salva na string
		    encodedText += self.binCodes[char]
	    return encodedText

    # Função para ajudar a ordenar
    def SortHelper(self, node):
        # Retorna o valor do nodo
        return node.GetLabel()
    
    # Função que calcula o tamanho do arquivo de entrada
    def FileSize(self, stringFile):
        # Valor do byte
        byte = 8
        # Contador para cada caracter
        charCount = 0
        # Para cada caracter no arquivo original
        for char in stringFile:
            # Adiciona 1 no contador
            charCount += 1
        # Arquivo original é baseado em ascii
        ascii = charCount * byte
        return ascii

    # Função que retorna o tamanho em bits do arquivo comprimido
    def CompressedSize(self, stringFile):
        # Inicializa contador
        count = 0
        # Para cada bit na string de binários
        for bit in stringFile:
            # Adiciona 1 no contador
            count += 1
        return count

    # Função que calcula a porcentagem de redução entre o arquivo original e o comprimido
    def CompressPercent(self, fileSize, compressedFile):
        # Pega a porcentagem do comprimido perante o original
        percent = (compressedFile / fileSize) * 100
        # A diferença é o que foi comprimido
        inversePercent = 100 - percent
        return inversePercent

    '''def WriteCompressedFile(self):
        newFile = open('bincode.bin', 'w+b')
        encodedText = self.GetEncodedText(read).encode("utf-8")
        newFile.write(encodedText)
        newFile.close()'''

'''test = Huffman()
test.HuffmanAlgorithm(read)

print(test.binCodes,'\n')

fileSize = test.FileSize(read)
encodedText = test.GetEncodedText(read)
compressedFile = test.CompressedSize(encodedText)

print(encodedText)
print("O nome do arquivo original é:", fileName)
print("Tamanho do arquivo original:",fileSize, 'bits')
print("Tamanho do arquivo comprimido:",compressedFile, 'bits')

print("O arquivo comprimido é:", test.CompressPercent(fileSize, compressedFile),'% menor do que o arquivo original')

#test.WriteCompressedFile()'''