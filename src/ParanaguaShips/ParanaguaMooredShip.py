from ParanaguaShips.ParanaguaShip import ParanaguaShip


class ParanaguaMooredShip(ParanaguaShip):
    def __init__(self, programation: int, duv: int, cradle: str, ship: str, imo: str, loa: float, dwt: float,
                 board: str, direction: str, agency: str, operator: str, goods: str, mooring: str, arrival: str,
                 ets: str, tons_per_day: float, expected: float, realized: float, operator_balance: float, total_balance: float):
        super().__init__(ship, agency, arrival, goods, duv)
        self.programation = programation
        self.cradle = cradle
        self.imo = imo
        self.loa = loa 
        self.dwt = dwt
        self.board = board
        self.direction = direction
        self.operator = operator
        self.mooring = mooring
        self.ets = ets
        self.tons_per_day = tons_per_day
        self.expected = expected
        self.realized = realized
        self.operator_balance = operator_balance
        self.total_balance = total_balance

    def __str__(self):
        return f"Programation: {self.programation}\n" \
               f"DUV: {self.duv}\n" \
               f"Cradle: {self.cradle}\n" \
               f"Ship: {self.ship}\n" \
               f"IMO: {self.imo}\n" \
               f"LOA: {self.loa}\n" \
               f"DWT: {self.dwt}\n" \
               f"Board: {self.board}\n" \
               f"Direction: {self.direction}\n" \
               f"Agency: {self.agency}\n" \
               f"Operator: {self.operator}\n" \
               f"Goods: {self.goods}\n" \
               f"Mooring: {self.mooring}\n" \
               f"Arrival: {self.arrival}\n" \
               f"ETS: {self.ets}\n" \
               f"Tons per day: {self.tons_per_day}\n" \
               f"expected: {self.expected}\n" \
               f"Realized: {self.realized}\n" \
               f"Operator balance: {self.operator_balance}\n" \
               f"Total balance: {self.total_balance}\n" \
               f"--------------------------\n"
