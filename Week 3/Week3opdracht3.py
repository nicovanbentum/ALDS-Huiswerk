class BSTNode:
    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''
        s2 = ''
        s3 = ''
        if self.right != None:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = s2 + ' '*nspaces + str(self.element) + '\n'
        if self.left != None:
            s3 = self.left.__repr__(nspaces + 3)
        return s1 + s2 + s3

    def insert(self,e):
        parent = self
        current = None
        found = False

        if parent.element < e:
            current = parent.right
        elif parent.element > e:
            current = parent.left
        else:
            found = True

        while not found and current:
            parent = current
            if parent.element < e:
                current = parent.right
            elif parent.element > e:
                current = parent.left
            else:
                found = True

        if not found:
            if parent.element < e:
                parent.right = BSTNode(e,None,None)
            else:
                parent.left = BSTNode(e,None,None)
        return not found

    def insertArray(self,a, low=0, high=-1):
        if len(a) == 0:
            return
        if high == -1:
            high = len(a)-1
        mid = (low+high+1)//2
        self.insert(a[mid])
        if mid > low:
            self.insertArray(a,low,mid-1)
        if high > mid:
            self.insertArray(a,mid + 1,high)

    #homework function
    def rsearch(self, e, node):
        if node == None:
            return False
        if node.element == e:
            return node

        if node.element < e:
            return self.rsearch(e, node.right)
        else:
            return self.rsearch(e, node.left)

    #homework function
    def rinsert(self, e, previous_node, node, went_left): 
        #keeping track of previous node and direction because apparently just doing if node == none:
        #                                                                               node = BST(e, None, None) doesn't actually add the new node
        if node == None:
            if went_left:
                previous_node.left = BSTNode(e, None, None)
            else: 
                previous_node.right = BSTNode(e, None, None)

        else:
            if e < node.element:
                previous_node = node
                went_left = True
                return self.rinsert(e, previous_node, node.left, went_left)
            else:
                previous_node = node
                went_left = False
                return self.rinsert(e, previous_node, node.right, went_left)

#homework class
class Queue:
    def __init__(self):
        self.Q = list()

    def __repr__(self):
        ret = str(self.Q)
        return ret

    def put(self, e):
        if e not in self.Q:
            self.Q.insert(0,e)

    def pop(self):
        if len(self.Q) > 0:
            return self.Q.pop()

    def front(self):
        return self.Q[-1]

    def size(self):
        return len(self.Q)

class BST:
    def __init__(self,a=None):
        if a:
            mid = len(a)//2
            self.root = BSTNode(a[mid],None,None)
            self.root.insertArray(a[:mid])
            self.root.insertArray(a[mid+1:])
        else:
            self.root = None

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'

    #homework function
    def getMax(self):
        it = self.root
        while it.right != None:
            it = it.right
        return it.element

    #homework function
    def rinsert(self, e):
        temp_node = BSTNode(0, None, None)
        return self.root.rinsert(e, temp_node, self.root, False)

    #homework function
    def rsearch(self, e):
        return self.root.rsearch(e, self.root)

    #homework function
    def showLevelOrder(self):
        if not self.root:
            return -1

        node_q = Queue()
        node_q.put(self.root)
        output = ''

        while node_q.size() > 0:
            nr_of_nodes = node_q.size()
            while nr_of_nodes > 0:

                node = node_q.front()
                output = output + ' ' + str(node.element)
                node_q.pop()

                if node.left != None:
                    node_q.put(node.left)
                if node.right != None:
                    node_q.put(node.right)
                nr_of_nodes -= 1

            print(output)
            output = ''

if __name__ == '__main__':
    b = BST([2, 4, 6, 8])
    print(b)
    print('----------------')

    print("max in bst: " + str(b.getMax()))
    print("9 found in bst: " + str(b.rsearch(9)))

    b.rinsert(1)
    b.rinsert(3)
    print('----------------')
    print(b)
    print('----------------')
    b.showLevelOrder()


