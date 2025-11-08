"""
WoWallet - A simple CLI wallet/store app (complete with all 7 features)
Includes login type selection (Admin / Kasir)
"""
from utils.file_manager import FileManager
from controllers.user_manager import UserManager
from controllers.product_manager import ProductManager
from controllers.transaction_manager import TransactionManager
from views.menus import admin_menu, kasir_menu

def main():
    FileManager.ensure_data_files()
    user_manager = UserManager()
    product_manager = ProductManager()
    transaction_manager = TransactionManager()
    print("=== Selamat Datang di WoWallet ===")
    while True:
        print("\nPilih jenis login:")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Kasir")
        print("0. Keluar")
        opt = input("Pilih: ").strip()
        if opt == "1":
            user = user_manager.login("Admin")
            if user:
                admin_menu(user, product_manager, transaction_manager)
        elif opt == "2":
            user = user_manager.login("Kasir")
            if user:
                kasir_menu(user, product_manager, transaction_manager)
        elif opt == "0":
            print("Keluar dari aplikasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()