from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

from PortDataScraper import PortDataScraper
from SantosShips.SantosShip import SantosShip

class SantosDataScrapper(PortDataScraper):
    def __init__(self, url):
        super().__init__(url)
        #self.data = self.scrap_data()

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
                for ship_data in ship.find_all('td'):
                    match count_td:
                        case 0:
                            ship_name = ship_data.text
                        case 1:
                            ship_flag = ship_data.text
                        case 2:
                            ship_lenght = ship_data.text
                        case 3:
                            ship_draft = ship_data.text
                        case 4:
                            ship_navigation = ship_data.text
                        case 5:
                            ship_arrival = ship_data.text
                        case 6:
                            ship_notice = ship_data.text
                        case 7:
                            ship_operation = ship_data.text
                        case 8:
                            ship_goods = ship_data.text
                        case 9:
                            ship_weight = ship_data.text
                        case 10:
                            ship_voyage = ship_data.text
                        case 11:
                            ship_duv = ship_data.text
                        case 12:
                            ship_priority = ship_data.text
                        case 13:
                            ship_terminal = ship_data.text
                        case default:
                            print("Nothing to do with column ", count_td, "\n")
                    
                    count_td += 1

                new_santos_ship = SantosShip(ship_name, ship_flag, ship_lenght, ship_draft,
                                              ship_navigation, ship_arrival, ship_notice, ship_operation,
                                              ship_goods, ship_weight, ship_voyage, ship_duv, ship_priority,
                                              ship_terminal, ship_type)

                print(new_santos_ship)
