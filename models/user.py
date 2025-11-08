class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"], data["role"])
