import textwrap
class Empty:
    
    def __init__(self):
        # nothing to do!
        pass

    def is_empty(self):
        return True

    def is_leaf(self):
        return False

    def num_nodes(self):
        return 0

    def height(self):
        return 0

    def contains(self, n):
        return False

    def insert(self, n):
        return Node(n, Empty(), Empty())
    
    def min_item(self):
        return
    
    def max_item(self):
        return
    
    def balance_factor(self):
        return 0
    
    def balanced_everywhere(self):
        return True


class Node:

    def __init__(self, n, left, right):
        self.value = n
        self.left = left
        self.right = right

    def is_empty(self):
        return False

    def is_leaf(self):
        return self.left.is_empty() and self.right.is_empty()

    def num_nodes(self):
        return 1 + self.left.num_nodes() + self.right.num_nodes()

    def height(self):
        return 1 + max(self.left.height(), self.right.height())

    def contains(self, n):
        if n < self.value:
            return self.left.contains(n)
        elif n > self.value:
            return self.right.contains(n)
        else:
            return True

    def insert(self, n):
        if n < self.value:
            return Node(self.value, self.left.insert(n), self.right)
        elif n > self.value:
            return Node(self.value, self.left, self.right.insert(n))
        else:
            return self
    
    def inorder(self):
        lst = []
        if self.left.is_empty() == True and self.right.is_empty() == True:
            return [self.value]
        if self.left.is_empty() == False:
            lst += self.left.inorder()
            lst.append(self.value)
        if self.right.is_empty() == False:
            if self.value not in lst:
                lst.append(self.value)
            lst += self.right.inorder()
        return lst

    def min_item(self):
        if self.left.is_empty():
            return self.value
        return self.left.min_item()

    def max_item(self):
        if self.right.is_empty():
            return self.value
        return self.right.max_item()
    
    def balance_factor(self):
        left = self.left.height()
        right = self.right.height()
        return right - left
    
    def balanced_everywhere(self):
        if abs(self.left.balance_factor()) > 1 or abs(self.right.balance_factor()) > 1 :
            return False
        if self.left.balanced_everywhere() == False or self.right.balanced_everywhere() == False:
            return False
        return True
    
    def add_to_all(self,addval):
        if self.is_empty():
            return Empty()
        current = Node(self.value + addval,None,None)
        if self.left.is_empty() == False:
            current.left = self.left.add_to_all(addval)
        else:
            current.left = Empty()
        if self.right.is_empty() == False:
            current.right = self.right.add_to_all(addval)
        else:
            current.right = Empty()
        return current

    def path_to(self,val):
        if self.value == val:
            return [val]
        elif self.value < val:
            lst = [self.value]
            lst += self.right.path_to(val)
            return lst
        else:
            lst = [self.value]
            lst += self.left.path_to(val)
            return lst
    
    def __str__(self):
        return str(bst.inorder())

if __name__ == "__main__": #BST Tester Function
    bst = Empty().insert(42).insert(10).insert(15).insert(63).insert(9).insert(54).insert(99).insert(2).insert(121).insert(110).insert(112).insert(115)
    bst2 = Empty().insert(3).insert(2).insert(4).insert(5)
    print(f"The number of nodes is {bst.num_nodes()}")
    print(f"The height is {bst.height()}")
    print(bst.inorder())
    print(bst.min_item())
    print(bst.max_item())
    bst3 = bst.add_to_all(5)
    print(bst3.inorder())
    print(bst.path_to(115))
    print(bst)
