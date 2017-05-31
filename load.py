from scrape_module import Scrape_Module
from scrape_engine import Scrape_Engine

con_string = "dbname='stockroom' user='stockplug' host='localhost' password='stockplugpass'"

engine = Scrape_Engine()

engine.load_mods()
print engine.mods
