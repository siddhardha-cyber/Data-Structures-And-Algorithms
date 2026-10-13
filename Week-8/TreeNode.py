class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
root=TreeNode('A')
b=TreeNode('B')
c=TreeNode('C')
d=TreeNode('D')
root.children.extend([b,c,d])
b.children.append(TreeNode('E'))
c.children.append(TreeNode('F'))
print("Root Node: ",root.data)
print(f"Children of root node: {[child.data for child in root.children]}")
print(f"Children of B: {[child.data for child in b.children]}")
