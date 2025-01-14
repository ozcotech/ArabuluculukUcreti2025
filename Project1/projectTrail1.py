def arbUcreti(tutar): # Arabuluculuk ücretini hesaplayan fonksiyon
    return round(tutar * 0.06, 2)

while True:  # Kullanıcıdan anlaşma miktarını alıp arabuluculuk ücretini hesaplayan döngü
    tutar = input("Anlaşma miktarını girin: ")
    
    if not tutar.isdigit() or int(tutar) <= 0: # Kullanıcının girdiği değerin pozitif bir tam sayı olup olmadığını kontrol eden if bloğu
        print("Hatalı giriş yaptınız. Lütfen pozitif bir tam sayı girin.")
        continue

    tutar = int(tutar) #
    
    if tutar < 100000 and arbUcreti(tutar) < 6000: # Anlaşma miktarı 100.000 TL'den az ve arabuluculuk ücreti 6.000 TL'den az ise
        print(f"Anlaşma miktarı: {tutar} TL\nArabuluculuk ücreti: 6.000 TL")
        break
    else: # Anlaşma miktarı 100.000 TL'den fazla veya arabuluculuk ücreti 6.000 TL'den fazla ise
        print(f"Anlaşma miktarı: {tutar} TL\nArabuluculuk ücreti: {arbUcreti(tutar)} TL")
        break