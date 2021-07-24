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
        "Começando da posição 1, retorna None se o elemento não estiver na lista"
        if self.tail:
            ghost = Node(key)
            self.tail.next = ghost
            posicao = 1
            self._irParaPrimeiro()
            while self.pointer.data != key:
                posicao += 1
                self.pointer = self.pointer.next
            if posicao > self.size:
                posicao = None
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
            self.pointer = node

    def inserirAntesDoAtual(self, new):
        node = Node(new)
        if self.head:
            if self.pointer != self.head:
                node.prev = self.pointer.prev
                node.next = self.pointer
                self.pointer.prev.next = node
                self.pointer.prev = node
                self.pointer = node
            else:
                node.next = self.pointer
                self.pointer.prev = node
                self.head = node
            self.size += 1
        else:
            self.head = node
            self.tail = node
            self.size += 1
            self.pointer = node

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
        elif self.pointer == self.head:
            self.pointer.next.prev = None
            self.pointer = self.pointer.next
            self.head = self.pointer
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

    def acessarAtual(self):
        return self.pointer.data

    """Operações sofisticadas"""

    def inserirNoFim(self, new):
        self._irParaUltimo()
        self.inserirAposAtual(new)

    def inserirNaFrente(self, new):
        self._irParaPrimeiro()
        self.inserirAntesDoAtual(new)

    def inserirNaPosicao(self, k, new):
        self._irParaPrimeiro()
        if k != 1:
            pos = k - 2
            self._avancarKPosicoes(pos)
            self.inserirAposAtual(new)
        else:
            self.inserirAntesDoAtual(new)

    def excluirUlt(self):
        self._irParaUltimo()
        self.excluir()

    def excluirAtual(self):
        self.excluir()

    def excluirPrimeiro(self):
        self._irParaPrimeiro()
        self.excluir()

    def excluirElemento(self, key):
        self._irParaPrimeiro()
        posicao = self.posicaoDe(key)
        if posicao:
            self._avancarKPosicoes(posicao - 2)
            self.excluir()

    def excluirDaPos(self, k):
        self._irParaPrimeiro()
        self._avancarKPosicoes(k - 1)
        self.excluir()

    def buscar(self, key):
        if self.posicaoDe(key):
            achou = True
        else: 
            achou = False
        return achou

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

print(l)
l.inserirAposAtual(3)
l.inserirAposAtual(9)
l.inserirAntesDoAtual(5)
l.inserirAntesDoAtual(2)
l.inserirNoFim(6)
l.inserirNaFrente(1)
print(l)
l.excluirUlt()
print(l)
l.excluirPrimeiro()
print(l)
print(l.acessarAtual())
l.excluirAtual()
print(l)
print(l.posicaoDe(9))
l.excluirElemento(9)
print(l)
l.excluirDaPos(2)
print(l)
l.inserirNaPosicao(1, 4)
print(l)
print(l.buscar(4))
print(l.buscar(54))