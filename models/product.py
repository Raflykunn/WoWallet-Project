class Product:
    def __init__(self, id_, name, harga_modal, harga_jual, stok, created_at):
        self.id = id_
        self.name = name
        self.harga_modal = harga_modal
        self.harga_jual = harga_jual
        self.stok = stok
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "harga_modal": self.harga_modal,
            "harga_jual": self.harga_jual,
            "stok": self.stok,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["harga_modal"],
            data["harga_jual"],
            data["stok"],
            data["created_at"]
        )