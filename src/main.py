from ParanaguaDataScraper import ParanaguaDataScraper as pds

paranagua_data_scraper = pds("https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo")

paranagua_data_scraper.scrap_data()
