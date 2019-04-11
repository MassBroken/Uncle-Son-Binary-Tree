from math import sqrt
def createTree():
    Tree = {}
    Tree["root"] = [None,"a",None]
    return Tree

def insertChild(Tree, start, parent, node):
    if start is not None:
        if start == parent:
            atm = parent
            if Tree[atm][1] == None:
                Tree[node]=[atm,None,None]
                Tree[atm][1]=node
            else:
                atm = Tree[atm][1]
                while Tree[atm][2] != None:
                    atm = Tree[atm][2]
                if node not in Tree.keys():
                    Tree[node]=[atm,None,None]
                    
                else:
                    Tree[node][0]=atm
                Tree[atm][2]=node
            return True
        else:
            if not insertChild(Tree, Tree[start][1], parent, node):
                insertChild(Tree, Tree[start][2], parent, node)
    else:
        return False

def brotherDel(Tree, node):
    parent = Tree[node][0]
    Tree[parent][2] = Tree[node][2]
    if Tree[node][1]:
        insertChild(Tree,"root", parent, Tree[node][1])
    del(Tree[node])

def childDel(Tree,node):
    parent = Tree[node][0]
    if Tree[node][2]:
        Tree[parent][1] = Tree[node][2]
        if Tree[node][1]:
            insertChild(Tree, "root", Tree[node][2],Tree[node][1])
    else:
        if Tree[node][1]:
            insertChild(Tree,"root", parent, Tree[node][1])
    del(Tree[node])
        
def printTree(Tree, node , n):
    temp = n*"  "
    print (temp,node)
    atm = node
    if Tree[atm][1] != None:
        print(temp, "sons of ", node ,":")
        printTree(Tree, Tree[atm][1] ,n+1)
    if Tree[atm][2] != None:
        #print(temp,Tree[atm][2])
        printTree(Tree, Tree[atm][2],n)

def deleteNode(Tree,Node):
    if Node == "root" :
        print("Root cannot be deleted")

    else:
        parent = Tree[Node][0]
        if Tree[parent][1] == Node:
            childDel(Tree, Node)
        else:
            brotherDel(Tree, Node)

#Non essendo un albero binario di ricerca, 
#la ricerca di un nodo deve essere svolta come 
#in un qualsiasi altro albero binario

def findParent(Tree, node):
    parent = Tree[node][0]
    if Tree[parent][1] == node:
        return parent
    while Tree[parent][2] == node:
        node = parent
        parent = Tree[node][0]
    return parent

def search(Tree, start, node):
    if start != None:
        if start == node:
            print("I found the element as a son of: ", findParent(Tree, node))
            return True
        if not search(Tree, Tree[start][1], node):
            search(Tree,Tree[start][2], node)
               
    else:
        return False

################################################
#              ##             ##               #
#               ##  #######  ##                # 
#                ##         ##                 # 
# Gestione Albero Binario di ricerca Uncle-son #
#                  ##     ##                   #
#                   ##   ##                    #
#                    #####                     #
################################################
 
def isPrime(n):
    if n == 1:
        return 0
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n % i == 0:
            return i
    return 0 

def createUSRTree(n = 0):
    T = {}
    T["0"]=[None,None,None]
    for i in range(1,n):
        num = isPrime(i)
        insertChild(T,"0",str(num),str(i))
    return T  

def searchUSRTree(Tree, node):
    atm = Tree["0"][1]
    f = False
    while atm != None:
        if (int(node) % int(atm) ) != 0 or atm == "1":
            atm=Tree[atm][2]
        else:
            if atm == node:
                print("I Found the item as son of: ",findParent(Tree,node))
                return
            else:
                if not f:
                    f=True
                    atm = Tree[atm][1]
                else:
                    atm = Tree[atm][2]
    print("I couldn't find the item")

def insertUSRNode(Tree,node):
    atm = Tree["0"][1]
    while atm != None: 
        if (int(node) % int(atm) )== 0 and atm!="1":
            insertChild(Tree,"0",atm,node)
            return
        else:
            atm=Tree[atm][2]
    insertChild(Tree,"0","0",node)    

def deleteUSRNode(Tree, Node):
    if Node == "0" :
        print("Root cannot be deleted")

    else:
        parent = Tree[Node][0]
        if Tree[parent][1] == Node:
            USRChildDel(Tree, Node)
        else:
            USRBrotherDel(Tree, Node)


def USRChildDel(Tree,node):
    parent = Tree[node][0]
    Tree[parent][1] = Tree[node][2]
    atm = Tree[node][1]
    while atm != None:
        atm1 = Tree[atm][2]
        insertUSRNode(Tree, atm)
        Tree[atm][2] = None
        atm = atm1
    del(Tree[node])

def USRBrotherDel(Tree, node):
    parent = Tree[node][0]
    Tree[parent][2] = Tree[node][2]
    atm = Tree[node][1]
    while atm != None:
        atm1 = Tree[atm][2]
        insertUSRNode(Tree, atm)
        Tree[atm][2] = None
        atm = atm1
    del(Tree[node])


'''To create a simple Uncle-Son Tree
just call the createTree() function.
It creates a Tree with just the "root"
node and returns it. Make sure to save it
e.g:
T=createTree()

To create a peculiar Uncle-Son Research Tree
call the createUSRTree():
it takes an integer as parameter, which is set
as 0 by default. The parameter sets the number
of elements that will be generated with the Tree
e.g:
T = createUSRTree(25) creates a Tree with root 0
and every number from 1 to 24 as a node.

If you want to Add an element, just call the 
1.insertChild 
2.insertUSRNode
depending on which kind Tree you are using.
However, the first one needs the follow parameters:
1.The Tree that you are using
2.The node from where to start the descension:
  you should put "root", but nothing stops you
  from looking to tree from a different node.
3.The parent to whom you want to add the child
4.The name of the child.

inesrtUSRNode just needs two parameters:
1.The Tree you are using
2.The name of the node you want to add

If you want to delete a node you should use:
1.deleteNode
2.deleteUSRNode
depending on which tree you are using
They both needs just two parameters:
1.The Tree you are using;
2.The name of the node you want to use

If you want to Search for a node,
you need to use:
1.search;
1.searchUSRTree;
Depending on which Tree you are using.
The first one needs three parameters:
1.The Tree you are using;
2.The node from which you want to start the research
  (It should be "root", but again, no one stops you)
3.The node you are looking for.
The second function needs just two parameters
Can you guess which parameters it needs?
ok, fine. i'll tell you myself:
1.The Tree you are using;
2.The node you are looking for.

Feel Free to modify the code as you prefer.
Thanks for your precious time,
Antonino Massarotti, AKA: MassBroken
'''
