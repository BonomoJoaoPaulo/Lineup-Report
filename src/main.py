from ParanaguaDataScraper import ParanaguaDataScraper as pds
from SantosDataScraper import SantosDataScrapper as sds

paranagua_data_scraper = pds("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")
paranagua_data_scraper.scrap_data()

santos_data_scraper = sds("https://www.portodesantos.com.br/informacoes-operacionais/operacoes-portuarias/navegacao-e-movimento-de-navios/navios-esperados-carga/")
santos_data_scraper.scrap_data()