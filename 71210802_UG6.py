from lib2to3.pytree import Node


class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None
    
    def __init__(self, no_rekening, nama, saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLLNC:
    def __init__(self):
        self._nama = None
        self._saldo = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    def insert_head(self, e, nama, saldo=0):
        new_node = Node(e,nama,saldo)
        if self.size == 0:
            self._nama = baru
            self._saldo = baru
            self._tail._next = None
        else:
            new_node.next = head
            head = new_node
            self.size = self.size + 1
    
    def delete(self, position):
        if self.size == 0:
            return False
        elif position == 0:
            self.delete_head()
        elif position + 1 >= self.size:
            self.delete_tail()
        else:
            delete_node = self.head
            for i in range(position):
                delete_node = delete_node.next
            helper = self.head
            while helper.next != delete_node:
                helper = helper.next
            helper.next = delete_node.next
            del delete_node
            self.size = self.size - 1

    

slnc=SLLNC()
slnc.insert_head(201,"Hanif", 250000)
slnc.insert_head(110,"Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()