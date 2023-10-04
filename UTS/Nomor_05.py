from collections import deque
class antrianbank:
    def __init__(self):
        self._antrian = deque()
    
    def masuk(self,pelanggan):
        self._antrian.append(pelanggan)
    
    def keluar(self):
        if self._antrian:
            selesai = self._antrian.popleft()
            return selesai
antri = antrianbank ()
antri.masuk('Pelanggan 1')
antri.masuk('Pelanggan 2')
antri.masuk('Pelanggan 3')
print(antri.keluar())  
print(antri.keluar())