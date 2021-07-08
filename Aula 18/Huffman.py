import collections
import heapq

class Huffman:
    
    def Frequency(self, myFile):
        frequency = collections.Counter(myFile)
        print(frequency)
        return frequency

    def CountingSort(array, max):

    #1
    size = len(array)
    output = [0] * size

    #2 Initialize count array
    count = [0] * (max + 1)

    #3 Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    #4 Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    def Prefixes(self, frequency):
        tree = []
        for char, freq in frequency.items():
            heapq.heappush(tree,(freq,char))