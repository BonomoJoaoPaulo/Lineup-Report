import json
import datetime
import pandas as pd

from ParanaguaDataScraper import ParanaguaDataScraper as pds
from SantosDataScraper import SantosDataScrapper as sds
from SantosShips.SantosMultiOperationShip import SantosMultiOperationShip
from SantosShips.SantosShipsList import SantosShipsList

#paranagua_data_scraper = pds("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")
#paranagua_data_scraper.scrap_data()

santos_ships_list = SantosShipsList()
santos_data_scraper = sds(santos_ships_list, "https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/")
santos_data_scraper.scrap_data()


def export_all_data_as_csv():
    santos_csv_file = open("santos_all_ships.csv", "w")
    santos_csv_file.write(santos_data_scraper.ships_list.export_as_csv())
    santos_csv_file.close()


def export_all_data_as_json():
    santos_json_file = open("santos_all_ships.json", "w")
    santos_json_file.write(santos_data_scraper.ships_list.export_as_json())
    santos_json_file.close()


def filter_by_goods(goods):
    filtered_ships = []
    for ship in santos_data_scraper.ships_list.ships:
        if type(ship) == SantosMultiOperationShip:
            if ship.first_goods == goods or ship.second_goods == goods:
                filtered_ships.append(ship)
        else:
            if ship.goods == goods:
                filtered_ships.append(ship)

    return filtered_ships


def filter_by_operation(operation):
    filtered_ships = []
    for ship in santos_data_scraper.ships_list.ships:
        if type(ship) == SantosMultiOperationShip:
            if ship.first_operation == operation or ship.second_operation == operation:
                filtered_ships.append(ship)
        else:
            if ship.operation == operation:
                filtered_ships.append(ship)

    return filtered_ships


def export_filtered_data_as_xlsx():
    goods_import_list = []
    goods_export_list = []
    goods_ship_import_counter_list = []
    goods_ship_export_counter_list = []
    goods_ship_import_volume_list = []
    goods_ship_export_volume_list = []
    goods_ship_import_port_list = []
    goods_ship_export_port_list = []

    for ship in santos_data_scraper.ships_list.ships:
        if type(ship) == SantosMultiOperationShip:
            if ship.first_operation == "DESC":
                if ship.first_goods not in goods_import_list:
                    goods_import_list.append(ship.first_goods)
                    goods_ship_import_counter_list.append(1)
                    goods_ship_import_volume_list.append(float(ship.first_weight))
                    goods_ship_import_port_list.append("Santos")
                else:
                    goods_ship_import_counter_list[goods_import_list.index(ship.first_goods)] += 1
                    goods_ship_import_volume_list[goods_import_list.index(ship.first_goods)] += float(ship.first_weight)
            else:
                if ship.first_goods not in goods_export_list:
                    goods_export_list.append(ship.first_goods)
                    goods_ship_export_counter_list.append(1)
                    goods_ship_export_volume_list.append(float(ship.first_weight))
                    goods_ship_export_port_list.append("Santos")
                else:
                    goods_ship_export_counter_list[goods_export_list.index(ship.first_goods)] += 1
                    goods_ship_export_volume_list[goods_export_list.index(ship.first_goods)] += float(ship.first_weight)

            if ship.second_operation == "DESC":
                if ship.second_goods not in goods_import_list:
                    goods_import_list.append(ship.second_goods)
                    goods_ship_import_counter_list.append(1)
                    goods_ship_import_volume_list.append(float(ship.second_weight))
                    goods_ship_import_port_list.append("Santos")
                else:
                    goods_ship_import_counter_list[goods_import_list.index(ship.second_goods)] += 1
                    goods_ship_import_volume_list[goods_import_list.index(ship.second_goods)] += float(ship.second_weight)
            else:
                if ship.second_goods not in goods_export_list:
                    goods_export_list.append(ship.second_goods)
                    goods_ship_export_counter_list.append(1)
                    goods_ship_export_volume_list.append(float(ship.second_weight))
                    goods_ship_export_port_list.append("Santos")
                else:
                    goods_ship_export_counter_list[goods_export_list.index(ship.second_goods)] += 1
                    goods_ship_export_volume_list[goods_export_list.index(ship.second_goods)] += float(ship.second_weight)
        else:
            if ship.operation == "DESC   ":
                if ship.goods not in goods_import_list:
                    goods_import_list.append(ship.goods)
                    goods_ship_import_counter_list.append(1)
                    goods_ship_import_volume_list.append(float(ship.weight))
                    goods_ship_import_port_list.append("Santos")
                else:
                    goods_ship_import_counter_list[goods_import_list.index(ship.goods)] += 1
                    goods_ship_import_volume_list[goods_import_list.index(ship.goods)] += float(ship.weight)
            else:
                if ship.goods not in goods_export_list:
                    goods_export_list.append(ship.goods)
                    goods_ship_export_counter_list.append(1)
                    goods_ship_export_volume_list.append(float(ship.weight))
                    goods_ship_export_port_list.append("Santos")
                else:
                    goods_ship_export_counter_list[goods_export_list.index(ship.goods)] += 1
                    goods_ship_export_volume_list[goods_export_list.index(ship.goods)] += float(ship.weight)
    
    #print("GOODS_IMPORT_lIST: ", goods_import_list)
    #print("GOODS_IMPORT_lIST: ", len(goods_import_list))
    #print("GOODS_EXPORT_lIST: ", goods_export_list)
    #print("GOODS_EXPORT_lIST: ", len(goods_export_list))
    #print("GOODS_IMPORT_COUNTER_lIST: ", goods_ship_import_counter_list)
    #print("GOODS_IMPORT_COUNTER_lIST: ", len(goods_ship_import_counter_list))
    #print("GOODS_EXPORT_COUNTER_lIST: ", goods_ship_export_counter_list)
    #print("GOODS_EXPORT_COUNTER_lIST: ", len(goods_ship_export_counter_list))
    #print("GOODS_IMPORT_PORT_lIST: " ,goods_ship_import_port_list)
    #print("GOODS_IMPORT_PORT_lIST: ", len(goods_ship_import_port_list))
    #print("GOODS_EXPORT_PORT_lIST: ",goods_ship_export_port_list)
    #print("GOODS_EXPORT_PORT_lIST: ",len(goods_ship_export_port_list))
    #print("GOODS_IMPORT_VOLUME_lIST: ",goods_ship_import_volume_list)
    #print("GOODS_IMPORT_VOLUME_lIST: ",len(goods_ship_import_volume_list))
    #print("GOODS_EXPORT_VOLUME_lIST: ",goods_ship_export_volume_list)
    #print("GOODS_EXPORT_VOLUME_lIST: ",len(goods_ship_export_volume_list))

    import_data = {
        "Goods": goods_import_list,
        "Ships Number": goods_ship_import_counter_list,
        "Goods Import Volume": goods_ship_import_volume_list,
        "Port": goods_ship_import_port_list,
    }
    export_data = {
        "Goods": goods_export_list,
        "Ships Number": goods_ship_export_counter_list,
        "Goods Export Volume": goods_ship_export_volume_list,
        "Port": goods_ship_export_port_list,
    }
    export_df = pd.DataFrame(export_data)
    import_df = pd.DataFrame(import_data)

    # Escrever os DataFrames em um único arquivo Excel com duas abas
    output_file = f"santos_ships_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        import_df.to_excel(writer, sheet_name='Import', index=False)
        export_df.to_excel(writer, sheet_name='Export', index=False)

    print(f"Arquivo Excel '{output_file}' criado com sucesso.")



