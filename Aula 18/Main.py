import collections
from Huffman import Huffman

file = open('E:\Aulas\Algoritmos de Programação\Python\Algoritmos de Programação 3\Aula 18\hino.txt','r', encoding="utf8")
read = file.read()

huffman = Huffman()

huffman.Frequency(read)
