class Node:
    def __init__(self, data = None, next = None):
        ## data of the node
        self.data = data

        ## next pointer
        self.next = next

class LinkedList:

    def __init__(self):
        ## initializing the head with None
        self.head = None
    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)
    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None
     # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        Node = self.head
        while Node != None:
            print(nodeNames[Node.data], end =" => ")
            #print(Node.data, end =" => ")
            Node = Node.next
        print()

grafo = [
            [0,0,0,1,1,1,1,1],#A
            [0,0,1,0,0,1,1,1],#B
            [0,1,0,1,0,0,1,1],#C
            [1,0,1,0,0,1,0,1],#D
            [1,0,0,0,0,1,0,0],#E
            [1,1,0,1,1,0,1,0],#F
            [1,1,1,0,0,1,0,0],#G
            [1,1,1,1,0,0,0,0]#H
        ]
visitedNodes = []
treeList = [None] * 8
orderedNodes = [None] * 8
nodeLetters  = ['A','B','C','D','E','F','G','H'];
nodeNames  = ['Tia Juana','Mi Ex','La Charito','El Jefe','Mamá','La Prima Moderna','Ella','El Cuñado'];

def calculate():
    #for actualTree, row in enumerate(grafo):
    for orderedNode in orderedNodes:
        actualTree = orderedNode[0]
        if actualTree not in visitedNodes:
            visitedNodes.append(actualTree)
            treeList[actualTree] = LinkedList() # Instancia de la clase
            treeList[actualTree].add_at_end(actualTree) # Agregamos un elemento al frente del nodo
            for i, element in enumerate(grafo[actualTree]):
                if element==1 and checkCompatibility(i, treeList[actualTree]):
                    treeList[actualTree].add_at_end(i)
                    visitedNodes.append(i)


    for tree in treeList:
        if tree != None:
            tree.print_list() # Imprimimos la lista de nodos    

def checkCompatibility(i, tree):
    if i in visitedNodes: return False
    Node = tree.head
    while Node != None:
        if grafo[Node.data][i] != 1 or grafo[i][Node.data]!=1: 
            return False
        Node = Node.next   
    return True

def orderNodesByConnections():
    global orderedNodes
    nodesWeight = [ [i,0]  for i in range(8)]
    for row in grafo:
        for i, col in enumerate(row):
            nodesWeight[i][1] += col
    orderedNodes = sorted(nodesWeight, key=lambda x: x[1]) 


# 0 => 3
orderNodesByConnections()
print("[# Nodo, Connections]")
print(orderedNodes)
calculate()
