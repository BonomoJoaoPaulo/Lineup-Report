from ParanaguaShips.ParanaguaShip import ParanaguaShip


class ParanaguaSupportShip(ParanaguaShip):
    def __init__(self, programation: int, duv: int, cradle: str, ship: str, imo: str, loa: float, dwt: float,
                 operation_type: str, status: str, agency: str, operator: str,
                 arrival: str, ets: str):
        super().__init__(ship, agency, arrival, 0, duv)
        self.programation = programation
        self.cradle = cradle
        self.imo = imo
        self.loa = loa 
        self.dwt = dwt
        self.operation_type = operation_type
        self.status = status
        self.operator = operator
        self.ets = ets

    def __str__(self):
        return f"Programation: {self.programation}\n" \
               f"DUV: {self.duv}\n" \
               f"Cradle: {self.cradle}\n" \
               f"Ship: {self.ship}\n" \
               f"IMO: {self.imo}\n" \
               f"LOA: {self.loa}\n" \
               f"DWT: {self.dwt}\n" \
               f"Operation type: {self.operation_type}\n" \
               f"Status: {self.status}\n" \
               f"Agency: {self.agency}\n" \
               f"Operator: {self.operator}\n" \
               f"Arrival: {self.arrival}\n" \
               f"ETS: {self.ets}\n" \
               f"--------------------------\n"
