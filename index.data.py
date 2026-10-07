import json

Produk_Mieinstan = "data.json"
while True:
    print("1. Lihat semua Produk Mie Instan")
    print("2. Tambah Produk Mie Instan")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        with open(Produk_Mieinstan, "r", encoding="utf-8") as f:
            data_barang = json.load(f)

        print("Daftar produk mie instan:")
        for barang in data_barang:
            print("Nama :", barang["nama"])
            print("Harga :", barang["harga"])
            print("Stok :", barang["stok"])
        print()

    elif pilihan == "2":
        with open(Produk_Mieinstan, "r", encoding="utf-8") as f:
            data_barang = json.load(f)
        nama = input("Nama produk mie instan: ")
        harga = input("Harga produk mie instan: ")
        stok = input("Stok produk instan: ")

        data_baru={
            "nama": nama,
            "harga": harga,
            "stok": stok,
        }
        data_barang.append(data_baru)

        with open(Produk_Mieinstan, "w", encoding="utf-8") as f:
            json.dump(data_barang, f, indent=4)
        print("Produk Mie Instan telah ditambahkan")
        print()

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
