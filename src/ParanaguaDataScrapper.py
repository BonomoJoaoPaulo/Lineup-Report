from PortDataScrapper import PortDataScrapper

class ParanaguaDataScrapper(PortDataScrapper):
    def __init__(self, url):
        super().__init__(url)
        self.data = self.scrap_data()

    def scrap_data(self):
        pass