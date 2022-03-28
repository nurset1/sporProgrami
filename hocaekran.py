from Qthocaekran import Ui_Form
from PyQt5.QtWidgets import *
import sqlite3

class HocaEkran(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.baglantiolustur()

        self.ui.arabuton.clicked.connect(self.kullaniciara)
        self.ui.uyelerigosterbuton.clicked.connect(self.uyelerigoster)
        self.ui.antproggoster.clicked.connect(self.antrenmanprog)
        self.ui.diyetgoster.clicked.connect(self.diyetgoster)
        self.ui.pushButton.clicked.connect(self.antkaydet)
        self.ui.pushButton_2.clicked.connect(self.diyetkaydet)
    def baglantiolustur(self):
        self.uyebaglanti = sqlite3.connect("kullanıcı.db")
        self.uyecursor = self.uyebaglanti.cursor()
        sorgu = "Create Table If not exists üyeler" \
                "(isim TEXT,soyisim TEXT,telefon TEXT,doğumtarihi TEXT,boy TEXT,kilo TEXT,kullanıcı_adı TEXT,parola TEXT,antrenman TEXT,diyet TEXT)"
        self.uyecursor.execute(sorgu)
        self.uyebaglanti.commit()

        self.hocabaglanti = sqlite3.connect("kullanıcı.db")
        self.hocacursor = self.hocabaglanti.cursor()
        sorgu2 = "Create Table If not exists hocalar " \
                 "(isim TEXT,soyisim TEXT,telefon TEXT,doğumtarihi TEXT,boy TEXT,kilo TEXT,kullanıcı_adı TEXT,parola TEXT)"
        self.hocacursor.execute(sorgu2)
        self.hocabaglanti.commit()

    def kullaniciara(self):
        self.ui.bilgilabel.clear()
        kullanici = self.ui.kullaniciarama.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ?"
        self.uyecursor.execute(sorgu,(kullanici,))
        bilgi = self.uyecursor.fetchall()
        if len(bilgi)==0:
            self.ui.bilgilabel.setText("Aradığınız Kullanıcı Bulunamadı!")

        elif len(bilgi)!=0:
            boy=str(bilgi[0][4])
            kilo=str(bilgi[0][5])
            self.ui.uyeismi.setText(bilgi[0][0])
            self.ui.uyesoyisim.setText(bilgi[0][1])
            self.ui.kullaniciadi.setText(bilgi[0][6])
            self.ui.tarih.setText(bilgi[0][3])
            self.ui.boy.setText(boy)
            self.ui.kilo.setText(kilo)
            self.ui.telefon.setText(bilgi[0][2])
    def uyelerigoster(self):
        sorgu = "Select * From üyeler"
        self.uyecursor.execute(sorgu)
        bilgi = self.uyecursor.fetchall()
        with open ("bilgi.txt","w",encoding="utf-8") as file:
            file.write("İsim"+" "+"|"+" "+"Soyisim"+" "+"|"+" "+"Numara"+" "+"|"+" "+"Doğum Tarihi"+" "+"|"+" "+"Boy"+" "+"|"+" "+"Kilo"+" "+"|"+" "+"Kullanıcı Adı"+"\n")
            file.write("---------------------------------------------------------------------------------------"+"\n")
            for i in bilgi:
                boy=str(i[4])
                kilo=str(i[5])
                file.write(i[0]+" "+"|"+" "+i[1]+" "+"|"+" "+ i[2]+" "+"|"+" "+ i[3]+" "+"|"+" "+ boy+" "+"|"+" "+ kilo+" "+"|"+" "+i[6] + "\n")
                file.write("---------------------------------------------------------------------------------------"+"\n")
        with open("bilgi.txt","r",encoding="utf-8") as file:
            icerik=file.read()
            self.ui.bilgiekran.setText(icerik)

    def antrenmanprog(self):
        uye = self.ui.kullaniciarama.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ?"
        self.uyecursor.execute(sorgu,(uye,))
        bilgi = self.uyecursor.fetchall()
        if len(bilgi)==0:
            self.ui.bilgiekran.setText("Üye Seçmeniz Gerekli")
        elif len(bilgi)!=0:
            self.ui.bilgiekran.setText(bilgi[0][8])

    def diyetgoster(self):
        uye = self.ui.kullaniciarama.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ?"
        self.uyecursor.execute(sorgu,(uye,))
        bilgi = self.uyecursor.fetchall()
        if len(bilgi)==0:
            self.ui.bilgiekran.setText("Üye Seçmeniz Gerekli")
        elif len(bilgi)!=0:
            self.ui.bilgiekran.setText(bilgi[0][9])

    def antkaydet(self):
        uye = self.ui.kullaniciarama.text()
        yazı = self.ui.bilgiekran.toPlainText()

        if uye =="" or uye == " ":
            self.ui.bilgilabel.setText("Lütfen Program Eklemek İçin Üye Seçin")

        elif uye !="":
            sorgu = "Update üyeler set antrenman = ? where kullanıcı_adı = ?"
            self.uyecursor.execute(sorgu,(yazı,uye))
            self.uyebaglanti.commit()
            self.ui.bilgilabel.setText("Antrenman Programı Kaydedildi")

    def diyetkaydet(self):
        uye = self.ui.kullaniciarama.text()
        yazı = self.ui.bilgiekran.toPlainText()

        if uye =="" or uye == " ":
            self.ui.bilgilabel.setText("Lütfen Program Eklemek İçin Üye Seçin")

        elif uye !="":
            sorgu = "Update üyeler set diyet = ? where kullanıcı_adı = ?"
            self.uyecursor.execute(sorgu,(yazı,uye))
            self.uyebaglanti.commit()
            self.ui.bilgilabel.setText("Diyet Programı Kaydedildi")



