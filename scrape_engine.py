from scrape_module import Scrape_Module
import psycopg2, random, math, json, time, file, imp, sys

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

        file = open("errors.log", "w")

        conn = psycopg2.connect(self.con_string)
        cur = conn.cursor()

        for mod_name in self.mods[frequency]:

            mod = self.mods[frequency][mod_name]
            progress = 0

            for url_var in url_vars: 
                
                url = mod.generate_url(url_var)

                try: 

                    self.scrape_page(mod, cur, url)

                except:

                    error = "There was an error retrieving the %s url from the %s module" %\
                            (url_var, mod_name)

                    file.write(error)

                progress_bar = '#' * int(math.floor((float(progress)/len(url_vars))*10))
                remaining = ' ' * (10 - int(math.floor((float(progress)/len(url_vars))*10)))
                progress_bar = progress_bar + remaining
                sys.stdout.write('\r%s: [%s] %d/%d' % (mod_name, progress_bar, progress, len(url_vars)))
                sys.stdout.flush()
                progress = progress + 1

                time.sleep(random.randrange(5, 11))

            sys.stdout.write('\r%s: [%s]' % (mod_name, '##########'))
            print 

        conn.commit()
        cur.close()
