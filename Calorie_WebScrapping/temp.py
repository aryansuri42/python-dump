from email.mime import base
import requests
from selectorlib import Extractor

base_url = 'https://www.timeanddate.com/worldclock/'

class Temperature:

    def __init__(self,city, country):
        self.city = city.replace(" ", "-")
        self.country = country.replace(" ", "-")

    def _url_create(self):
        url = base_url+self.country+'/'+self.city
        return url
        
    def _scrape(self):
        url = self._url_create()
        r = requests.get(url)
        c = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        result = extractor.extract(c)
        return result
    
    def get(self):
        clean_content = self._scrape()
        return float(clean_content['temp'].replace("°C","").strip())
    
if __name__ == "__main__":
    temperature = Temperature(city = "tokyo", country = 'japan')
    print(temperature.get())
        
        