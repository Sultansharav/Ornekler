giris="""
(1) Toplama
(2) cikarma
(3) carpma
(4) bolme
(5) karesini alma
(6) karekokunu alma"""
print(giris)

soru = input("Yapmak isteginiz islemin numarasini giriniz:")

if soru == "1":
    sayi1=int(input("Toplamak istediginiz birinci sayiyi girin:"))
    sayi2=int(input("Toplamak istediginiz ikinci sayiyi girin:"))
    print(sayi1, "+", sayi2, "=", sayi1+ sayi2)

elif soru=="2":
    sayi3=int(input("Cikarmak istediginiz birinci sayiyi girin:"))
    sayi4=int(input("Cikarmak istediginiz ikinci sayiyi girin:"))
    print(sayi3, "-", sayi4, "=", sayi3 - sayi4)

elif soru=="3":
    sayi5=int(input("Carpmak istediginiz birinci sayiyi girin:"))
    sayi6=int(input("Carpmak istediginiz ikinci sayiyi girin:"))
    print(sayi5, "x", sayi6, "=", sayi5* sayi6)

elif soru=="4":
    sayi7=int(input("Bolmek istediginiz birinci sayiyi girin:"))
    sayi8=int(input("Bolmek istediginiz ikinci sayiyi girin:"))
    print(sayi7, "/", sayi8, "=", sayi7 / sayi8)

elif soru=="5":
    sayi9=int(input("Karesini almak istediginiz sayiyi girin:"))
    print(sayi9**2)

elif soru=="6":
    sayi10=int(input("Karekokunu almak istediginiz birinci sayiyi girin:"))
    print(sayi10**0.5)

else:
    print("Yanlis giris yaptiniz")
    print("Yapmak istediginiz islemin numarasini giriniz:", giris)

input()

