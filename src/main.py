import json
import datetime
import pandas as pd

from scrapers.paranagua_data_scraper import ParanaguaDataScraper as pds
from scrapers.santos_data_scraper import SantosDataScrapper as sds
from scrapers.santarem_data_scraper import SantaremDataScraper as sads
from SantosShips.SantosMultiOperationShip import SantosMultiOperationShip
from SantosShips.SantosShipsList import SantosShipsList

paranagua_data_scraper = pds("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")
paranagua_data_scraper.scrap_data()

santos_data_scraper = sds("https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/")
santos_data_scraper.scrap_data()

santarem_data_scraper = sads("https://cdpport.cdp.com.br/cdpport/pesquisa.aspx?WCI=relLineUp_008&Mv=Link&sqlCodDominio=6")
santarem_data_scraper.scrap_data()

def export_all_data_as_csv():
    paranagua_data_scraper.ships_to_csv()
    santarem_data_scraper.ships_to_csv()
    santos_data_scraper.ships_to_csv()

def export_all_data_as_json():
    paranagua_data_scraper.ships_to_json()
    santarem_data_scraper.ships_to_json()
    santos_data_scraper.ships_to_json()

def ask_user_want_to_close():
    user_want_to_close = input("Deseja encerrar o sistema? (S/N): ")
    if user_want_to_close.lower() == "s":
        print("\nEncerrando o sistema...")
        return True
    else:
        print("\nRetornando ao menu principal...")
        return False


if __name__ == "__main__":
    menu_string = """
    -----------------------------------------------
    LINEUP DE NAVIOS - PORTOS DE PARANAGUÁ, SANTAREM E SANTOS\n
    1 - Exportar dados completos como CSV
    2 - Exportar dados completos como JSON
    3 - Exportar dados completos como CSV e JSON
    5 - Sair
    -----------------------------------------------
    """

    while True:
        print("Iniciando o sistema...")
        print(menu_string)
        option = input("Digite a opção desejada: ")

        try:
            option = int(option)
        except:
            print("Opção inválida!\n"
                "Retornando ao menu principal...")
            continue

        match option:
            case 1:
                print("Exportando dados completos como CSV...")
                export_all_data_as_csv()

            case 2:
                print("Exportando dados completos como JSON...")
                export_all_data_as_json()

            case 3:
                print("Exportando dados completos como CSV e JSON...")
                export_all_data_as_csv()
                export_all_data_as_json()

            case 5:
                print("Encerrando o sistema...")
                break

            case default:
                pass

        if ask_user_want_to_close():
            break
