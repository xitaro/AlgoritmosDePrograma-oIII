class Node:
    def __init__(self, label):
        self.label = label
        self.char = None
        self.left = None
        self.right = None

    def GetLabel(self):
        return self.label
    
    def GetLeft(self):
        return self.left

    def GetRight(self):
        return self.right

    def GetChar(self):
        return self.char

    def SetLabel(self, label):
        self.label = label

    def SetLeft(self, left):
        self.left = left

    def SetRight(self, right):
        self.right = right   
    
    def SetChar(self, char):
        self.char = char   