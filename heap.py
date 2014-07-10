class Heap:
    def __init__(self, L = []):
        self.buf = L
        self.buf = self.heapify(L)

    def heapify(self, L):
        """Heapify and return L"""
        if len(L) == 0: return L
        for i in range(len(L)-1, -1, -1):
            self.percolateDown(L, i)
        return L

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

    def percolateDown(self, L, index):
        """Validate Heap properties starting at buf[index]"""
        if self.leaf(index): return

        if self.oneChild(index):
            if L[index] > L[self.leftChild(index)]:
                (L[index], L[self.leftChild(index)]) = (L[self.leftChild(index)], L[index])
            return

        if min(L[self.leftChild(index)], L[self.rightChild(index)]) >= L[index]:
            return

        if L[self.leftChild(index)] < L[self.rightChild(index)]:
            (L[index], L[self.leftChild(index)]) = (L[self.leftChild(index)], L[index])
            self.percolateDown(L, self.leftChild(index))
            return

        (L[index], L[self.rightChild(index)]) = (L[self.rightChild(index)], L[index])
        self.percolateDown(L, self.rightChild(index))
        return

def main():
    L = [50, 88, 27, 58, 30, 21, 58, 13, 84, 24, 29, 43, 61, 44 ,65, 74, 76, 30, 82, 43]
    h = Heap(L)

if __name__ == "__main__":
    main()
