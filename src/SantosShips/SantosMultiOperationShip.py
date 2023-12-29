from SantosShips.SantosShip import SantosShip


class SantosMultiOperationShip(SantosShip):
    def __init__(self, ship: str, flag: str, lenght: float, draft: float, navigation: str, arrival: str, notice: str, 
                 office: str, first_operation: str, second_operation: str, first_goods: str, second_goods: str,
                 first_weight: float, second_weight: float, voyage: str, duv: int, priority: str, terminal: str, ship_type):
        super().__init__(ship, flag, lenght, draft, navigation, arrival, notice, office, voyage, duv,
                         priority, terminal, ship_type)
        self.first_operation = first_operation
        self.second_operation = second_operation
        self.first_goods = first_goods
        self.second_goods = second_goods
        self.first_weight = first_weight
        self.second_weight = second_weight
    
    def __str__(self):
        return  f"Santos Multi Operation Ship Description - \n" \
                f"Ship: {self.ship}\n" \
                f"Flag: {self.flag}\n" \
                f"Lenght: {self.lenght}\n" \
                f"Draft: {self.draft}\n" \
                f"Navigation: {self.navigation}\n" \
                f"Arrival: {self.arrival}\n" \
                f"Notice: {self.notice}\n" \
                f"Office: {self.office}\n" \
                f"First Operation: {self.first_operation}\n" \
                f"Second Operation: {self.second_operation}\n" \
                f"First Goods: {self.first_goods}\n" \
                f"Second Goods: {self.second_goods}\n" \
                f"First Weight: {self.first_weight}\n" \
                f"Second Weight: {self.second_weight}\n" \
                f"Voyage: {self.voyage}\n" \
                f"DUV: {self.duv}\n" \
                f"Priority: {self.priority}\n" \
                f"Terminal: {self.terminal}\n" \
                f"Ship type: {self.ship_type}\n" \
                f"--------------------------\n"
