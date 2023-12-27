from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

from PortDataScraper import PortDataScraper
from ParanaguaMooredShip import ParanaguaMooredShip

class ParanaguaDataScraper(PortDataScraper):
    def __init__(self, url):
        super().__init__(url)
        #self.data = self.scrap_data()

    def scrap_data(self):
        print("Scraping data from Paranaguá...")
        website = "https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo"
        response = requests.get(website)
        content = response.text

        soup = BeautifulSoup(content, 'lxml')

        tables = soup.find_all('table', class_="table table-bordered table-striped table-hover")
        count_tables = 0

        for table in tables:
            table_header = table.find('thead')
            table_body = table.find('tbody')

            if table_header.find('th', text="ATRACADOS") is not None:
                print(f"Scraping data from table 'ATRACADOS'...")
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
                                predict = data_ship.get_text()
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
                                                                    tons_per_day, predict, realized, operator_balance, total_balance)

                    print(new_paranagua_moored_ship)

            elif table_header.find('th', text="PROGRAMADOS") is not None:
                print(f"Scraping data from table 'PROGRAMADOS'...")
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
                                expected = data_ship.get_text()
                            case default:
                                pass

                        count_td += 1
                    
                    print(f"Id: {id}\n" \
                        f"Programation: {programation}\n" \
                        f"DUV: {duv}\n" \
                        f"Cradle: {cradle}\n" \
                        f"Ship: {ship}\n" \
                        f"IMO: {imo}\n" \
                        f"LOA: {loa}\n" \
                        f"DWT: {dwt}\n" \
                        f"Board: {board}\n" \
                        f"Direction: {direction}\n" \
                        f"Agency: {agency}\n" \
                        f"Operator: {operator}\n" \
                        f"Goods: {goods}\n" \
                        f"Arrival: {arrival}\n" \
                        f"ETB: {etb}\n" \
                        f"ETS: {ets}\n" \
                        f"Expected: {expected}\n" \
                        f"--------------------------\n")
                    
            elif table_header.find('th', text="AO LARGO PARA REATRACAÇÃO") is not None:
                print(f"Scraping data from table 'AO LARGO PARA REATRACAÇÃO'...")
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
                                expected = data_ship.get_text()
                            case 18:
                                realized = data_ship.get_text()
                            case 19:
                                balance = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    print(f"Programation: {programation}\n" \
                        f"DUV: {duv}\n" \
                        f"Cradle: {cradle}\n" \
                        f"Ship: {ship}\n" \
                        f"IMO: {imo}\n" \
                        f"LOA: {loa}\n" \
                        f"DWT: {dwt}\n" \
                        f"Board: {board}\n" \
                        f"Direction: {direction}\n" \
                        f"Agency: {agency}\n" \
                        f"Operator: {operator}\n" \
                        f"Goods: {goods}\n" \
                        f"Mooring: {mooring}\n" \
                        f"Arrival: {arrival}\n" \
                        f"ETS: {ets}\n" \
                        f"Undocking: {undocking}\n" \
                        f"Expected: {expected}\n" \
                        f"Realized: {realized}\n" \
                        f"Balance: {balance}\n" \
                        f"--------------------------\n")
                            
            
            elif table_header.find('th', text="AO LARGO") is not None:
                print(f"Scraping data from table 'AO LARGO'...")
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
                                expected = data_ship.get_text()
                            case 16:
                                cal_arrival = data_ship.get_text()
                            case 17:
                                cal_departure = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    print(f"Programation: {programation}\n" \
                        f"DUV: {duv}\n" \
                        f"Cradle: {cradle}\n" \
                        f"Ship: {ship}\n" \
                        f"IMO: {imo}\n" \
                        f"LOA: {loa}\n" \
                        f"DWT: {dwt}\n" \
                        f"Direction: {direction}\n" \
                        f"Agency: {agency}\n" \
                        f"Operator: {operator}\n" \
                        f"Goods: {goods}\n" \
                        f"ETA: {eta}\n" \
                        f"ETS: {ets}\n" \
                        f"Arrival: {arrival}\n" \
                        f"Expected: {expected}\n" \
                        f"Calculated arrival: {cal_arrival}\n" \
                        f"Calculated departure: {cal_departure}\n" \
                        f"--------------------------\n")
            
            elif table_header.find('th', text="ESPERADOS") is not None:
                print(f"Scraping data from table 'ESPERADOS'...")
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
                                expected = data_ship.get_text()
                            case 15:
                                cal_arrival = data_ship.get_text()
                            case 16:
                                cal_departure = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    print(f"Programation: {programation}\n" \
                        f"DUV: {duv}\n" \
                        f"Cradle: {cradle}\n" \
                        f"Ship: {ship}\n" \
                        f"IMO: {imo}\n" \
                        f"LOA: {loa}\n" \
                        f"DWT: {dwt}\n" \
                        f"Direction: {direction}\n" \
                        f"Agency: {agency}\n" \
                        f"Operator: {operator}\n" \
                        f"Goods: {goods}\n" \
                        f"ETA: {eta}\n" \
                        f"ETS: {ets}\n" \
                        f"Expected: {expected}\n" \
                        f"Calculated arrival: {cal_arrival}\n" \
                        f"Calculated departure: {cal_departure}\n" \
                        f"--------------------------\n")

            elif table_header.find('th', text="APOIO PORTUÁRIO / OUTROS") is not None:
                print(f"Scraping data from table 'APOIO PORTUÁRIO / OUTROS'...")
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
                    
                    print(f"Programation: {programation}\n" \
                        f"DUV: {duv}\n" \
                        f"Cradle: {cradle}\n" \
                        f"Ship: {ship}\n" \
                        f"IMO: {imo}\n" \
                        f"LOA: {loa}\n" \
                        f"DWT: {dwt}\n" \
                        f"Operation type: {operation_type}\n" \
                        f"Status: {status}\n" \
                        f"Agency: {agency}\n" \
                        f"Operator: {operator}\n" \
                        f"Arrival: {arrival}\n" \
                        f"ETS: {ets}\n" \
                        f"--------------------------\n")
            
            
            elif table_header.find('th', text="DESPACHADOS") is not None:
                print(f"Scraping data from table 'DESPACHADOS'...")
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
                                predict = data_ship.get_text()
                            case default:
                                pass
                        
                        count_td += 1
                    
                    print(f"Programation: {programation}\n" \
                        f"DUV: {duv}\n" \
                        f"Cradle: {cradle}\n" \
                        f"Ship: {ship}\n" \
                        f"IMO: {imo}\n" \
                        f"LOA: {loa}\n" \
                        f"DWT: {dwt}\n" \
                        f"Board: {board}\n" \
                        f"Direction: {direction}\n" \
                        f"Agency: {agency}\n" \
                        f"Operator: {operator}\n" \
                        f"Goods: {goods}\n" \
                        f"Arrival: {arrival}\n" \
                        f"ETS: {ets}\n" \
                        f"Undocking: {undocking}\n" \
                        f"Predict: {predict}\n" \
                        f"--------------------------\n")
