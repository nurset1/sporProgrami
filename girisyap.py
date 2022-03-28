from girişekranı import GirisEkranı
from PyQt5.QtWidgets import QApplication

app=QApplication([])
pencere = GirisEkranı()
pencere.show()
app.exec()