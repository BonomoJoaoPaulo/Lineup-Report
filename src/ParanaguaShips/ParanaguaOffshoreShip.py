from ParanaguaShips.ParanaguaShip import ParanaguaShip


class ParanaguaOffshoreShip(ParanaguaShip):
    def __init__(self, programation: int, duv: int, cradle: str, ship: str, imo: str, loa: float, dwt: float,
                 direction: str, agency: str, operator: str, goods: str,
                 eta: str, ets: str, arrival: str, expected: float, cal_arrival: float, cal_departure: float):
        super().__init__(ship, agency, arrival, goods, duv)
        self.programation = programation
        self.cradle = cradle
        self.imo = imo
        self.loa = loa 
        self.dwt = dwt
        self.direction = direction
        self.operator = operator
        self.eta = eta
        self.ets = ets
        self.expected = expected
        self.cal_arrival = cal_arrival
        self.cal_departure = cal_departure

    def __str__(self):
        return f"Programation: {self.programation}\n" \
               f"DUV: {self.duv}\n" \
               f"Cradle: {self.cradle}\n" \
               f"Ship: {self.ship}\n" \
               f"IMO: {self.imo}\n" \
               f"LOA: {self.loa}\n" \
               f"DWT: {self.dwt}\n" \
               f"Direction: {self.direction}\n" \
               f"Agency: {self.agency}\n" \
               f"Operator: {self.operator}\n" \
               f"Goods: {self.goods}\n" \
               f"ETA: {self.eta}\n" \
               f"ETS: {self.ets}\n" \
               f"Arrival: {self.arrival}\n" \
               f"Expected: {self.expected}\n" \
               f"Calculated arrival: {self.cal_arrival}\n" \
               f"Calculated departure: {self.cal_departure}\n" \
               f"--------------------------\n"
