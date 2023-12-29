import json
import csv
import os
import datetime

class ParanaguaShipsList():
    def __init__(self) -> None:
        self.ships: list = []

    def add_ship(self, ship) -> None:
        self.ships.append(ship)
    
    def export_as_dict(self) -> list:
        return [ship.export_as_dict() for ship in self.ships]
    
    def export_as_csv(self) -> str:
        csv = 'ship;agency;arrival;goods;duv;\n'
        for ship in self.ships:
            csv += ship.export_as_csv_line()
        return csv
    
    def export_as_json(self) -> str:
        return json.dumps(self.export_as_dict(), indent=4)
    
    def __str__(self) -> str:
        return f"Paranagua Ships List - \n" \
               f"{self.ships}\n" \
               f"--------------------------\n"
