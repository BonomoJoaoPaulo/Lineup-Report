from SantosShips.SantosShip import SantosShip


class SantosMultiOperationShip(SantosShip):
    def __init__(self, ship: str, flag: str, lenght: float, draft: float, navigation: str, arrival: str, notice: str, 
                 office: str, first_operation: str, second_operation: str, first_goods: str, second_goods: str,
                 first_weight: float, second_weight: float, voyage: str, duv: int, priority: str, terminal: str, ship_type) -> None:
        super().__init__(ship, flag, lenght, draft, navigation, arrival, notice, office, voyage, duv,
                         priority, terminal, ship_type)
        self.first_operation = first_operation
        self.second_operation = second_operation
        self.first_goods = first_goods
        self.second_goods = second_goods
        self.first_weight = first_weight
        self.second_weight = second_weight

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
            'first_operation': self.first_operation,
            'second_operation': self.second_operation,
            'first_goods': self.first_goods,
            'second_goods': self.second_goods,
            'first_weight': self.first_weight,
            'second_weight': self.second_weight,
            'voyage': self.voyage,
            'duv': self.duv,
            'priority': self.priority,
            'terminal': self.terminal,
            'ship_type': self.ship_type
        }
    
    def export_as_csv_line(self) -> str:
        return f"{self.ship};{self.flag};{self.lenght};{self.draft};{self.navigation};{self.arrival};" \
               f"{self.notice};{self.office};{self.first_operation};{self.second_operation};{self.first_goods};" \
               f"{self.second_goods};{self.first_weight};{self.second_weight};{self.voyage};{self.duv};" \
               f"{self.priority};{self.terminal};{self.ship_type}\n"

    def __str__(self) -> str:
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
