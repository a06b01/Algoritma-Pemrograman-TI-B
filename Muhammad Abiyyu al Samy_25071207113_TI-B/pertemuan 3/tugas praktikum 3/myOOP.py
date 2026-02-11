#Soal 1 inheritance

class Produk:
    def __init__(self, nama_produk, harga):
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        return f"Produk: {self.nama_produk}"

class elektronik(Produk):
    def __init__(self, nama_produk, harga, garansi):
        super().__init__(nama_produk, harga)
        self.garansi = garansi

    def info_produk(self):
    
        harga_format = f"{self.harga:,.0f}".replace(",", ".")
        return f"{self.nama_produk} seharga {harga_format}dengan garansi {self.garansi} tahun"

class makanan(Produk):
    def __init__(self, nama_produk, harga, tanggal_kadaluarsa):
        super().__init__(nama_produk, harga)
        self.tanggal_kadaluarsa = tanggal_kadaluarsa

    def info_produk(self):
        harga_format = f"{self.harga:,.0f}".replace(",", ".")
        return f"{self.nama_produk} seharga {harga_format} kadaluarsa {self.tanggal_kadaluarsa}"

# Soal 2 olymorphisme

class notifikasi:
    def kirim(self):
        return "mengirim notifikasi umum"

class Email(notifikasi):
    def kirim(self):
        return "mengirim notifikasi melalui Email"

class SMS(notifikasi):
    def kirim(self):
        return "mengirim notifikasi melalui SMS"

# Soal 3 encapsulation

class Mahasiswa:
    def __init__(self):
        self.__nilai = 0
    def set_nilai(self, nilai):
        if 0 <= nilai <= 100:
            self.__nilai = nilai
        else:
            print("nilai tidak valid")

    def get_nilai(self):
        return self.__nilai