class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None


class BST(Node):
    def __init__(self):
        self.root = None
        self.array = []
    # this function take a value, convert it into node and then insert it in the binary tree

    def insertNode(self, value):
        item = Node(value)
        if self.root == None:
            self.root = Node(item.value)
        else:
            current = self.root
            while True:
                if item.value[1] > current.value[1]:
                    if current.right == None:
                        current.right = Node(item.value)
                        current.right.parent = current
                        break
                    else:
                        current = current.right
                elif item.value[1] < current.value[1]:
                    if current.left == None:
                        current.left = Node(item.value)
                        current.left.parent = current
                        break
                    else:
                        current = current.left
    # this function finds the minimum value of the tree

    def visit(self, node):
        try:
            if node.value != None:
                #print("Node: " + str(node.value))
                self.array.append(node.value)
        except:
            print("Node: None")
    # this is a recursive function for inorder traversal

    def inorder(self, root):
        try:
            if root.left != None:
                self.inorder(root.left)
            self.visit(root)
            if root.right != None:
                self.inorder(root.right)
        except:
            return

    def getSorted(self, array):
        tree = BST()
        for i in range(len(array)):
            tree.insertNode(array[i])
        tree.inorder(tree.root)
        return self.array

    def fill_array(self, Node):
       
        if (Node.left != None): 
            pos = self.fill_array(Node.left)

        global BST_array
        BST_array.append(Node.value)
                               
        if (Node.right != None): 
            pos = self.fill_array(Node.right)

    def To_Array (self, Node):
        global BST_array
        BST_array = []
        self.fill_array(Node)

def Shell_sort(array):

    gap = len(array) // 2 
    
    while gap > 0:
        i = 0
        j = gap

        while (j < len(array)):
    
            if (array[i][1] > array[j][1]):
                array[i],array[j] = array[j],array[i]
            
            i = i + 1
            j = j + 1
        
            
            k = i
            while (k - gap > -1):

                if array[k - gap][1] > array[k][1]:
                    array[k-gap], array[k] = array[k], array[k-gap]
                
                k = k - 1

        gap = gap // 2
        
    return array
        
def cocktail_sort(array):


    
    swapped = True
    start = 0
    end = len(array) - 1
    while (swapped == True):
 
        
        swapped = False
 
        
        for i in range(start, end):
            if (array[i][1] > array[i + 1][1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
 
        
        if (swapped == False):
            break
 
        
        swapped = False
 
        
        end = end-1
 
        
        for i in range(end-1, start-1, -1):
            if (array[i][1] > array[i + 1][1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
 
        
        start = start + 1

    return array

bt = BST()

bt.insertNode([[0],[3]])
bt.insertNode([[1],[4]])

bt.insertNode([[2],[5]])
bt.insertNode([[3],[6]])
bt.insertNode([[4],[7]])

bt.To_Array(bt.root)
print(BST_array)