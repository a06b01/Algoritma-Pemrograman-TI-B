from myOOP import elektronik, makanan, Email, SMS, Mahasiswa

def main():
    print("inheritance-------------------(1)")

    tv = elektronik("TV", 3000000, 2)
    roti = makanan("Roti", 15000, "12-12-2026")

    print(tv.info_produk())
    print(roti.info_produk())
    print("polymorphism-------------------(2)")

    pesan_email = Email()
    pesan_sms = SMS()

    print(pesan_email.kirim())
    print(pesan_sms.kirim())
    print("encapsulation------------------(3)")
    mhs = Mahasiswa()
    print("test nilai 85")
    mhs.set_nilai(85)
    print(f"nilai saat ini: {mhs.get_nilai()}")
    print("\ntest nilai 150")
    mhs.set_nilai(150)
    print(f"Nilai saat ini: {mhs.get_nilai()}")

if __name__ == "__main__":
    main()