class Transaction:
    def __init__(self, id_, time, product_id, product_name, qty, total, profit, cashier):
        self.id = id_
        self.time = time
        self.product_id = product_id
        self.product_name = product_name
        self.qty = qty
        self.total = total
        self.profit = profit
        self.cashier = cashier

    def to_dict(self):
        return {
            "id": self.id,
            "time": self.time,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "qty": self.qty,
            "total": self.total,
            "profit": self.profit,
            "cashier": self.cashier
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["time"],
            data["product_id"],
            data["product_name"],
            data["qty"],
            data["total"],
            data["profit"],
            data["cashier"]
        )