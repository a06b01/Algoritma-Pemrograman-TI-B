#dapat di pakai dengan tanda petik seperti : "" dan ''

print("hello")
print('world')
print("It's alright")

# string adalah array dalam python, dapat di buktikan dengan

a = "teknik"
print(a[2]) # akan muncul "k" (karena 0 = t, 1 = e dan selanjutnya)

# pengulangan melalui string dapat di lakukan dengan "for loop"

for x in "mahasiswa":
    print(x)

p = "Nikolai Ivanovich Vavilov adalah tokoh botani dan genetika terkenal asal Rusia dan Uni Soviet. Namanya dikenal terutama dari koleksi tanaman budidayanya yang kemudian mengantarnya pada teori asal-usul penyebaran tanaman budidaya. "
print(len(p)) # mengukur panjang string dalam p menggunakan "len" (ada 230, huruf dan termasuk tanda baca lainnya)

nomor_hp = "+628120986745"
if "8" in nomor_hp:
    print("ya, ada angka 8")
else:
 print("tidak ada angka 8")

n = "indonesia"
print(n.upper()) # mengkapital kan dengan (variabel.upper()), sebaliknya gunakan 
m = "KECIl"
print(m.lower())

y = "be"
z = "lajar"
c = y + z
print(c) # menjadi belajar

# bisa menggabungkan string dan angka dengan "f string"
umur = 19

lengkap = f"umur ku adalah {umur} tahun"
print(lengkap)
