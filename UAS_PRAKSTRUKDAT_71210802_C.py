class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
        
    def getNamaPelanggan(self):
        return self._namaPelanggan

class WarungMakan:
    DEFAULT_CAPACITY = 5
    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0
        
    def dequeue(self): #menghapus data paling depan, dan memajukan urutan data yang dibelangkangnya
        if self.is_empty():
            print("Empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        print("\n### Pelanggan", answer.getNamaPelanggan(),"selesai Membayar ###")

        listBaru = [None] * len(self._data)
        counterListBaru = 0
        for i in range(len(self._data)):
            if self._data[i] != None:
                listBaru[counterListBaru] = self._data[i]
                counterListBaru += 1
        self._data = listBaru
        self._front = 0

    def enqueue(self, namaPelanggan): #menambah data ke list
        pelangganMasuk = NodePelanggan(namaPelanggan)
        if self._size == len(self._data):
            self.resizeBy3(3+len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = pelangganMasuk
        self._size += 1
        
    def resizeBy3(self, cap): #menambah ukuran queue sebesar 3
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+ walk) % len(old)
        self._front = 0
        print("\n ### Melakukan Rezise 3 ###")

    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")
# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()



class node : 
    def __init__(self, data, priority) -> None :
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas : 
    def __init__(self) -> None : 
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool :
        if self._size == 0 : 
            return True
        else:
            return False

    def printAll(self) -> None:
        print("=== Prioritas : Tugas ===", end = ".")
        if self.is_empty() == True:
            print("Priority Queue is empty")
        else:
            bantu = self._head
            while bantu != None :
                print('(', bantu._,',',bantu._priority,')',end = '')
                bantu = bantu._next
            print()

        

    #def _addHead(self, newNode) -> None :
    #    pass

    #def _addTail(self, newNode) -> None:
    #    #isi kode anda
    #    pass
    #    
    #def _addMiddle(self, newNode) -> None:
        #isi kode anda
    #    pass
        
    def add(self, data, priority) -> None:
        baru = node(data, priority)
        if self.is_empty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            if self._head._priority > priority:
                baru._next = self._head
                self._head._prev = baru 
                self._head = baru
            else : 
                self._head._next = baru
                baru._prev = self._head
                self._tail = baru
        else : 
            if self._head._priority> priority:
                baru._next = self._head
                self._head._prev = baru
                self._head = baru

            elif self._tail._priority <= priority : 
                self._tail._next = baru
                baru._prev = self._tail
                self._tail = baru
                self._tail._next = None
            else :
                bantu = self._head
                while bantu._priority< priority:
                    bantu = bantu._next
                bantu2 =bantu._prev
                baru._next = bantu
                bantu2._next = baru
                baru._prev = bantu2
        self._size = self._size + 1
                    

        
    def remove(self) -> None:
        del self._data[0]
        self._size -= 1
        
    def removePriority(self, priority) -> None:
        lst2 = []
        answer = self._data[self._front]
        self._data[self._front] = None
        for x in range (len(self._data)):
            if self._data[x] [0] == priority :
                del self._data[x][1]
        for y in range (len (self._data)):
            if len(self._data[y]) == 1 :
                pass
            else :
                lst2.append(self._data[y])
        self._data = lst2
        self._size -= 1
        print("\n Menghapus",answer.get() )
        
    
    
if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    tugasKu.add("Menyapu", 5)
    tugasKu.add("Cuci Baju", 4)
    tugasKu.add("Beli Alat Tulis", 3)
    tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    tugasKu.remove()
    tugasKu.printAll()
    tugasKu.removePriority(2)
    tugasKu.removePriority(4)
    tugasKu.printtAll()