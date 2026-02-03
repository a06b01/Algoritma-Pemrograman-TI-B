perintah = input("Masukkan perintah (start/stop/pause): ")

match perintah:
    case "start":
        print("Mesin dinyalakan...")
    case "stop":
        print("Mesin dimatikan.")
    case "pause":
        print("Mesin dihentikan sejenak.")
    case _:
        print("Perintah tidak dikenal!")
