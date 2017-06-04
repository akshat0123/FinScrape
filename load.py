from scrape_module import Scrape_Module
from scrape_engine import Scrape_Engine
import psycopg2

con_string = "dbname='stockroom' user='stockplug' host='localhost' password='stockplugpass'"

engine = Scrape_Engine(con_string)

engine.load_mods()

# engine.create_tables()
# engine.scrape_run('initial')

conn = psycopg2.connect(con_string)
cur = conn.cursor()
cur.execute("SELECT ticker FROM  basic_data;")
tickers = [x[0] for x in cur.fetchall()]
cur.close()
engine.scrape_run('daily', tickers)
