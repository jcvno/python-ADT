class Heap:
    def __init__(self):
        self.buf = []

    def leftChild(self, index):
        return index*2+1

def main():
    h = Heap()
    print h.leftChild(0)

if __name__ == "__main__":
    main()
