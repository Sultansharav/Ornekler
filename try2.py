while True:
    ilk_sayi=input("ilk sayiyi giriniz (Kapatmak icin q tusuna basiniz):")

    if ilk_sayi=="q":
        break

    ikinci_sayi=input("ikinci sayiyi giriniz:")
                   
    try:
        sayi1=int(ilk_sayi)
        sayi2=int(ikinci_sayi)
        print(sayi1, "/", sayi2,"=",sayi1/sayi2)
    except (ValueError, ZeroDivisionError)as hata:
        print("Bir hata olustu!")
        print("Orijinal hata mesaji:",hata)
