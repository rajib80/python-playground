INT_MAX = 2147483647

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    

def findCeil(root_node, key):
    if root_node is None:
        return -1

    if root_node.value == key:
        return root_node.value
    
    if root_node.value < key:
        return findCeil(root_node.right, key)
    
    ceil = findCeil(root_node.left, key)
    return ceil if ceil >= key else root_node.value


def findFloor(root_node, key):
    
    if root_node is None:
        return INT_MAX

    if root_node.value == key:
        return root_node.value
    
    if root_node.value > key:
        return findFloor(root_node.left, key)
    
    floor = findFloor(root_node.right, key)
    return floor if floor <= key else root_node.value


# Test code
root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

key = 5
print("Key = " + str(key))
ceil = findCeil(root, key)
print("Ceil = " + str(ceil))

floor = findFloor(root, key)
print("Floor = " + str(floor))