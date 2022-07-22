
class Node:
    def __init__(self, Value = None):
        self.Value = Value
        self.LeftNode = None
        self.RigthNode =  None
        self.ParentNode = None
        
class BinarySearchTree:
    def __init__(self):
        self.Root = None
        
    def Insert (self, Value):
        if self.Root == None:
            self.Root = Node(Value)
        else:
            self._insert(Value, self.Root)
            
    def _insert(self, Value, CurrentNode):
        if CurrentNode.Value > Value:
            if CurrentNode.LeftNode == None:
                CurrentNode.LeftNode = Node(Value)
                CurrentNode.LeftNode.ParentNode = CurrentNode
            else:
                self._insert (Value, CurrentNode.LeftNode )
        elif Value > CurrentNode.Value:
            if CurrentNode.RigthNode == None:
                CurrentNode.RigthNode = Node(Value)
                CurrentNode.RigthNode.ParentNode = CurrentNode
            else:
                self._insert (Value, CurrentNode.RigthNode )
        else:
            print('Vece e vo drvoto i ne se tormozam so duplikati \n')
    
    def PrintTree(self):
        if self.Root != None:
            self._PrintTree(self.Root)
            
    def _PrintTree(self, CurrentNode):
        if CurrentNode != None:
            self._PrintTree(CurrentNode.LeftNode)
            print (str(CurrentNode.Value))
            self._PrintTree(CurrentNode.RigthNode)
       
            
def FillTree(Tree, NumberOfElements = 100, MaxInteger = 10000):
    from random import randint
    for _ in range(NumberOfElements):
        CurrentElement = randint(0, MaxInteger)
        Tree.Insert(CurrentElement)  
    return Tree

tree = BinarySearchTree()
tree = FillTree(tree)

tree.PrintTree()























