dosyaAdi = input("Dosya adi giriniz: ")
t0 = input("T0 giriniz: ")
p = input("P giriniz: ")

t0 = float(t0)
p = float(p)

satirlar = []
with open(dosyaAdi, "r") as f:
    for satir in f:  # dosyayi f olarak ac
        i = satir.split()  # satiri al, boslukla parcala
        if len(i) is not 0:  # eger satır bos degil ise:
            satirlar.append(i)  # satirlar icerisine satırı depola 

zamanlar = [float(x[0]) for x in satirlar]  # satirlar icindeki ilk elemanı dondur
akilar = [float(x[1]) for x in satirlar]  # satirlar icindeki ikinci elemani dondur

evreler = []
for zaman in zamanlar:
    evre = (zaman - t0) / p - int((zaman - t0) / p)
    evreler.append(evre)

cikti = dosyaAdi.rstrip(".txt") + "_hesap.txt"  # dosya adindan .txt yi silip _hesap.txt yi ekle

ciktiSatirlar = ""
for zaman, aki, evre in zip(zamanlar, akilar, evreler): 
    # {:>(minimum genislik).(maksimum ondalik)(format tipi)}
    zaman = "{:> 8.4f}".format(float(zaman))
    aki = "{:> 10.7f}".format(float (aki))
    evre = "{:> 7.5f}".format(float(evre))
    satir = zaman + " " + aki + " " + evre + " " + "\n"  # zaman, aki ve evreyi yazip satir atla
    ciktiSatirlar = ciktiSatirlar + satir  # bütün verileri tek bir degiskende topla

with open(cikti, "w") as f:
    f.write(ciktiSatirlar)  # verilerin toplandigi degiskeni cikti'da tanimlanan dosya ismiyle yazdir

from matplotlib import pyplot as plt
a = plt.scatter(zamanlar, akilar, s=2)
plt.show()