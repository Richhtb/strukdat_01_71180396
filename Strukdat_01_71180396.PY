def tambah(x , y):
    x + y
def Kurang(x , y):
    x - y
def kali(x , y):
    x * y
def bagi(x , y):
    x / y     
print("Pilih Menu: ")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

while True :
    pilihan = input("Pilihan anda: ")
    if pilihan in("1","2","3","4"):
        bil1 = int(input("Masukkan bilangan 1:"))
        bil2 = int(input("Masukkan bilangan 2:"))
        
        if pilihan == "1":
            print(tambah(bil1,bil2))
        elif pilihan == "2":
            print(Kurang(bil1,bil2))
        elif pilihan == "3":
            print(kali(bil1,bil2))
        elif pilihan == "4":
            print(bagi(bil1,bil2))
        pilihanLagi= input("pilihan anda: ")
        if pilihanLagi == "Q":
            break     
        else:
          print("nomor tidak sesuai ") 
print("terima kasih dan sampai jumpa") 