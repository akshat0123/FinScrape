from scrape_module import Scrape_Module
import psycopg2, json, imp

class Scrape_Engine:

    def __init__(self, con_string):

        self.con_string = con_string
        self.mods = {}

    def load_mods(self):

        mod_list = json.load(open('mods/engine_mods.json', 'r'))['Mods']

        for frequency in mod_list: 

            frequency = str(frequency)

            for mod_name in mod_list[frequency]: 
                
                mod_name = str(mod_name)
                mod_class = str(mod_list[frequency][mod_name].title())
                mod_file = str('mods/%s.py' % mod_list[frequency][mod_name])
                mod = imp.load_source(mod_class, mod_file)
                mod = Scrape_Module(self.con_string, getattr(mod, mod_class)())

                if frequency not in self.mods:

                    self.mods[frequency] = {}
                    self.mods[frequency][mod_name] = mod

                else: 
                    
                    self.mods[frequency][mod_name] = mod

    def add_mod(self, mod, name, frequency):

        if frequency not in self.mods:

            self.mods[frequency] = {}
            self.mods[frequency][name] = mod

        else:

            self.mods[frequency][name] = mod

    def create_tables(self):

        for frequency in self.mods:
            for mod in self.mods[frequency]:
                self.mods[frequency][mod].create_table()

    def scrape_page(self, module, cur, url):

        rows = module.get_unformatted_rows(url)

        for row in rows:
            row_values = module.format_row(row)
            module.save_row_values(row_values, cur)

    def scrape_run(self, frequency, url_vars=['']):

        conn = psycopg2.connect(self.con_string)
        cur = conn.cursor()

        for mod_name in self.mods[frequency]:

            mod = self.mods[frequency][mod_name]

            for url_var in url_vars: 
                
                url = mod.generate_url(url_var)
                self.scrape_page(mod, cur, url)

        conn.commit()
        cur.close()
