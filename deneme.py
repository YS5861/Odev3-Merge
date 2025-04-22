# Kullanıcıdan işlem türünü al
def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Bir sayıyı sıfıra bölemezsiniz!"
    return x / y

def faktoriyel(x):
    if x == 0 or x == 1:
        return 1
    else:
        sonuc = 1
        for i in range(1, x + 1):
            sonuc *= i
        return sonuc

def main():
    print("Hesap Makinesi")
    print("--------------")
    print("İşlem türünü seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Faktoriyel Hesaplama")

    # Kullanıcıdan işlem seçmesini iste
    secim = input("Seçiminizi yapın (1/2/3/4/5): ")

    # Eğer kullanıcı faktöriyel seçerse, sadece bir sayı al
    if secim == '5':
        num = int(input("Faktöriyelini almak istediğiniz sayıyı girin: "))
        print(f"{num}! = {faktoriyel(num)}")
    else:
        # Kullanıcıdan iki sayı al
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print(f"{num1} + {num2} = {toplama(num1, num2)}")
        elif secim == '2':
            print(f"{num1} - {num2} = {cikarma(num1, num2)}")
        elif secim == '3':
            print(f"{num1} * {num2} = {carpma(num1, num2)}")
        elif secim == '4':
            print(f"{num1} / {num2} = {bolme(num1, num2)}")
        else:
            print("Geçersiz giriş")

# Ana fonksiyonu çağır
if __name__ == "__main__":
    main()
