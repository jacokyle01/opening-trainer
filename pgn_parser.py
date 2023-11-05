import re
import opening_tree as otree

def parse_pgn(pgn):
    tokens = tokenize_pgn(pgn)
    pairs = pair_parentheses(tokens)
    root = otree.OpeningTree("root", "none")
    build_otree(tokens, root, pairs, 0, len(tokens))
    return root 

def build_otree(tokens, parent, pairs, start, end):
    index = start
    head = False
    while (index < end):
        token = tokens[index]
        if (not head):
            ply = otree.OpeningTree(token, "white") #TODO handle color changes
            head = ply 
            otree.link(parent, head)
        elif (token == "("): #handle branch
            branch_start = index
            branch_end = pairs[branch_start]
            build_otree(tokens, head.parent, pairs, branch_start + 1, branch_end)
            #continue searching the main line 
            index = branch_end
        else:
            ply = otree.OpeningTree(token, "white")
            otree.link(head, ply)
            head = ply 
        index += 1

def tokenize_pgn(pgn):
    pattern = r'\(|\)|\w+\d' #make this more rigorous- will fail with more complex SAN
    return re.findall(pattern, pgn)

def pair_parentheses(tokens):
    pairs = dict()
    nesting = [] #keep track of how many nested parentheses we're in 
    for (pos, token) in enumerate(tokens):
        if (token == ")"):
            if (nesting):
                opening = nesting.pop()
                pairs.update({opening: pos})
        elif (token == "("):
            nesting.append(pos)
    return pairs 