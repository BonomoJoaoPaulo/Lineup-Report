class SantosShip():
    def __init__(self, ship: str, flag: str, lenght: float, draft: float, navigation: str, arrival: str, notice: str, 
                 operation: str, goods: str, weight: float, voyage: str, duv: int, priority: str, terminal: str, ship_type):
        self.ship = ship
        self.flag = flag
        self.lenght = lenght
        self.draft = draft
        self.navigation = navigation
        self.arrival = arrival
        self.notice = notice
        self.operation = operation
        self.goods = goods
        self.weight = weight
        self.voyage = voyage
        self.duv = duv
        self.priority = priority
        self.terminal = terminal
        self.ship_type = ship_type
    
    def __str__(self):
        return f"Ship: {self.ship}\n" \
               f"Flag: {self.flag}\n" \
                f"Lenght: {self.lenght}\n" \
                f"Draft: {self.draft}\n" \
                f"Navigation: {self.navigation}\n" \
                f"Arrival: {self.arrival}\n" \
                f"Notice: {self.notice}\n" \
                f"Operation: {self.operation}\n" \
                f"Goods: {self.goods}\n" \
                f"Weight: {self.weight}\n" \
                f"Voyage: {self.voyage}\n" \
                f"DUV: {self.duv}\n" \
                f"Priority: {self.priority}\n" \
                f"Terminal: {self.terminal}\n" \
                f"Ship type: {self.ship_type}\n" \
                f"--------------------------\n"
