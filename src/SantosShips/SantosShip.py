class SantosShip():
    def __init__(self, ship: str, flag: str, lenght: float, draft: float, navigation: str, arrival: str, notice: str, 
                 office: str, voyage: str, duv: int, priority: str, terminal: str, ship_type) -> None:
        self.ship = ship
        self.flag = flag
        self.lenght = lenght
        self.draft = draft
        self.navigation = navigation
        self.arrival = arrival
        self.notice = notice
        self.office = office
        self.voyage = voyage
        self.duv = duv
        self.priority = priority
        self.terminal = terminal
        self.ship_type = ship_type

    def export_as_dict(self):
        pass

    def export_as_csv_line(self):
        pass

    def __str__(self) -> str:
        return  f"Santos Ship Description - \n" \
                f"Ship: {self.ship}\n" \
                f"Flag: {self.flag}\n" \
                f"Lenght: {self.lenght}\n" \
                f"Draft: {self.draft}\n" \
                f"Navigation: {self.navigation}\n" \
                f"Arrival: {self.arrival}\n" \
                f"Notice: {self.notice}\n" \
                f"Office: {self.office}\n" \
                f"Voyage: {self.voyage}\n" \
                f"DUV: {self.duv}\n" \
                f"Priority: {self.priority}\n" \
                f"Terminal: {self.terminal}\n" \
                f"Ship type: {self.ship_type}\n" \
                f"--------------------------\n"
