class OpeningTree: 
    
    def __init__(self, ply, color):
        self.ply = ply
        self.color = color
        self.parent = -1

        self.children = []

    def getTree(self, multiplier = 0):
        indent = "  " * multiplier
        tree = indent + self.ply + "\n"
        for child in self.children:
            tree += child.getTree(multiplier + 1)
        return tree
 
    def __str__(self):
        return self.color + " played " + self.ply

# helper method to set parent-child relationship
def link(tree1, tree2):
    tree1.children.append(tree2)
    tree2.parent = tree1