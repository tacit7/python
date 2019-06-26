from tree_node import TreeNode
#!/usr/bin/env python
#   1
# 2   3
#    4 5
#

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)

a.left = b
a.right = c

c.left= d
c.right = e



def serialize(node):
    if node == None:
      return "X,"

    left  = serialize(node.left)
    right = serialize(node.right)

    return str(node.value) + "," + left + right

def do_it():
    return serialize(a)


x  = ['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X']
def deserialize(str):
    value = str.pop(0)
    if value == "X":
        return None

    node = TreeNode(int(value))
    node.left = deserialize(str)
    node.right = deserialize(str)
    return node


import serialize_a_tree
serialize_a_tree.deserialize(['1', '2', 'X', 'X', '3', '4', 'X', 'X', '5', 'X', 'X']
)
