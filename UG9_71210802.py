class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
        self.size = 0
    def peek(self):
        print("Data prioritas tertinggi : {}" .format(self._data[0]))
    def add(self, data, priority):
        if len(self._data):
            bantu = 0
            while self._data[bantu][1] < priority:
                bantu += 1
            self._data.insert(bantu, (data, priority))
        else:
            self._data.append((data, priority))
    def update(self, priority, data):
        bantu = 0
        while self._data[bantu][1] != priority:
            bantu += 1
        self._data[bantu] = (data, priority)
    def remove(self):
        del self._data[0]
    def removePriority(self, priority):
        bantu = 0
        while self._data[bantu][1] != priority:
            bantu += 1
        del self._data[bantu]
    def printIsiQueue(self):
        print("Isi semua Queue: ", end="")
        for i in self._data[:-1]:
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()