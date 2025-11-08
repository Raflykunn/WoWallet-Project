import json
import os
from utils.constants import USERS_FILE, PRODUCTS_FILE, TRANSACTIONS_FILE, REPORTS_DIR

class FileManager:
    @staticmethod
    def ensure_data_files():
        if not os.path.exists(REPORTS_DIR):
            os.makedirs(REPORTS_DIR)
        if not os.path.exists(USERS_FILE):
            default_users = [
                {"username": "admin", "password": "adminpass", "role": "Admin"},
                {"username": "kasir", "password": "kasirpass", "role": "Kasir"},
            ]
            FileManager.write_json(USERS_FILE, default_users)
        if not os.path.exists(PRODUCTS_FILE):
            FileManager.write_json(PRODUCTS_FILE, [])
        if not os.path.exists(TRANSACTIONS_FILE):
            FileManager.write_json(TRANSACTIONS_FILE, [])

    @staticmethod
    def read_json(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    @staticmethod
    def write_json(path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def write_txt(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)