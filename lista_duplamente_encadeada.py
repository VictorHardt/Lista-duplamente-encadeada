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
        "Começando da posição 1, retorna 0 se o elemento não estiver na lista"
        ghost = Node(key)
        self.tail.next = ghost
        posicao = 1
        self._irParaPrimeiro()
        while self.pointer.data != key:
            posicao += 1
            self.pointer = self.pointer.next
        if posicao > self.size:
            posicao = 0
        self.tail.next = None
        return posicao

    """Operações atômicas"""

    def inserirAposAtual(self, new):
        node = Node(new)
        if self.head:
            node.next = self.pointer.next
            node.prev = self.pointer
            self.pointer.next = node
            self.pointer = node
            self.size += 1
            if self.pointer.next is None:
                self.tail = node
        else:
            self.head = node
            self.tail = node
            self.size += 1

    def excluir(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size = 0
        elif self.pointer.next is None:
            self.pointer = self.pointer.prev
            self.pointer.next = None
            self.tail = self.pointer
            self.size -= 1
        elif self.head:
            prev = self.pointer.prev
            next = self.pointer.next
            self.pointer = self.pointer.prev
            self.pointer.next = next
            self.pointer = self.pointer.next
            self.pointer.prev = prev
            self.size -= 1
        else:
            print("Lista vazia!")

    """Operações sofisticadas"""

    def inserirNoFim(self, new):
        self._irParaUltimo()
        self.inserirAposAtual(new)

    def excluirUlt(self):
        self._irParaUltimo()
        self.excluir()

    """Operações para print da lista"""

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
print(l.posicaoDe(3))
print(l.posicaoDe(4))
l.excluirUlt()
l.excluirUlt()
print(l)
print(l.vazia())
