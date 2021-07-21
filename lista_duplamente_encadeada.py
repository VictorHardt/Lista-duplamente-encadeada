class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.pointer = None
        self.head = None
        self.tail = None
        self.size = 0

    """Cursor"""

    def _avancarKPosicoes(self, K):
        for i in range(K):
            if self.pointer.next:
                self.pointer = self.pointer.next
        return self.pointer

    def _retrocederKPosicoes(self, K):
        for i in range(K):
            if self.pointer.prev:
                self.pointer = self.pointer.prev
        return self.pointer

    def _irParaPrimeiro(self):
        self.pointer = self.head

    def _irParaUltimo(self):
        self.pointer = self.tail

    """Outras"""

    def vazia(self):
        if self.size == 0:
            return True
        else:
            return False

    def cheia(self):
        """só exemplo, lista não está limitada a 10 elementos"""
        if self.size == 10:
            return True
        else:
            return False

    def posicaoDe(self, key):
        pass

    """Operações"""

    def inserirNoFim(self, new):
        self._irParaUltimo()
        node = Node(new)
        if self.head:
            node.prev = self.pointer
            self.pointer.next = node
            self.pointer = node
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.tail = node
            self.size += 1

    def excluirUlt(self):
        self._irParaUltimo()
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
        elif self.head:
            self.pointer = self.pointer.prev
            self.pointer.next = None
            self.tail = self.pointer
            self.size -= 1
        else:
            print("Lista vazia!")

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        if r:
            return r
        else:
            return "Lista vazia!"

    def __str__(self):
        return self.__repr__()


l = ListaDuplamenteEncadeada()
l.inserirNoFim(1)
l.inserirNoFim(2)
l.inserirNoFim(3)
print(l)
l.excluirUlt()
l.excluirUlt()
print(l)
print(l.vazia())
