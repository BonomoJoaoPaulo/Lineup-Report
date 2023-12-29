from ParanaguaShips.ParanaguaShip import ParanaguaShip


class ParanaguaDispatchedShip(ParanaguaShip):
    def __init__(self, programation: int, duv: int, cradle: str, ship: str, imo: str, loa: float, dwt: float,
                 board: str, direction: str, agency: str, operator: str, goods: str, arrival: str,
                 ets: str, undocking: str, predict: float):
        super().__init__(ship, agency, arrival, goods, duv)
        self.programation = programation
        self.cradle = cradle
        self.imo = imo
        self.loa = loa 
        self.dwt = dwt
        self.board = board
        self.direction = direction
        self.operator = operator
        self.ets = ets
        self.undocking = undocking
        self.predict = predict

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
               f"Arrival: {self.arrival}\n" \
               f"ETS: {self.ets}\n" \
               f"Undocking: {self.undocking}\n" \
               f"Predict: {self.predict}\n" \
               f"--------------------------\n"
