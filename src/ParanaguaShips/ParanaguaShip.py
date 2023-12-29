class ParanaguaShip():
    def __init__(self, ship: str, agency: str, arrival: str, goods: str, duv: int):
        self.ship = ship
        self.agency = agency
        self.arrival = arrival
        self.goods = goods
        self.duv = duv

    def export_as_dict(self) -> dict:
        return {
            'ship': self.ship,
            'agency': self.agency,
            'arrival': self.arrival,
            'goods': self.goods,
            'duv': self.duv,
        }
    
    def export_as_csv_line(self) -> str:
        return f"{self.ship};{self.agency};{self.arrival};{self.goods};{self.duv};\n"
        
    def __str__(self) -> str:
        return f"Ship: {self.ship} - Agency: {self.agency} - Arrival: {self.arrival} - Goods: {self.goods} - DUV: {self.duv}"
