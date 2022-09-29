print("luas persegi")
def luas_persegi():
    s = int(input("masukkan panjang sisi: "))
    print("luas persegi: ", s*s, "\n")
luas_persegi()

print("luas persegi panjang") 
def luas_persegi_panjang():
    p = int(input("masukkan panjang: "))
    l = int(input("masukkan lebar: ")) 
    print("luas persegi panjang: ", p*l, "\n")
luas_persegi_panjang()

print("luas segitiga")
def luas_segitiga():
    a = int(input("masukkan alas segitiga: "))
    t = int(input("tinggi segitiga: "))
    print("luas segitiga:", a*t*0.5 "\n")
luas_segitiga()

print("luas lingkaran")
def luas_lingkaran():
    r = int(input("masukkan jari-jari lingkaran: "))
    print("luas lingkaran:" , 3.14*r*r, "\n")
luas_lingkaran()