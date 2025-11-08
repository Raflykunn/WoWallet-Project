from models.user import User
from utils.file_manager import FileManager
from utils.constants import USERS_FILE
class UserManager:
    def __init__(self):
        self.users = [User.from_dict(u) for u in FileManager.read_json(USERS_FILE)]

    def login(self, role_expected):
        print(f"\n=== Login sebagai {role_expected} ===")
        username = input("Username: ").strip()
        if not username:
            print("Username tolong diisi.")
            return None
        password = input("Password: ").strip()
        if not password:
            print("Password tolong diisi.")
            return None
        for user in self.users:
            if (user.username == username and user.password == password and
                    user.role.lower() == role_expected.lower()):
                print(f"Login sukses sebagai {role_expected}.")
                return user
        print("Login gagal: username/password/role salah.")
        return None