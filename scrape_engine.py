import imp, json

class Scrape_Engine:

    def __init__(self):

        self.mods = {}

    def add_mod(self, mod, name, frequency):

        if frequency not in self.mods:

            self.mods[frequency] = {}
            self.mods[frequency][name] = mod

        else:

            self.mods[frequency][name] = mod

    def scrape_page(self, module, cur, url):

        rows = module.get_unformatted_rows(url)

        for row in rows:
            row_values = module.format_row(row)
            module.save_row_values(row_values, cur)

    def load_mods(self):

        mod_list = json.load(open('mods/engine_mods.json', 'r'))['Mods']

        for frequency in mod_list: 

            frequency = str(frequency)

            for mod_name in mod_list[frequency]: 
                
                mod_name = str(mod_name)
                mod_class = str(mod_list[frequency][mod_name].title())
                mod_file = str('mods/%s.py' % mod_list[frequency][mod_name])
                mod = imp.load_source(mod_class, mod_file)

                if frequency not in self.mods:

                    self.mods[frequency] = {}
                    self.mods[frequency][mod_name] = mod

                else: 
                    
                    self.mods[frequency][mod_name] = mod
