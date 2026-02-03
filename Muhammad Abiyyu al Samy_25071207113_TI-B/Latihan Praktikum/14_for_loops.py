buah_buahan = ["apel", "jeruk", "mangga"]

for buah in buah_buahan:
    print(f"saya suka makan {buah}")

for angka in range(10):
    if angka == 5:
        break # berhenti saat angka mencapai 5
    print(angka)

print("---")

for angka in range(5):
    if angka == 2:
        continue # lewati angka 2
    print(angka) # output: 0, 1, 3, 4

daftar_nama = ["andi", "budi", "cici"]
cari = "dedi"

for nama in daftar_nama:
    if nama == cari:
        print("ketemu")
        break
else:
    print("nama tidak ditemukan di dalam daftar.")

for i in range(1, 4): # Baris
    for j in range(1, 4): # Kolom
        print(f"[{i},{j}]", end=" ")
    print() # Pindah baris