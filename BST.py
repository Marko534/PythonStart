class Node:
    def __init__(self, Value=None):
        self.Value = Value
        self.LeftNode = None
        self.RigthNode = None
        self.ParentNode = None


class BinarySearchTree:
    def __init__(self):
        self.Root = None

    def Insert(self, Value):
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
                self._insert(Value, CurrentNode.LeftNode)
        elif Value > CurrentNode.Value:
            if CurrentNode.RigthNode == None:
                CurrentNode.RigthNode = Node(Value)
                CurrentNode.RigthNode.ParentNode = CurrentNode
            else:
                self._insert(Value, CurrentNode.RigthNode)
        else:
            print('Vece e vo drvoto i ne se tormozam so duplikati')

    def PrintTree(self):
        if self.Root != None:
            self._PrintTree(self.Root)

    def _PrintTree(self, CurrentNode):
        if CurrentNode != None:
            self._PrintTree(CurrentNode.LeftNode)
            print(str(CurrentNode.Value))
            self._PrintTree(CurrentNode.RigthNode)

    def Height(self):
        if self.Root == None:
            return 0
        else:
            return self._height(self.Root, 0)
        
    def _height (self, CurrentNode, height):
        if CurrentNode == None:
            return height
        leftHeight = self._height(CurrentNode.LeftNode, height+1 )
        rightHeight = self._height(CurrentNode.RigthNode, height+1 )
        return max(leftHeight, rightHeight)
        


def FillTree(Tree, List):
    for i in List:
        Tree.Insert(i)
    return Tree

def RandomList (NumberOfElements=100, MaxInteger=1000):
    from random import randint
    List = []
    for i in range (NumberOfElements):
        List.append(randint(0, MaxInteger))
    return List
        
print (RandomList())


tree = BinarySearchTree()
tree = FillTree(tree, RandomList())

tree.PrintTree()
print (tree.Height())
