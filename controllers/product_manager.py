from datetime import datetime
from models.product import Product
from utils.file_manager import FileManager
from utils.constants import PRODUCTS_FILE, LOW_STOCK_THRESHOLD
class ProductManager:
    def __init__(self):
        self.products = [Product.from_dict(p) for p in FileManager.read_json(PRODUCTS_FILE)]

    def save_products(self):
        data = [p.to_dict() for p in self.products]
        FileManager.write_json(PRODUCTS_FILE, data)

    def get_next_id(self):
        if not self.products:
            return 1
        return max(p.id for p in self.products) + 1

    def add_product(self):
        pid = self.get_next_id()
        name = input("Nama produk: ").strip()
        if not name:
            print("Nama produk tolong diisi.")
            return
        try:
            harga_modal_str = input("Harga modal: ").strip()
            if not harga_modal_str:
                print("Harga modal tolong diisi.")
                return
            harga_modal = float(harga_modal_str)
            harga_jual_str = input("Harga jual: ").strip()
            if not harga_jual_str:
                print("Harga jual tolong diisi.")
                return
            harga_jual = float(harga_jual_str)
            stok_str = input("Stok awal: ").strip()
            if not stok_str:
                print("Stok awal tolong diisi.")
                return
            stok = int(stok_str)
        except ValueError:
            print("Input angka tidak valid.")
            return
        product = Product(pid, name, harga_modal, harga_jual, stok, self._now_iso())
        self.products.append(product)
        self.save_products()
        print(f"Produk ditambahkan: {product.to_dict()}")

    def view_all_products(self):
        if not self.products:
            print("Belum ada produk.")
            return
        print("\nDaftar Produk:")
        print("{:<4} {:<20} {:>10} {:>10} {:>8}".format("ID", "Nama", "Modal", "Jual", "Stok"))
        for p in self.products:
            print("{:<4} {:<20} {:>10.2f} {:>10.2f} {:>8}".format(
                p.id, p.name, p.harga_modal, p.harga_jual, p.stok))
        print()

    def find_by_id(self, pid):
        for p in self.products:
            if p.id == pid:
                return p
        return None

    def edit_product(self):
        pid_str = input("Masukkan ID produk yang ingin di-edit: ").strip()
        if not pid_str:
            print("ID produk tolong diisi.")
            return
        try:
            pid = int(pid_str)
        except ValueError:
            print("ID tidak valid.")
            return
        p = self.find_by_id(pid)
        if not p:
            print("Produk tidak ditemukan.")
            return
        print("Biarkan kosong jika tidak ingin mengubah field tersebut.")
        new_name = input(f"Nama ({p.name}): ").strip()
        new_harga_modal = input(f"Harga modal ({p.harga_modal}): ").strip()
        new_harga_jual = input(f"Harga jual ({p.harga_jual}): ").strip()
        new_stok = input(f"Stok ({p.stok}): ").strip()
        if new_name:
            p.name = new_name
        if new_harga_modal:
            try:
                p.harga_modal = float(new_harga_modal)
            except ValueError:
                print("Harga modal tidak valid; tidak diubah.")
        if new_harga_jual:
            try:
                p.harga_jual = float(new_harga_jual)
            except ValueError:
                print("Harga jual tidak valid; tidak diubah.")
        if new_stok:
            try:
                p.stok = int(new_stok)
            except ValueError:
                print("Stok tidak valid; tidak diubah.")
        self.save_products()
        print("Produk berhasil diupdate.")

    def delete_product(self):
        pid_str = input("Masukkan ID produk yang ingin dihapus: ").strip()
        if not pid_str:
            print("ID produk tolong diisi.")
            return
        try:
            pid = int(pid_str)
        except ValueError:
            print("ID tidak valid.")
            return
        self.products = [p for p in self.products if p.id != pid]
        self.save_products()
        print("Produk dihapus (jika ID ada).")

    def input_stock_masuk(self):
        pid_str = input("Masukkan ID produk untuk stok masuk: ").strip()
        if not pid_str:
            print("ID produk tolong diisi.")
            return
        qty_str = input("Jumlah stok masuk: ").strip()
        if not qty_str:
            print("Jumlah stok tolong diisi.")
            return
        try:
            pid = int(pid_str)
            qty = int(qty_str)
        except ValueError:
            print("Input tidak valid.")
            return
        p = self.find_by_id(pid)
        if p:
            p.stok += qty
            self.save_products()
            print(f"Stok produk {p.name} bertambah {qty}. Stok sekarang: {p.stok}")
        else:
            print("Produk tidak ditemukan.")

    def get_low_stock(self):
        return [p for p in self.products if p.stok < LOW_STOCK_THRESHOLD]
    def _now_iso(self):
        return datetime.now().isoformat(sep=" ", timespec="seconds")