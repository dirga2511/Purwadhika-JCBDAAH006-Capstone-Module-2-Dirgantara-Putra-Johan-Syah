# Dirgantara Putra Johan Syah
# JCBDAAH006 - Purwadhika
# Capstone Module 2


# ==========================================
# KOPERASI KAMPUNG
# Warehouse Inventory Management System
# Capstone Project Module 2
# ==========================================


# =========================
# INVENTROY DATA
# =========================

inventory = [
    {
        "id_barang": "BRG001",
        "nama_barang": "Indomie Goreng",
        "kategori": "Makanan",
        "stok": 120,
        "harga": 3500,
        "supplier": "PT Indofood CBP Sukses Makmur"
    },
    {
        "id_barang": "BRG002",
        "nama_barang": "Mie Sedaap Goreng",
        "kategori": "Makanan",
        "stok": 110,
        "harga": 3000,
        "supplier": "PT Prakarsa Alam Segar"
    },
    {
        "id_barang": "BRG003",
        "nama_barang": "Aqua 600ml",
        "kategori": "Minuman",
        "stok": 80,
        "harga": 4000,
        "supplier": "PT Tirta Investama"
    },
    {
        "id_barang": "BRG004",
        "nama_barang": "Le Minerale 600ml",
        "kategori": "Minuman",
        "stok": 90,
        "harga": 3500,
        "supplier": "PT Tirta Fresindo Jaya"
    },
    {
        "id_barang": "BRG005",
        "nama_barang": "Ades 600ml",
        "kategori": "Minuman",
        "stok": 100,
        "harga": 3400,
        "supplier": "PT Akasha Wira International"
    },
    {
        "id_barang": "BRG006",
        "nama_barang": "Teh Botol Sosro",
        "kategori": "Minuman",
        "stok": 60,
        "harga": 5000,
        "supplier": "PT Sinar Sosro"
    },
    {
        "id_barang": "BRG007",
        "nama_barang": "Teh Pucuk Harum",
        "kategori": "Minuman",
        "stok": 65,
        "harga": 4500,
        "supplier": "PT Tirta Fresindo Jaya"
    },
    {
        "id_barang": "BRG008",
        "nama_barang": "Teh Kotak",
        "kategori": "Minuman",
        "stok": 70,
        "harga": 4000,
        "supplier": "PT Ultrajaya Milk Industry"
    },
    {
        "id_barang": "BRG009",
        "nama_barang": "Sampoerna Mild",
        "kategori": "Rokok",
        "stok": 100,
        "harga": 40000,
        "supplier": "PT HM Sampoerna"
    },
    {
        "id_barang": "BRG010",
        "nama_barang": "Djarum Mild",
        "kategori": "Rokok",
        "stok": 100,
        "harga": 42000,
        "supplier": "PT Djarum"
    }
]


# =========================
# DISPLAY FUNCTION
# =========================

def display_all_data():

    print("\n========== STOCK DATA ==========\n")

    for item in inventory:

        print(f"ID Barang   : {item['id_barang']}")
        print(f"Nama Barang : {item['nama_barang']}")
        print(f"Kategori    : {item['kategori']}")
        print(f"Stok        : {item['stok']}")
        print(f"Harga       : Rp {item['harga']}")
        print(f"Supplier    : {item['supplier']}")
        print("-" * 40)


def display_data_by_id():

    id_cari = input("\nMasukkan ID Barang : ").upper()

    found = False

    for item in inventory:

        if item["id_barang"] == id_cari:

            print("\n========== DATA BARANG ==========\n")

            print(f"ID Barang   : {item['id_barang']}")
            print(f"Nama Barang : {item['nama_barang']}")
            print(f"Kategori    : {item['kategori']}")
            print(f"Stok        : {item['stok']}")
            print(f"Harga       : Rp {item['harga']}")
            print(f"Supplier    : {item['supplier']}")

            found = True
            break

    if not found:
        print("\nData tidak ditemukan.")


def display_menu():

    while True:

        print("\n===== DISPLAY STOCK DATA =====")
        print("1. Display All Data")
        print("2. Display Data by ID")
        print("3. Back to Main Menu")

        choice = input("\nSelect Menu : ")

        if choice == "1":
            display_all_data()

        elif choice == "2":
            display_data_by_id()

        elif choice == "3":
            break

        else:
            print("\nMenu tidak tersedia.")


