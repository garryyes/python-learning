# 1) Define a tree node structure (using class)
class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


# 2) Construct a tree by given pre-ordered list, e.g.
#
#    Given: [1, 2, 3, None, None, 4, None, None, 5, None, None]
#
#    Create tree:
#                       1
#                      / \
#                     2  5
#                    / \
#                   3  4

#

def construct_tree(arr, loc=None):
    if loc is None:
        loc = {'i': 0}
    # print 'add', loc['i'], arr[loc['i']]
    if arr[loc['i']] is None:
        loc['i'] += 1
        return None
    root = Node(arr[loc['i']])
    loc['i'] += 1
    root.left = construct_tree(arr, loc)
    root.right = construct_tree(arr, loc)

    return root


tree = construct_tree([1, 2, 3, None, None, 4, None, None, 5, None, None])


def print_tree_preorder(root):
    if root is None:
        print 'None'
        return

    print(root.value)
    print_tree_preorder(root.left)
    print_tree_preorder(root.right)

# print_tree_preorder(tree)


# 3) Print tree by pre-order, reverse 2) but skip None in the list, so you will return [1,2,3,4,5] for the above example
# middleorder:
def print_tree_inorder(root):
    if root is None:
        print 'None'
        return
    print_tree_inorder(root.left)
    print(root.value)
    print_tree_inorder(root.right)

# print_tree_midorder(tree)

def print_tree_postorder(root):
    if root is None:
        print 'None'
        return
    print_tree_postorder(root.left)
    print_tree_postorder(root.right)
    print(root.value)

# print_tree_postorder(tree)

#4) sum of all node values
def sum_of_all_nodes(root):
    nsum = 0
    if root is None:
        return nsum
    nsum += root.value
    nsum+= sum_of_all_nodes(root.left)
    nsum += sum_of_all_nodes(root.right)
    return nsum
# print sum_of_all_nodes(tree)
#
arr2 = [1,18,6,7,None, None, None, None, 2,11,2,None, None, 3, None, 4,None, None,3,1,None, 2, None, None, None]
tree2 = construct_tree(arr2, loc=None)
# print_tree_preorder(tree2)
# print sum_of_all_nodes(tree2)

def max_height(root):

    if root is None:
        return 0
    height = 1
    height += max(max_height(root.left),max_height(root.right))
    return height
# print max_height(tree2)

# search a given value; exit -->true, else-->false
def search_it(root,val):
    if root is None:
        return False
    if root.value == val:
        return True
    l = search_it(root.left,val)
    r = search_it(root.right,val)
    return l or r

print search_it(tree2, 11)



