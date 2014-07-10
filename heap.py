class Heap:
    def __init__(self, L = []):
        self.buf = L
        self.heapify()

    def heapify(self):
        """Heapify and return L"""
        if len(self.buf) == 0: return self.buf
        for i in range(len(self.buf)-1, -1, -1):
            self.percolateDown(i)

    def leftChild(self, index):
        """Returns index of the left child of buf[index]"""
        return index*2+1

    def rightChild(self, index):
        """Returns index of the right child of buf[index]"""
        return index*2+2

    def parent(self, index):
        """Returns index of the parent of buf[index]"""
        return (index-1)/2

    def root(self, index):
        """Returns True if buf[index] is the root"""
        return index==0

    def leaf(self, index):
        """Returns True if buf[index] is a leaf"""
        return self.rightChild(index) >= len(self.buf) and self.leftChild(index) >= len(self.buf)

    def oneChild(self, index):
        """Returns Tue if buf[index] has only one child"""
        return self.rightChild(index) == len(self.buf)

    def percolateDown(self, index):
        """Validate Heap properties starting at buf[index]"""
        if self.leaf(index): return

        if self.oneChild(index):
            if self.buf[index] > self.buf[self.leftChild(index)]:
                (self.buf[index], self.buf[self.leftChild(index)]) = (self.buf[self.leftChild(index)], self.buf[index])
            return

        if min(self.buf[self.leftChild(index)], self.buf[self.rightChild(index)]) >= self.buf[index]:
            return

        if self.buf[self.leftChild(index)] < self.buf[self.rightChild(index)]:
            (self.buf[index], self.buf[self.leftChild(index)]) = (self.buf[self.leftChild(index)], self.buf[index])
            self.percolateDown(self.leftChild(index))
            return

        (self.buf[index], self.buf[self.rightChild(index)]) = (self.buf[self.rightChild(index)], self.buf[index])
        self.percolateDown(self.rightChild(index))
        return

    def removeMin(self):
        self.buf[0] = self.buf.pop()
        self.percolateDown(0)


def main():
    L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44 ,65, 74, 76, 30, 82, 43]
    h = Heap(L)
    print h.buf
    h.removeMin()
    print h.buf

if __name__ == "__main__":
    main()
