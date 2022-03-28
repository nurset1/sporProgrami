from Qtkayıtekranı import Ui_Form
from PyQt5.QtWidgets import *
import sqlite3

class Kayit(QWidget):
    def __init__(self):
        super().__init__()
        self.baglantiolustur()
        self.ui= Ui_Form()
        self.ui.setupUi(self)
        self.ui.kayitol.clicked.connect(self.kayittamamla)

    def baglantiolustur(self):
        self.baglanti = sqlite3.connect("kullanıcı.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists üyeler " \
                "(isim TEXT,soyisim TEXT,telefon TEXT,doğumtarihi TEXT,boy TEXT,kilo TEXT,kullanıcı_adı TEXT,parola TEXT,antrenman TEXT, diyet TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def kayittamamla(self):
        ad=self.ui.isim.text()
        soyad=self.ui.soyisim.text()
        kullanici=self.ui.kullaniciadi.text()
        sifre=self.ui.parola.text()
        telefon=self.ui.telefon.text()
        dogumtarihi=self.ui.dogumtarih.text()
        boy=self.ui.boy.text()
        kilo=self.ui.kilo.text()

        sorgu="Select * From üyeler where kullanıcı_adı = ?"
        self.cursor.execute(sorgu,(kullanici,))
        bilgi = self.cursor.fetchall()
        if ad == "" or soyad == "" or kullanici == "" or sifre == "" or telefon == "" or dogumtarihi == "" or boy == "" or kilo == "":
            self.ui.bilgilabel.setText("Lütfen Bilgileri Eksiksiz Doldurun!")

        elif len(bilgi) != 0:
            self.ui.bilgilabel.setText("Kullanıcı Adı Zaten Kullanılıyor")

        elif len(bilgi) == 0:
            sorgu2 = "Insert into üyeler Values (?,?,?,?,?,?,?,?,?,?)"
            self.cursor.execute(sorgu2,(ad,soyad,telefon,dogumtarihi,boy,kilo,kullanici,sifre,"Antrenman Programı Yok","Diyet Programı Yok"))
            self.baglanti.commit()
            self.ui.bilgilabel.setText("Başarıyla Kaydoldunuz")




