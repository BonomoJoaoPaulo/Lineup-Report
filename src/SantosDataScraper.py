from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

from PortDataScraper import PortDataScraper
from SantosShips.SantosShip import SantosShip
from SantosShips.SantosSingleOperationShip import SantosSingleOperationShip
from SantosShips.SantosMultiOperationShip import SantosMultiOperationShip
from SantosShips.SantosShipsList import SantosShipsList

class SantosDataScrapper():
    def __init__(self, ship_list, url):
        self.url = url
        self.ships_list = ship_list

    def scrap_data(self):
        print("Scraping data from Santos port...")
        website = "https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/"
        response = requests.get(website)
        content = response.content
        soup = BeautifulSoup(content, "lxml")


        tables = soup.find_all("table")

        table_conter = 0

        for table in tables:
            table_header = table.find('thead')
            table_body = table.find('tbody')

            ship_type = table_header.find('tr').find('th').text

            for ship in table_body.find_all('tr'):
                count_td = 0
                multiple_operation = False

                for ship_data in ship.find_all('td'):
                    match count_td:
                        case 0:
                            ship_name = ship_data.text
                        case 1:
                            ship_flag = ship_data.text
                        case 2:
                            br_tag = ship_data.find('br')
                            if br_tag and br_tag.previous_sibling and br_tag.next_sibling:
                                # The text before the 'br' is the lenght value
                                ship_lenght = br_tag.previous_sibling.strip()
                                # The text after 'br' is the draft value
                                ship_draft = br_tag.next_sibling.strip()
                            else:
                                ship_lenght = ship_data.text
                                ship_draft = None
                        case 3:
                            ship_navigation = ship_data.text
                        case 4:
                            ship_arrival = ship_data.text
                        case 5:
                            ship_notice = ship_data.text
                        case 6:
                            ship_office = ship_data.text
                        case 7:
                            br_tag = ship_data.find('br')
                            if br_tag and (br_tag.previous_sibling and br_tag.next_sibling != " "):
                                multiple_operation = True
                                ship_first_operation = br_tag.previous_sibling.strip()
                                ship_second_operation = br_tag.next_sibling.strip()
                            else:
                                ship_operation = ship_data.text
                        case 8:
                            if multiple_operation:
                                br_tag = ship_data.find('br')
                                ship_first_goods = br_tag.previous_sibling.strip()
                                ship_second_goods = br_tag.next_sibling.strip()
                            else:
                                ship_goods = ship_data.text
                                if ship_goods == "CONTEINERES CHEIOSCONTEINERES CHEIOS":
                                    ship_goods = "CONTEINERES CHEIOS"
                        case 9:
                            if multiple_operation:
                                br_tag = ship_data.find('br')
                                ship_first_weight = br_tag.previous_sibling.strip()
                                ship_second_weight = br_tag.next_sibling.strip()
                                if ship_first_weight == "":
                                    ship_first_weight = "0"
                                if ship_second_weight == "":
                                    ship_second_weight = "0"
                            else:
                                ship_weight = ship_data.text
                                if ship_weight == "":
                                    ship_weight = "0"
                        case 10:
                            ship_voyage = ship_data.text
                        case 11:
                            ship_duv = ship_data.text
                        case 12:
                            ship_priority = ship_data.text
                        case 13:
                            ship_terminal = ship_data.text
                        case default:
                            pass
                    
                    count_td += 1

                if multiple_operation:
                    new_santos_ship = SantosMultiOperationShip(ship_name, ship_flag, ship_lenght, ship_draft,
                                                ship_navigation, ship_arrival, ship_notice, ship_office, ship_first_operation,
                                                ship_second_operation, ship_first_goods, ship_second_goods, ship_first_weight,
                                                ship_second_weight, ship_voyage, ship_duv, ship_priority,
                                                ship_terminal, ship_type)
                else:
                    new_santos_ship = SantosSingleOperationShip(ship_name, ship_flag, ship_lenght, ship_draft,
                                                ship_navigation, ship_arrival, ship_notice, ship_office, ship_operation,
                                                ship_goods, ship_weight, ship_voyage, ship_duv, ship_priority,
                                                ship_terminal, ship_type)

                self.ships_list.add_ship(new_santos_ship)

                #print(new_santos_ship)
