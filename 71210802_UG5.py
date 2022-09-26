class Mobil:
    merk=""
    tipe=""
    kapasitasBBM= None
    jenisBahanBakar= None

    def __init__(self,merk,tipe):
        self._merk = merk
        self._tipe = tipe

    def setkapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM
    def setjenisBahanBakar(self,kapasitasBBM):
        self._jenisBahanBakar = kapasitasBBM

    def getjenisBahanBakar(self):
        return self._jenisBahanBakar
    def getkapasitasBBM(self):
        return self._kapasitasBBM
    def gettipe(self):
        return self._tipe
    def getmerk(self):
        return self._merk

    def printInfo(self):
        print("="*10 + " INFO " + "="*10)
        print("Merk\t\t:", self.getmerk())
        print("Tipe\t\t:", self.gettipe())
        print("Bahan Bakar\t:",self.getjenisBahanBakar())
        print("Kapasitas BBM\t:", self.getkapasitasBBM())
    
    def isiBBM(self, harga):
        if self.getjenisBahanBakar() is None or self.getkapasitasBBM() is None :
            print("ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")
        else:
            print("Mengisi "+str(self.getkapasitasBBM())+" liter")
            print("Total Harga : Rp"+str(harga * self.getkapasitasBBM()))

if __name__ == "_main_":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()
    
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setjenisBahanBakar("Bensin")
    mobil2.setkapasitasBBM(20)
    mobil2.printInfo()

    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)