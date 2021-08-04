class MaxHeap:
    def __init__(self):
        self.arr = [None]
        self.size = 0

    # Part A.
    # Fill in the ff. functions such that, given an array implementation arr
    # of a complete tree and a node at arr[idx], the following functions
    # correctly return the indices of the left child, right child, and parent
    # of the given node. Assume that the root node is at arr[1] (NOT arr[0]).

    def _left_child(self, idx):
        return idx*2 # Fill in the blank.
    def _right_child(self, idx):
        return idx*2+1 # Fill in the blank.
    def _parent(self, idx):
        return idx//2 # Fill in the blank.

    def _swap_nodes(self, i, j):
        '''Helper function for swapping two nodes at indices i and j.'''
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _bubble_down(self, idx):
        '''
        Bubbles down a node at arr[idx] to preserve max-heap properties.

        Specifically, a node needs to be moved down the heap if its value is
        smaller than either of its children's values. To ensure that the
        greatest node is at the top of the heap, the current node is swapped
        with the greater of its two children.
        '''
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        if (left_idx > self.size):
            return

        elif (right_idx > self.size):
            left_val = self.arr[left_idx]

            if (left_val > self.arr[idx]):
                self._swap_nodes(left_idx, idx)

        else:
            left_val = self.arr[left_idx]
            right_val = self.arr[right_idx]

            if (left_val > self.arr[idx] and left_val > right_val):
                self._swap_nodes(left_idx, idx)
                self._bubble_down(left_idx)
            elif (right_val > self.arr[idx] and right_val > left_val):
                self._swap_nodes(right_idx, idx)
                self._bubble_down(right_idx)

    def _bubble_up(self, idx):
        '''
        Bubbles up a node at arr[idx] to preserve max-heap properties.

        Specifically, a node needs to be moved up the heap if its value is
        greater than its parent's.
        '''
        parent_idx = self._parent(idx)
        parent_val = self.arr[parent_idx];

        if (idx == 1):
            return

        if (self.arr[idx] > parent_val):
            self._swap_nodes(parent_idx, idx)

            if (parent_idx > 1):
                self._bubble_up(parent_idx)

    # Part B.
    # Complete the following function to perform the following operations:
    # - pop the top node from the max-heap
    #   (i.e. remove the node and return its value)
    # - swap nodes in the heap to preserve the heap's order and shape
    # - adjust the count for the number of nodes in the heap

    def extract(self):
        '''Removes the maximum element from the heap and returns its value.'''
        result = self.arr[1] # Pop the top node and store its value here.

        self.size = self.size - 1 # No. of nodes after the top node is popped

        if (self.size != 0): # If the heap still contains nodes...
            # --- Do something here. ---
            self._swap_nodes(1, self.size+1)
            self.arr.pop()
            self._bubble_down(1)


        return result

    # Part C.
    # Complete the following function to perform the following operations:
    # - insert a new node (with value val) into the heap
    # - swap nodes in the heap to preserve the heap's order and shape
    # - adjust the count for the number of nodes in the heap

    def insert(self, val):
        '''Inserts a new value into the heap.'''
        idx = len(self.arr) # Index where the new value should be placed
        self.arr.insert(idx, val)
        self.size = self.size + 1 # No. of nodes after insertion

        if (self.size > 1): # If the new node is not the root...
            # --- Do something here. ---
            for i in range(self.size,0,-1):
                self._bubble_up(i)


# NOTE: The following statements in main check for the correctness of
#       your implementation. Do not modify anything beyond this point!
if __name__ == '__main__':
    n = int(input())
    ls = list()

    for i in range(n):
        ls.append(int(input()))

    myHeap = MaxHeap()

    for x in ls:
        myHeap.insert(x)

    while(myHeap.size != 0):
        print(myHeap.extract(), end=' ')
    print()