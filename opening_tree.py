class OpeningTree: 
    
    def __init__(self, ply, color):
        self.ply = ply
        self.color = color
        self.parent = -1
        self.children = []

        
    def __str__(self):
        return self.color + " played " + self.ply

# helper method to set parent-child relationship
def link(tree1, tree2):
    tree1.children.append(tree2)
    tree2.parent = tree1