def ask_user_want_to_close():
    user_want_to_close = input("Deseja encerrar o sistema? (S/N): ")
    if user_want_to_close.lower() == "s":
        print("\nEncerrando o sistema...")
        return True
    else:
        print("\nRetornando ao menu principal...")
        return False


menu_string = """
-----------------------------------------------
LINEUP DE NAVIOS - PORTOS DE SANTOS E PARANAGUÁ\n
1 - Exportar dados completos como CSV
2 - Exportar dados completos como JSON
3 - Exportar dados completos como CSV e JSON
4 - Filtrar navios por carga
5 - Filtrar navios por operação (importação/exportação)
6 - Exportar dados por carga/operacao/porto como XLSX
7 - Sair
-----------------------------------------------
"""

while True:
    print("Iniciando o sistema...\n")
    print(menu_string)
    option = input("Digite a opção desejada: ")
    if not(int(option)) or int(option) < 1 or int(option) > 7:
        print("Opção inválida!\n"
              "Retornando ao menu principal...")
        continue
    else:
        match int(option):
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

            case 4:
                goods_selection = input("Digite a carga desejada: ")
                filtered_ships = filter_by_goods(goods_selection)
                print(f"Total de navios de {goods_selection}: {len(filtered_ships)}")

            case 5:
                operation_selection = input("Digite a operação desejada (IMP/EXP): ")
                if operation_selection.lower() != "imp" and operation_selection.lower() != "exp":
                    print("Opção inválida!\n")
                    continue
                else:   
                    filtered_ships = filter_by_operation(operation_selection)
                    print(f"Total de navios de {operation_selection}: {len(filtered_ships)}")
            
            case 6:
                print("Exportando dados por carga/operacao/porto como XLSX...")
                export_filtered_data_as_xlsx()

            case 7:
                print("Encerrando o sistema...")
                break

            case default:
                pass

        if ask_user_want_to_close():
            break
