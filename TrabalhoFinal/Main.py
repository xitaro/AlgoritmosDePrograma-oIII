from os import read
from Huffman import Huffman

fileName = 'input.in'
path = 'C:\\Users\\Marco\\Documents\\GitHub\\AlgoritmosDePrograma-oIII\\TrabalhoFinal\\'
file = open( path + fileName,'r', encoding="utf8")
read = file.read()

h = Huffman()
h.HuffmanAlgorithm(read)

print(h.binCodes,'\n')

fileSize = h.FileSize(read)
encodedText = h.GetEncodedText(read)
compressedFile = h.CompressedSize(encodedText)

print(encodedText)
print("O nome do arquivo original é:", fileName)
print("Tamanho do arquivo original:", fileSize, 'bits')

print("Tamanho do arquivo comprimido:",compressedFile, 'bits')
print("Uma diferença de:", fileSize-compressedFile, 'bits' )
print("O arquivo comprimido é:", h.CompressPercent(fileSize, compressedFile),'% menor do que o arquivo original')