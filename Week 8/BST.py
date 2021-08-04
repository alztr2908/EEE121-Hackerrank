class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __delete__(self):
        del self._left
        del self._right

    def _insert(self, val):
        # Part A.
        # Complete the following function so that BSTree.insert(val)
        # correctly inserts an element val into its correct location in
        # the binary search tree.

        if (val < self._data):
            if (self._left == None):
                # --- Do something here. ---
                self._left = BSTNode(val)
            else:
                # --- Do something here. ---
                self._left._insert(val)

        else:
            if (self._right == None):
                # --- Do something here. ---
                self._right = BSTNode(val)
            else:
                # --- Do something here. ---
                self._right._insert(val)

    def _print(self):
        # Part B.
        # Implement the following function recursively so that BSTree.print()
        # correctly prints the contents of the BST in sorted order.
        # --- Write your code here.----

        # Inorder traversal
        # if(node == null) won't work so this is my implementation
        
        if self._left is not None:
            self._left._print()
        print(self._data,end=' ') 
        if self._right is not None:
            self._right._print()

        

    def _find(self, val):
        if (val == self._data):
            return True

        elif (val < self._data):
            if (self._left == None):
                return False
            else:
                return self._left._find(val)

        else:
            if (self._right == None):
                return False
            else:
                return self._right._find(val)


class BSTree:
    def __init__(self):
        self._root = None

    def __delete__(self):
        del self._root

    def insert(self, val):
        '''Inserts val into the BST.'''
        if (self._root != None):
            self._root._insert(val)
        else:
            self._root = BSTNode(val)

    def find(self, val):
        '''Returns True if val is in the BST, and False otherwise.'''
        return self._root._find(val)

    def print(self):
        '''Prints the sorted contents of the BST.'''
        self._root._print()
        print()


# NOTE: The following statements in main check for the correctness of
#       your implementation. Do not modify anything beyond this point!
if __name__ == '__main__':
    n = int(input())
    ls = list()

    for i in range(n):
        ls.append(int(input()))

    myTree = BSTree()

    for x in ls:
        myTree.insert(x)

    myTree.print()

    print(myTree.find(7))
    print(myTree.find(15))