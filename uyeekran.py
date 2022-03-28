from Qtuyeekran import Ui_Form
from PyQt5.QtWidgets import *
import sqlite3
from datetime import datetime
class UyeEkran(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.baglantiolustur()
        self.ui.kullanicilabel.setText("nusret")

        self.ui.antrenmanbuton.clicked.connect(self.antrenmangoster)
        self.ui.diyetbuton.clicked.connect(self.diyetgoster)
        self.ui.nabizbuton.clicked.connect(self.nabizgoster)


    def baglantiolustur(self):
        self.baglanti = sqlite3.connect("kullanıcı.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists üyeler " \
                "(isim TEXT,soyisim TEXT,telefon TEXT,doğumtarihi TEXT,boy TEXT,kilo TEXT,kullanıcı_adı TEXT,parola TEXT,antrenman TEXT, diyet TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def antrenmangoster(self):
        kullanici = self.ui.kullanicilabel.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ?"
        self.cursor.execute(sorgu,(kullanici,))
        bilgi = self.cursor.fetchall()
        self.ui.bilgiekran.setText(bilgi[0][8])

    def diyetgoster(self):
        kullanici = self.ui.kullanicilabel.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ?"
        self.cursor.execute(sorgu, (kullanici,))
        bilgi = self.cursor.fetchall()
        self.ui.bilgiekran.setText(bilgi[0][9])

    def nabizgoster(self):
        kullanici = self.ui.kullanicilabel.text()
        nabiz = self.ui.dinleniknabiz.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ?"
        self.cursor.execute(sorgu,(kullanici,))
        bilgi = self.cursor.fetchall()

        if nabiz=="" or nabiz==" ":
            self.ui.bilgiekran.setText("Lütfen Minimum Kalp Atış Hızınızı Girin(harf ve noktalama işaretleri olmadan)")

        elif nabiz!="":
            nabiz = int(nabiz)
            dogumtarihi=bilgi[0][3]
            dogumtarihi=dogumtarihi.split(".")
            dogumyili=dogumtarihi[2]
            dogumyili = int(dogumyili)
            su_an = datetime.now()
            buyil= su_an.year
            kullaniciyas=buyil-dogumyili
            mkh = 220-kullaniciyas
            minnabiz = 0.6*(mkh-nabiz)+nabiz
            maxnabiz = 0.8*(mkh-nabiz)+nabiz
            minnabiz = str(minnabiz)
            maxnabiz = str(maxnabiz)
            self.ui.bilgiekran.setText("Minimum yağ yakma kalp atış hızınız="+minnabiz+"\n"+
                                       "Maksimum yağ yakma kalp atış hızınız="+maxnabiz+"\n"+"Not:Maksimum kalp atış hızına ulaştığınız zaman lütfen antrenmanınızı sonlandırın bu sizin sağlığınız için çok önemli")


