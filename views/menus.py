from controllers.product_manager import ProductManager
from controllers.transaction_manager import TransactionManager
from views.dashboard import Dashboard

def admin_menu(user, product_manager: ProductManager, transaction_manager: TransactionManager):
    while True:
        print("\n--- MENU ADMIN ---")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Edit Produk")
        print("4. Hapus Produk")
        print("5. Input Stok Masuk")
        print("6. Transaksi Penjualan")
        print("7. Dashboard")
        print("8. Lihat Riwayat Transaksi")
        print("9. Ekspor Laporan Harian")
        print("0. Logout")
        choice = input("Pilih: ").strip()
        if not choice:
            print("Pilihan tolong diisi.")
            continue
        if choice == "1":
            product_manager.add_product()
        elif choice == "2":
            product_manager.view_all_products()
        elif choice == "3":
            product_manager.edit_product()
        elif choice == "4":
            product_manager.delete_product()
        elif choice == "5":
            product_manager.input_stock_masuk()
        elif choice == "6":
            transaction_manager.sell_product(user, product_manager)
        elif choice == "7":
            Dashboard.print_dashboard(transaction_manager, product_manager)
        elif choice == "8":
            filter_date = input("Filter by tanggal (YYYY-MM-DD, kosong untuk semua): ").strip() or None
            transaction_manager.view_transactions(filter_date)
        elif choice == "9":
            report_date = input("Tanggal laporan (YYYY-MM-DD, kosong untuk hari ini): ").strip() or None
            transaction_manager.generate_daily_report(report_date)
        elif choice == "0":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.")

def kasir_menu(user, product_manager: ProductManager, transaction_manager: TransactionManager):
    while True:
        print("\n--- MENU KASIR ---")
        print("1. Transaksi Penjualan")
        print("2. Lihat Semua Produk")
        print("3. Dashboard Ringkas")
        print("4. Lihat Riwayat Transaksi")
        print("0. Logout")
        choice = input("Pilih: ").strip()
        if not choice:
            print("Pilihan tolong diisi.")
            continue
        if choice == "1":
            transaction_manager.sell_product(user, product_manager)
        elif choice == "2":
            product_manager.view_all_products()
        elif choice == "3":
            Dashboard.print_dashboard(transaction_manager, product_manager)
        elif choice == "4":
            filter_date = input("Filter by tanggal (YYYY-MM-DD, kosong untuk semua): ").strip() or None
            transaction_manager.view_transactions(filter_date)
        elif choice == "0":
            print("Logout...")
            break
        else:
            print("Pilihan tidak valid.")