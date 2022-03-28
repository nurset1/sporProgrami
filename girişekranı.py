from QTgiris import Ui_MainWindow
from kayıtekranı import Kayit
from uyeekran import UyeEkran
from hocaekran import HocaEkran
from PyQt5.QtWidgets import *
import sqlite3



class GirisEkranı(QMainWindow):

    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.kayitekran = Kayit()
        self.uyeekran = UyeEkran()
        self.hocaekrani = HocaEkran()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.girisbuton.clicked.connect(self.giris)
        self.ui.kaydolbuton.clicked.connect(self.kayitol)

    def baglanti_olustur(self):
        self.baglantı = sqlite3.connect("kullanıcı.db")
        self.cursor = self.baglantı.cursor()
        sorgu = "Create Table If not exists üyeler " \
                "(isim TEXT,soyisim TEXT,telefon TEXT,doğumtarihi TEXT,boy TEXT,kilo TEXT,kullanıcı_adı TEXT,parola TEXT,antrenman TEXT,diyet TEXT)"
        self.cursor.execute(sorgu)
        self.baglantı.commit()
        sorgu2 = "Create Table If not exists hocalar" \
                 " (isim TEXT,soyisim TEXT,telefon TEXT,doğumtarihi TEXT,boy TEXT,kilo TEXT,kullanıcı_adı TEXT,parola TEXT)"
        self.cursor.execute(sorgu2)
        self.baglantı.commit()

    def giris(self):
        kullanici = self.ui.kullanicigiris.text()
        sifre = self.ui.parolagiris.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ? and parola = ? "
        self.cursor.execute(sorgu,(kullanici,sifre))
        bilgi = self.cursor.fetchall()
        sorgu2 = "Select * From hocalar where kullanıcı_adı = ? and parola = ? "
        self.cursor.execute(sorgu2,(kullanici,sifre))
        bilgi2 = self.cursor.fetchall()

        if len(bilgi)==0 and len(bilgi2)==0:
            self.ui.bilgilabel.setText("Kullanıcı Adı veya Parola Yanlış")
        elif len(bilgi)!=0:
            self.uyeekran.show()
            self.uyeekran.ui.kullanicilabel.setText(kullanici)
        elif len(bilgi2)!=0 and len(bilgi)==0:
            self.hocaekrani.show()

    def kayitol(self):
        self.kayitekran.show()
