

# class for nodes to be used in a graph 
class Node(object):
    def __init__(self, position, identity):
        self.position = position
        self.identity = identity
        self.gscore = 0
        self.hscore = 0
        self.fscore = 0

    def position(self):
        return self.position 

    def identity(self):
        return self.identity

#columns and rows for a graph/grid
#preferbly 5x5 
class Graph(object):
    def __init__(self, row, col):
        self.columns = col
        self.rows = row
        self.nodes = []
        self.gengraph()
        
    def gengraph(self):
        counter = 0
        for xpos in range(0, self.rows):
            for ypos in range(0, self.columns):
                newnode = Node([xpos, ypos], counter)
                counter = counter + 1
                self.nodes.append(newnode)
                
                    

# Collects neighbors from adjacent areas to the given node on the given graph    
def test_neighbors(node, graph):
    neighbors = []
    left = [node.position[0] - 1, node.position[1]]
    bottom = [node.position[0], node.position[1] - 1]
    right = [node.position[0] + 1, node.position[1]]
    top = [node.position[0], node.position[1] + 1]

    top_left = [node.position[0] - 1, node.position[1] + 1]
    bottom_left = [node.position[0] - 1, node.position[1] - 1]
    top_right = [node.position[0] + 1, node.position[1] + 1]
    bottom_right = [node.position[0] + 1, node.position[1] - 1]

    validposition = [left, bottom, right, top, top_left, bottom_left, top_right, bottom_right]

    for graphnode in graph.nodes:
        for position in validposition:
            if graphnode.position[0] == position[0] and graphnode.position[1] == position[1]:
                neighbors.append(graphnode)
 

    return neighbors

#prints each position (w/ an x and y axis) from the graph given
def print_graph_info(graph):
    for node in graph.nodes :
        print str(node.position[0])  + "," + str(node.position[1])


#
def gScore_test(node, neighbor):
    if neighbor.position[0] == node.position[0] or neighbor.position[1] == node.position[1]:
        neighbor.gscore += 10
    else:
        neighbor.gscore += 14


def hScore_test(goal, node):
    diffx = abs(goal.position[0] - node.position[0])    #xPos
    diffy = abs(goal.position[1] - node.position[1])    #yPos
    node.hscore += 10 * (diffx - diffy)                 

def fScore_test(node):
    node.fscore = (node.gscore + node.hscore)

GRAPH = Graph(5, 5)
STARTINGNODE = Node([0, 0], 0)
ENDINGNODE = Node([4, 2], 1)


mylist = test_neighbors(STARTINGNODE, GRAPH)
for node in mylist:    
    gScore_test(STARTINGNODE, node)
    hScore_test(ENDINGNODE, node)
    fScore_test(node)

#lists neighbors that appear next to the node
for node in mylist:
    print str(node.position[0]) + "," + str(node.position[1]) + " Neighbor "




