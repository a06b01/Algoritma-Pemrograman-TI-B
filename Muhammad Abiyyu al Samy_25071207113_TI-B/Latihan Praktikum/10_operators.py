print(1+2)

hasil1 = 340 + 230
hasil2 = hasil1 + 2
hasil3 = hasil1 - hasil2 * 0

print(hasil1)
print(hasil2)
print(hasil3)

c = 34
r = 22

print(c + r)
print(c - r)
print(c * r)
print(c / r)
print(c ** r)
print(c // r)

s = 5
s += 4
print(s)

# perbandingan operator

a = 2
b = 3

print(a == b) # F
print(a != b) # T
print(a > b) # F
print(a < b) # T
print(a >= b) # F

# Operator logika

# and (dan) :menghasilkan True hanya jika kedua kondisi bernilai True.
# Jika salah satu saja False, maka hasilnya False.

# or (atau) : Menghasilkan True jika salah satu atau kedua kondisi bernilai True.
# Hanya menghasilkan False jika keduanya False.

# not (negasi) : Membalikkan nilai kebenaran. Jika True jadi False, jika False jadi True.

a = 1945

print( a > 0 and a < 2000) # True

# operator identitas

# is: Menghasilkan True jika kedua variabel merujuk ke objek yang sama.
# is not: Menghasilkan True jika kedua variabel merujuk ke objek yang berbeda.

x = ["jeruk", "apel"]
y = ["jeruk", "apel"]
z = x

print(x is z) # True
print(x is y) # False
print(x == y) # True
