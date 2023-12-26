from MooredShip import MooredShip


class ParanaguaMooredShip(MooredShip):
    def __init__(self, ship: str, agency: str, arrival: str, goods: str, duv: int):
        super().__init__(ship, agency, arrival, goods, duv)
