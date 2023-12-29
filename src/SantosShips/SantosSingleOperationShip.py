from SantosShips.SantosShip import SantosShip


class SantosSingleOperationShip(SantosShip):
    def __init__(self, ship: str, flag: str, lenght: float, draft: float, navigation: str, arrival: str, notice: str, 
                 office: str, operation: str, goods: str, weight: float, voyage: str, duv: int, priority: str, terminal: str, ship_type):
        super().__init__(ship, flag, lenght, draft, navigation, arrival, notice, office, voyage, duv,
                         priority, terminal, ship_type)
        self.operation = operation
        self.goods = goods
        self.weight = weight
    
    def __str__(self):
        return  f"Santos Single Operation Ship Description - \n" \
                f"Ship: {self.ship}\n" \
                f"Flag: {self.flag}\n" \
                f"Lenght: {self.lenght}\n" \
                f"Draft: {self.draft}\n" \
                f"Navigation: {self.navigation}\n" \
                f"Arrival: {self.arrival}\n" \
                f"Notice: {self.notice}\n" \
                f"Office: {self.office}\n" \
                f"Operation: {self.operation}\n" \
                f"Goods: {self.goods}\n" \
                f"Weight: {self.weight}\n" \
                f"Voyage: {self.voyage}\n" \
                f"DUV: {self.duv}\n" \
                f"Priority: {self.priority}\n" \
                f"Terminal: {self.terminal}\n" \
                f"Ship type: {self.ship_type}\n" \
                f"--------------------------\n"
