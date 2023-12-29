import json

from ParanaguaDataScraper import ParanaguaDataScraper as pds
from SantosDataScraper import SantosDataScrapper as sds
from SantosShips.SantosMultiOperationShip import SantosMultiOperationShip

#paranagua_data_scraper = pds("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")
#paranagua_data_scraper.scrap_data()

santos_data_scraper = sds("https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/")
santos_data_scraper.scrap_data()

csv_file = open("santos_ships.csv", "w")
csv_file.write(santos_data_scraper.ships_list.export_as_csv())
csv_file.close()

json_file = open("santos_ships.json", "w")
json_file.write(santos_data_scraper.ships_list.export_as_json())
json_file.close()

container_ships = []
for ship in santos_data_scraper.ships_list.ships:
    if type(ship) == SantosMultiOperationShip:
        if ship.first_goods == "CONTEINERES CHEIOS" or ship.second_goods == "CONTEINERES CHEIOS":
            container_ships.append(ship)
    else:
        if ship.goods == "CONTEINERES CHEIOS":
            container_ships.append(ship)

print(f"Total de navios de contêineres: {len(container_ships)}")
container_file = open("container_ships.json", "w")
container_file.write(json.dumps([ship.export_as_dict() for ship in container_ships], indent=4))
container_file.close()
