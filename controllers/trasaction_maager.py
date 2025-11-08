import os
from datetime import datetime, date, timedelta
from collections import defaultdict, Counter
from models.transaction import Transaction
from utils.file_manager import FileManager
from utils.constants import TRANSACTIONS_FILE, REPORTS_DIR
from controllers.product_manager import ProductManager

class TransactionManager:
    def __init__(self):
        self.transactions = [Transaction.from_dict(t) for t in FileManager.read_json(TRANSACTIONS_FILE)]

    def save_transactions(self):
        data = [t.to_dict() for t in self.transactions]
        FileManager.write_json(TRANSACTIONS_FILE, data)

    def get_next_id(self):
        if not self.transactions:
            return 1
        return max(t.id for t in self.transactions) + 1

    def sell_product(self, user, product_manager: ProductManager):
        if not product_manager.products:
            print("Tidak ada produk untuk dijual.")
            return
        product_manager.view_all_products()
        pid_str = input("Masukkan ID produk yang dibeli: ").strip()
        if not pid_str:
            print("ID produk tolong diisi.")
            return
        qty_str = input("Masukkan jumlah beli: ").strip()
        if not qty_str:
            print("Jumlah beli tolong diisi.")
            return
        try:
            pid = int(pid_str)
            qty = int(qty_str)
        except ValueError:
            print("Input tidak valid.")
            return

        p = product_manager.find_by_id(pid)
        if not p:
            print("Produk tidak ditemukan.")
            return
        if qty <= 0:
            print("Jumlah harus > 0.")
            return
        if p.stok < qty:
            print(f"Stok tidak cukup. Stok sekarang: {p.stok}")
            return

        total = qty * p.harga_jual
        profit = qty * (p.harga_jual - p.harga_modal)

        p.stok -= qty # Kurangi stok produk
        product_manager.save_products()

        tid = self.get_next_id()
        txn = Transaction(
            tid, product_manager._now_iso(), p.id, p.name, qty,
            round(total, 2), round(profit, 2), user.username
        )
        self.transactions.append(txn)
        self.save_transactions() # Simpan transaksi

        print("=== Transaksi Sukses ===")
        print(f"Produk: {p.name}")
        print(f"Jumlah: {qty}")
        print(f"Total harga: Rp {total:.2f}")
        print(f"Profit transaksi: Rp {profit:.2f}")
        print(f"Stok tersisa: {p.stok}")