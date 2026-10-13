class BinaryTreeArray:
    def __init__(self,size):
        self.tree=[None]*size
        self.size=size
    def setRoot(self,data):
        self.tree[0]=data
    def setLeft(self,parentIndex,data):
        childIndex=2*parentIndex+1
        if childIndex<self.size:
            self.tree[childIndex]=data
        else:
            print("Index out of range")
    def setRight(self,parentIndex,data):
        childIndex=2*parentIndex+2
        if childIndex<self.size:
            self.tree[childIndex]=data
        else:
            print("Index out of range")
    def preOrder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        print(self.tree[index],end=' ')
        self.preOrder(2*index+1)
        self.preOrder(2*index+2)
    def postOrder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        self.postOrder(2*index+1)
        self.postOrder(2*index+2)
        print(self.tree[index],end=' ')
    def inOrder(self,index=0):
        if index>=self.size or self.tree[index] is None:
            return
        self.inOrder(2*index+1)
        print(self.tree[index],end=' ')
        self.inOrder(2*index+2)
    def levelOrder(self):
        for value in self.tree:
            if value is not None:
                print(value,end=' ')
    def display(self):
        print("\nArray Representation:")
        for i in range(self.size):
            print(f"Index {i}: {self.tree[i]}")
tree=BinaryTreeArray(7)
tree.setRoot('A')
tree.setLeft(0,'B')
tree.setRight(0,'C')
tree.display()
tree.setLeft(1,'D')
tree.setRight(1,'E')
tree.setRight(2,'F')
tree.display()
print("\nPreorder:",end=' ')
tree.preOrder()
print("\nInorder: ",end=' ')
tree.inOrder()
print("\nPostorder: ",end=' ')
tree.postOrder()
print("\nLever-order: ",end=' ')
tree.levelOrder()
