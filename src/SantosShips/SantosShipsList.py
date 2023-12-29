import json


class SantosShipsList():
    def __init__(self) -> None:
        self.ships: list = []

    def add_ship(self, ship) -> None:
        self.ships.append(ship)
    
    def export_as_dict(self) -> list:
        return [ship.export_as_dict() for ship in self.ships]
    
    def export_as_csv(self) -> str:
        csv = 'ship;flag;lenght;draft;navigation;arrival;notice;office;first_operation;second_operation;first_goods;second_goods;first_weight;second_weight;voyage;duv;priority;terminal;ship_type\n'
        for ship in self.ships:
            csv += ship.export_as_csv_line()
        return csv
    
    def export_as_json(self) -> str:
        return json.dumps(self.export_as_dict(), indent=4)
    
    def __str__(self) -> str:
        return f"Santos Ships List - \n" \
               f"{self.ships}\n" \
               f"--------------------------\n"