# =========================
# CREATE FUNCTION
# =========================

def create_menu():

    while True:

        print("\n===== ADD NEW ITEM =====")
        print("1. Add New Item")
        print("2. Back to Main Menu")

        choice = input("\nSelect Menu : ")

        if choice == "1":
             add_new_item()

        elif choice == "2":
            break

        else:
            print("\nMenu tidak tersedia.")

def add_new_item():

    # =========================
    # VALIDASI ID
    # =========================

    while True:

        id_baru = input("\nMasukkan ID Barang : ").upper()

        found = False

        for item in inventory:

            if item["id_barang"] == id_baru:

                print(f"\nID Barang {id_baru} sudah terdaftar.")

                found = True
                break

        if found:

            pilihan = input("\nIngin mencoba lagi? (Y/N) : ").upper()

            if pilihan == "Y":
                continue

            elif pilihan == "N":
                return

            else:
                print("\nPilihan tidak valid.")
                return

        break

    # =========================
    # INPUT DATA
    # =========================

    nama_barang = input("Masukkan Nama Barang : ")
    kategori = input("Masukkan Kategori : ")
    stok = int(input("Masukkan Stok : "))
    harga = int(input("Masukkan Harga : "))
    supplier = input("Masukkan Supplier : ")

    # =========================
    # KONFIRMASI DATA
    # =========================

    print("\n========== KONFIRMASI DATA ==========")
    print(f"ID Barang   : {id_baru}")
    print(f"Nama Barang : {nama_barang}")
    print(f"Kategori    : {kategori}")
    print(f"Stok        : {stok}")
    print(f"Harga       : Rp {harga}")
    print(f"Supplier    : {supplier}")

    # =========================
    # KONFIRMASI SIMPAN
    # =========================

    konfirmasi = input("\nSimpan data? (Y/N) : ").upper()

    if konfirmasi == "Y":

        inventory.append({
            "id_barang": id_baru,
            "nama_barang": nama_barang,
            "kategori": kategori,
            "stok": stok,
            "harga": harga,
            "supplier": supplier
        })

        print("\nData berhasil ditambahkan.")

        display_all_data()

    elif konfirmasi == "N":

        print("\nPenambahan data dibatalkan.")

    else:

        print("\nPilihan tidak valid.")


# =========================
# UPDATe FUNCTION
# =========================
def update_menu():

    while True:

        print("\n===== UPDATE ITEM =====")
        print("1. Update Item")
        print("2. Back to Main Menu")

        choice = input("\nSelect Menu : ")

        if choice == "1":
            update_item()

        elif choice == "2":
            break

        else:
            print("\nMenu tidak tersedia.")

