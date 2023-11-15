MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 17000,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30000,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("pilih produk yang diinginkan :")
print(" 1. Espresso : Rp. 17.000 \n 2. Latte : Rp. 25.000 \n 3. Cappucino : Rp.30.000")

pesanan = input("inputkan 1 untuk espresso, 2 untuk latte, dan 3 untuk capuccino \n")
if pesanan in ["1","2","3"]:
    produk = list(MENU.keys())[int(pesanan)-1]
    print(f"Anda telah memilih {produk.capitalize()}.")

    cek_bahan = MENU[produk]["ingredients"]
    bahan_cukup = True

    for bahan in cek_bahan:
        if resources[bahan] < cek_bahan[bahan]:
            bahan_cukup = False
            print(f"maaf bahan {bahan} tidak cukup untuk membuat {produk}")
            break
    if bahan_cukup:
        print(f"Anda dapat membuat {produk.capitalize()}. Silakan siapkan pembayaran Anda.")
    else:
        print("Input tidak valid.")

pembayaran = int(input("Masukkan uang sesuai dengan nama pesanan\n"))
if pembayaran == MENU[produk]["cost"]:
    print("Coffe telah dibuat, terima kasih atas pembeliannya")
elif pembayaran > MENU[produk]["cost"]:
    kembalian = pembayaran - MENU[produk]["cost"]
    print(f"Coffe telah dibuat, terima kasih atas pembeliannya \n Anda telah membayar dengan uang lebih, silakan ambil kembalian sebesar Rp.{kembalian}.")
else:
    kekurangan = MENU[produk]["cost"] - pembayaran
    print(f"Maaf, uang yang dimasukkan kurang. Total yang dibutuhkan adalah Rp.{kekurangan}.")









