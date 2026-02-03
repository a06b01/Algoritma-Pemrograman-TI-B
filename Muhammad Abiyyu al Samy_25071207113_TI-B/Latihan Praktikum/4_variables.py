g = 2

h = "dua"

print(g)

print(h)

ada = "apa"
ada_apa = "tidak apa"
_apa_ada= "apa tidak"
ada_tidak2 = "tidak apa"

#contoh yang salah

#ada-apa = "apa"
#ada apa = "apa"
#2tak_apa = "apa"

#variabel juga bisa di assign dalam satu baris sekaligus asal sesuai urutannya

a, b, c = "11", "22", "33"

print("a")
print("b")
print("c")

#dan bisa juga mengisi nilai variabel yang sama pada satu baris kode

x = y = z = "21"

print(x)
print(y)
print(z)

buah = "Apel"  # Global

def cek_kulkas():
    buah = "Jeruk"  # LOKAL
    print(f"Di dalam fungsi : {buah}")

print(f"Di luar fungsi  : {buah}") #Apel
cek_kulkas()                 # Memanggil fungsi (Jeruk)
print(f"Di luar fungsi  : {buah}") # Apel (Tidak berubah karena fungsi)

