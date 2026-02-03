suhu1 = 50
celsius1 = (suhu1 - 32) * 5 / 9
print(celsius1)

suhu2 = 75
celsius2 = (suhu2 - 32) * 5 / 9 # tanpa fungsi
print(celsius2)

suhu3 = 50
celsius3 = (suhu3 - 32) * 5 / 9
print(celsius3)

# dengan fungsi, kode dapat di gunakan kembali

# contohnya:

def suhu_to_celsius(suhu):
  return (suhu - 32) * 5 / 9

print(suhu_to_celsius(77))
print(suhu_to_celsius(95))
print(suhu_to_celsius(50))

#Fungsi dapat mengirimkan data kembali ke baris kode yang memanggilnya menggunakan pernyataan return."

#Ketika sebuah fungsi mencapai pernyataan return, fungsi tersebut akan berhenti dieksekusi dan mengirimkan hasilnya kembali (ke pemanggilnya)."

def sambutan():
  return "Hello"

pesan =sambutan()
print(pesan)