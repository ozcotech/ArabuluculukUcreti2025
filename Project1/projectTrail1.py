def arbUcreti(tutar):
    return round(tutar * 0.06, 2)

while True: 
    tutar = input("Anlaşma miktarını girin: ")
    
    if not tutar.isdigit() or int(tutar) <= 0:
        print("Hatalı giriş yaptınız. Lütfen pozitif bir tam sayı girin.")
        continue

    tutar = int(tutar)
    
    if tutar < 100000 and arbUcreti(tutar) < 6000:
        print(f"Anlaşma miktarı: {tutar} TL\nArabuluculuk ücreti: 6.000 TL")
        break
    else:
        print(f"Anlaşma miktarı: {tutar} TL\nArabuluculuk ücreti: {arbUcreti(tutar)} TL")
        break