from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

from ParanaguaShips.ParanaguaMooredShip import ParanaguaMooredShip
from ParanaguaShips.ParanaguaProgrammedShip import ParanaguaProgrammedShip
from ParanaguaShips.ParanaguaRedockingShip import ParanaguaRedockingShip
from ParanaguaShips.ParanaguaOffshoreShip import ParanaguaOffshoreShip
from ParanaguaShips.ParanaguaExpectedShip import ParanaguaExpectedShip
from ParanaguaShips.ParanaguaSupportShip import ParanaguaSupportShip
from ParanaguaShips.ParanaguaDispatchedShip import ParanaguaDispatchedShip

class ParanaguaDataScraper():
    def __init__(self, ships_list, url):
        self.url = url
        self.ships_list = ships_list

    def scrap_data(self):
        print("Scraping data from Paranaguá port...")
        website = "https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo"
        response = requests.get(website)
        content = response.text

        soup = BeautifulSoup(content, 'lxml')

        tables = soup.find_all('table', class_="table table-bordered table-striped table-hover")

        for table in tables:
            table_header = table.find('thead')
            table_body = table.find('tbody')

            if table_header.find('th', text="ATRACADOS") is not None:
                #print(f"Scraping data from table 'ATRACADOS'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                board = data_ship.get_text()
                            case 9:
                                direction = data_ship.get_text()
                            case 10:
                                agency = data_ship.get_text()
                            case 11:
                                operator = data_ship.get_text()
                            case 12:
                                goods = data_ship.get_text()
                            case 13:
                                mooring = data_ship.get_text()
                            case 14:
                                arrival = data_ship.get_text()
                            case 15:
                                ets = data_ship.get_text()
                            case 16:
                                tons_per_day = data_ship.get_text()
                            case 17:
                                # Substituir "," por "." para converter para float
                                string_without_commas = data_ship.get_text().replace(",", ".")
                                # Remover pontos
                                final_string = string_without_commas.replace(".", "")
                                expected = float(final_string.split()[0])
                            case 18:
                                realized = data_ship.get_text()
                            case 19:
                                operator_balance = data_ship.get_text()
                            case 20:
                                total_balance = data_ship.get_text()
                            case default:
                                pass

                        count_td += 1
                    
                    new_paranagua_moored_ship = ParanaguaMooredShip(programation, duv, cradle, ship, imo, loa, dwt, board,
                                                                    direction, agency, operator, goods, mooring, arrival, ets,
                                                                    tons_per_day, expected, realized, operator_balance, total_balance)

                    self.ships_list.add_ship(new_paranagua_moored_ship)

                    #print(new_paranagua_moored_ship)

            elif table_header.find('th', text="PROGRAMADOS") is not None:
                #print(f"Scraping data from table 'PROGRAMADOS'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                board = data_ship.get_text()
                            case 9:
                                direction = data_ship.get_text()
                            case 10:
                                agency = data_ship.get_text()
                            case 11:
                                operator = data_ship.get_text()
                            case 12:
                                goods = data_ship.get_text()
                            case 13:
                                arrival = data_ship.get_text()
                            case 14:
                                etb = data_ship.get_text()
                            case 15:
                                ets = data_ship.get_text()
                            case 16:
                                # Substituir "," por "." para converter para float
                                string_without_commas = data_ship.get_text().replace(",", ".")
                                # Remover pontos
                                final_string = string_without_commas.replace(".", "")
                                expected = float(final_string.split()[0])
                            case default:
                                pass

                        count_td += 1
                    
                    new_paranagua_programmed_ship = ParanaguaProgrammedShip(programation, duv, cradle, ship, imo, loa, dwt, board,
                                                                            direction, agency, operator, goods, arrival, etb, ets,
                                                                            expected)
                    self.ships_list.add_ship(new_paranagua_programmed_ship)

                    #print(new_paranagua_programmed_ship)
                    
            elif table_header.find('th', text="AO LARGO PARA REATRACAÇÃO") is not None:
                #print(f"Scraping data from table 'AO LARGO PARA REATRACAÇÃO'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                board = data_ship.get_text()
                            case 9:
                                direction = data_ship.get_text()
                            case 10:
                                agency = data_ship.get_text()
                            case 11:
                                operator = data_ship.get_text()
                            case 12:
                                goods = data_ship.get_text()
                            case 13:
                                mooring = data_ship.get_text()
                            case 14:
                                arrival = data_ship.get_text()
                            case 15:
                                ets = data_ship.get_text()
                            case 16:
                                undocking = data_ship.get_text()
                            case 17:
                                # Substituir "," por "." para converter para float
                                string_without_commas = data_ship.get_text().replace(",", ".")
                                # Remover pontos
                                final_string = string_without_commas.replace(".", "")
                                expected = float(final_string.split()[0])
                            case 18:
                                realized = data_ship.get_text()
                            case 19:
                                balance = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    new_paranagua_redocking_ship = ParanaguaRedockingShip(programation, duv, cradle, ship, imo, loa, dwt, board,
                                                                            direction, agency, operator, goods, mooring, arrival, ets,
                                                                            undocking, expected, realized, balance)
                    self.ships_list.add_ship(new_paranagua_redocking_ship)
                    
                    #print(new_paranagua_redocking_ship) 
            
            elif table_header.find('th', text="AO LARGO") is not None:
                #print(f"Scraping data from table 'AO LARGO'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                direction = data_ship.get_text()
                            case 9:
                                agency = data_ship.get_text()
                            case 10:
                                operator = data_ship.get_text()
                            case 11:
                                goods = data_ship.get_text()
                            case 12:
                                eta = data_ship.get_text()
                            case 13:
                                ets = data_ship.get_text()
                            case 14:
                                arrival = data_ship.get_text()
                            case 15:
                                # Substituir "," por "." para converter para float
                                string_without_commas = data_ship.get_text().replace(",", ".")
                                # Remover pontos
                                final_string = string_without_commas.replace(".", "")
                                expected = float(final_string.split()[0])
                            case 16:
                                cal_arrival = data_ship.get_text()
                            case 17:
                                cal_departure = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    new_paranagua_offshore_ship = ParanaguaOffshoreShip(programation, duv, cradle, ship, imo, loa, dwt, direction,
                                                                            agency, operator, goods, eta, ets, arrival, expected,
                                                                            cal_arrival, cal_departure)
                    self.ships_list.add_ship(new_paranagua_offshore_ship)
                    
                    #print(new_paranagua_offshore_ship)
            
            elif table_header.find('th', text="ESPERADOS") is not None:
                #print(f"Scraping data from table 'ESPERADOS'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                direction = data_ship.get_text()
                            case 9:
                                agency = data_ship.get_text()
                            case 10:
                                operator = data_ship.get_text()
                            case 11:
                                goods = data_ship.get_text()
                            case 12:
                                eta = data_ship.get_text()
                            case 13:
                                ets = data_ship.get_text()
                            case 14:
                                # Substituir "," por "." para converter para float
                                string_without_commas = data_ship.get_text().replace(",", ".")
                                # Remover pontos
                                final_string = string_without_commas.replace(".", "")
                                expected = float(final_string.split()[0])
                            case 15:
                                cal_arrival = data_ship.get_text()
                            case 16:
                                cal_departure = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    new_paranagua_expected_ship = ParanaguaExpectedShip(programation, duv, cradle, ship, imo, loa, dwt, direction,
                                                                            agency, operator, goods, eta, ets, expected, cal_arrival,
                                                                            cal_departure)
                    self.ships_list.add_ship(new_paranagua_expected_ship)
                    
                    #print(new_paranagua_expected_ship)

            elif table_header.find('th', text="APOIO PORTUÁRIO / OUTROS") is not None:
                #print(f"Scraping data from table 'APOIO PORTUÁRIO / OUTROS'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                operation_type = data_ship.get_text()
                            case 9:
                                status = data_ship.get_text()
                            case 10:
                                agency = data_ship.get_text()
                            case 11:
                                operator = data_ship.get_text()
                            case 12:
                                arrival = data_ship.get_text()
                            case 13:
                                ets = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    new_paranagua_suport_ship = ParanaguaSupportShip(programation, duv, cradle, ship, imo, loa, dwt, operation_type,
                                                                        status, agency, operator, arrival, ets)
                    # print(new_paranagua_suport_ship)
            
            
            elif table_header.find('th', text="DESPACHADOS") is not None:
                #print(f"Scraping data from table 'DESPACHADOS'...")
                for ship in table_body.find_all('tr'):
                    count_td = 0
                    for data_ship in ship.find_all('td'):
                        match count_td:
                            case 1:
                                programation = data_ship.get_text()
                            case 2:
                                duv = data_ship.get_text()
                            case 3:
                                cradle = data_ship.get_text()
                            case 4:
                                ship = data_ship.get_text()
                            case 5:
                                imo = data_ship.get_text()
                            case 6:
                                loa = data_ship.get_text()
                            case 7:
                                dwt = data_ship.get_text()
                            case 8:
                                board = data_ship.get_text()
                            case 9:
                                direction = data_ship.get_text()
                            case 10:
                                agency = data_ship.get_text()
                            case 11:
                                operator = data_ship.get_text()
                            case 12:
                                goods = data_ship.get_text()
                            case 13:
                                arrival = data_ship.get_text()
                            case 14:
                                ets = data_ship.get_text()
                            case 15:
                                undocking = data_ship.get_text()
                            case 16:
                                # Substituir "," por "." para converter para float
                                string_without_commas = data_ship.get_text().replace(",", ".")
                                # Remover pontos
                                final_string = string_without_commas.replace(".", "")
                                expected = float(final_string.split()[0])
                            case default:
                                pass
                        
                        count_td += 1
                    
                    new_paranagua_dispatched_ship = ParanaguaDispatchedShip(programation, duv, cradle, ship, imo, loa, dwt, board,
                                                                            direction, agency, operator, goods, arrival, ets,
                                                                            undocking, expected)
                    self.ships_list.add_ship(new_paranagua_dispatched_ship)
                    
                    #print(new_paranagua_dispatched_ship)
