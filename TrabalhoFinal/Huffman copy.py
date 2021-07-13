from Node import Node

file = open('C:\\Users\\Marco\\Documents\\GitHub\\AlgoritmosDePrograma-oIII\\TrabalhoFinal\\teste.txt','r', encoding="utf8")
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

            # Adicionar novo pai na lista, mantendo ordenada
            #previousNode = 0
            for i in tree:
                if parentNode.GetLabel() >= i.GetLabel():
                    tree.insert(i.GetLabel(), parentNode)   
                    break

            #print(previousNode)
            #previousNode = i
            #print(previousNode)

            print("Updated Tree")
            self.ShowTree(tree)
        
    
    def ShowTree(self, tree):
        for i in tree:
            print(i.GetLabel())
        

    def Smaller(x,y,z):
        min = x

        if y < min:
            min = y
        if z < min:
            min = z

        return min  
                
        #node = Node(frequency.get(0), frequency.get(1),frequency
        #node.ShowNode()
        




test = Huffman()
test.HuffmanAlgorithm()

