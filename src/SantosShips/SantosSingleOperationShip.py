from SantosShips.SantosShip import SantosShip


class SantosSingleOperationShip(SantosShip):
    def __init__(self, ship: str, flag: str, lenght: float, draft: float, navigation: str, arrival: str, notice: str, 
                 office: str, operation: str, goods: str, weight: float, voyage: str, duv: int,
                 priority: str, terminal: str, ship_type) -> None:
        super().__init__(ship, flag, lenght, draft, navigation, arrival, notice, office, voyage, duv,
                         priority, terminal, ship_type)
        self.operation = operation
        self.goods = goods
        self.weight = weight
    
    def export_as_dict(self) -> dict:
        return {
            'ship': self.ship,
            'flag': self.flag,
            'lenght': self.lenght,
            'draft': self.draft,
            'navigation': self.navigation,
            'arrival': self.arrival,
            'notice': self.notice,
            'office': self.office,
            'operation': self.operation,
            'goods': self.goods,
            'weight': self.weight,
            'voyage': self.voyage,
            'duv': self.duv,
            'priority': self.priority,
            'terminal': self.terminal,
            'ship_type': self.ship_type
        }

    def export_as_csv_line(self) -> str:
        return f"{self.ship};{self.flag};{self.lenght};{self.draft};{self.navigation};{self.arrival};" \
               f"{self.notice};{self.office};{self.operation};{0};{self.goods};{0};{self.weight};{0};{self.voyage};" \
               f"{self.duv};{self.priority};{self.terminal};{self.ship_type}\n"

    def __str__(self) -> str:
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