def update_item():

    while True:

        id_cari = input("\nMasukkan ID Barang : ").upper()

        found = False

        for item in inventory:

            if item["id_barang"] == id_cari:

                while True:

                    print("\n========== DATA BARANG ==========\n")

                    print(f"ID Barang   : {item['id_barang']}")
                    print(f"Nama Barang : {item['nama_barang']}")
                    print(f"Kategori    : {item['kategori']}")
                    print(f"Stok        : {item['stok']}")
                    print(f"Harga       : Rp {item['harga']}")
                    print(f"Supplier    : {item['supplier']}")

                    print("\n===== UPDATE DATA =====")
                    print("1. Nama Barang")
                    print("2. Kategori")
                    print("3. Stok")
                    print("4. Harga")
                    print("5. Supplier")
                    print("6. Batal")

                    pilihan = input("\nPilih data yang ingin diubah : ")

                    if pilihan == "1":

                        data_baru = input("\nMasukkan Nama Barang Baru : ")

                        print(f"\nNama Barang Lama : {item['nama_barang']}")
                        print(f"Nama Barang Baru : {data_baru}")

                        konfirmasi = input("\nSimpan perubahan? (Y/N) : ").upper()

                        if konfirmasi == "Y":

                            item["nama_barang"] = data_baru

                            print("\nData berhasil diperbarui.")

                        else:

                            print("\nPerubahan dibatalkan.")

                    elif pilihan == "2":

                        data_baru = input("\nMasukkan Kategori Baru : ")

                        print(f"\nKategori Lama : {item['kategori']}")
                        print(f"Kategori Baru : {data_baru}")

                        konfirmasi = input("\nSimpan perubahan? (Y/N) : ").upper()

                        if konfirmasi == "Y":

                            item["kategori"] = data_baru

                            print("\nData berhasil diperbarui.")

                        else:

                            print("\nPerubahan dibatalkan.")

                    elif pilihan == "3":

                        data_baru = int(input("\nMasukkan Stok Baru : "))

                        print(f"\nStok Lama : {item['stok']}")
                        print(f"Stok Baru : {data_baru}")

                        konfirmasi = input("\nSimpan perubahan? (Y/N) : ").upper()

                        if konfirmasi == "Y":

                            item["stok"] = data_baru

                            print("\nData berhasil diperbarui.")

                        else:

                            print("\nPerubahan dibatalkan.")

                    elif pilihan == "4":

                        data_baru = int(input("\nMasukkan Harga Baru : "))

                        print(f"\nHarga Lama : Rp {item['harga']}")
                        print(f"Harga Baru : Rp {data_baru}")

                        konfirmasi = input("\nSimpan perubahan? (Y/N) : ").upper()

                        if konfirmasi == "Y":

                            item["harga"] = data_baru

                            print("\nData berhasil diperbarui.")

                        else:

                            print("\nPerubahan dibatalkan.")

                    elif pilihan == "5":

                        data_baru = input("\nMasukkan Supplier Baru : ")

                        print(f"\nSupplier Lama : {item['supplier']}")
                        print(f"Supplier Baru : {data_baru}")

                        konfirmasi = input("\nSimpan perubahan? (Y/N) : ").upper()

                        if konfirmasi == "Y":

                            item["supplier"] = data_baru

                            print("\nData berhasil diperbarui.")

                        else:

                            print("\nPerubahan dibatalkan.")

                    elif pilihan == "6":

                        return

                    else:

                        print("\nMenu tidak tersedia.")

                found = True
                break

        if not found:

            print("\nData tidak ditemukan.")

            pilihan = input("\nIngin mencoba lagi? (Y/N) : ").upper()

            if pilihan == "Y":

                continue

            elif pilihan == "N":

                return

            else:

                print("\nPilihan tidak valid.")
                return

        break


# =========================
# DELETE FUNCTION
# =========================

def delete_menu():

    while True:

        print("\n===== DELETE ITEM =====")
        print("1. Delete Item")
        print("2. Back to Main Menu")

        choice = input("\nSelect Menu : ")

        if choice == "1":

            delete_item()

        elif choice == "2":

            break

        else:

            print("\nMenu tidak tersedia.")


def delete_item():

    while True:

        id_cari = input("\nMasukkan ID Barang : ").upper()

        found = False

        for item in inventory:

            if item["id_barang"] == id_cari:

                print("\n========== DATA BARANG ==========\n")

                print(f"ID Barang   : {item['id_barang']}")
                print(f"Nama Barang : {item['nama_barang']}")
                print(f"Kategori    : {item['kategori']}")
                print(f"Stok        : {item['stok']}")
                print(f"Harga       : Rp {item['harga']}")
                print(f"Supplier    : {item['supplier']}")

                found = True

                konfirmasi = input("\nYakin ingin menghapus data? (Y/N) : ").upper()

                if konfirmasi == "Y":

                    inventory.remove(item)

                    print("\nData berhasil dihapus.")

                    display_all_data()

                    return

                elif konfirmasi == "N":

                    print("\nPenghapusan data dibatalkan.")
                    return

                else:

                    print("\nPilihan tidak valid.")
                    return

        if not found:

            print("\nData tidak ditemukan.")

            pilihan = input("\nIngin mencoba lagi? (Y/N) : ").upper()

            if pilihan == "Y":

                continue

            elif pilihan == "N":

                return

            else:

                print("\nPilihan tidak valid.")
                return


# =========================
# MAIN MENU
# =========================

def main_menu():

    while True:

        print("\n" + "=" * 45)
        print("         KOPERASI KAMPUNG")
        print(" Warehouse Inventory Management")
        print("=" * 45)

        print("1. Display Stock Data")
        print("2. Add New Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        menu = input("\nSelect Menu : ")

        if menu == "1":
            display_menu()

        elif menu == "2":
            create_menu()

        elif menu == "3":
            update_menu()

        elif menu == "4":
            delete_menu()

        elif menu == "5":
            print("\nTerima kasih telah menggunakan program ini :).")
            break

        else:
            print("\nMenu tidak tersedia.")


# =========================
# RUN PROGRAM
# =========================

main_menu()

