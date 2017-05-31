from bs4 import BeautifulSoup
import urllib2, psycopg2

class Scrape_Module:

    def __init__(self, con_string, mod):

        self.con_string = con_string
        self.mod = mod

    def generate_url(self, variable):

        return self.mod.generate_url(variable)

    def create_table(self): 

        conn = psycopg2.connect(self.con_string)
        cur = conn.cursor()

        table_name = self.mod.get_table_name()
        column_names = self.mod.get_column_names()

        insert_string = "CREATE TABLE %s (" % (table_name)
        value_string = ""

        for column in column_names[:len(column_names)-1]:

            value_string += "%s %s," % (column['name'], column['type'])

        value_string += "%s %s);" % (column_names[len(column_names)-1]['name'], \
                                     column_names[len(column_names)-1]['type'])

        cur.execute(insert_string + value_string)
        conn.commit()


    def get_unformatted_rows(self, url):

        request = urllib2.urlopen(url)
        soup = BeautifulSoup(request.read(), 'lxml')
        request.close()

        return self.mod.get_unformatted_rows(soup)


    def format_row(self, row):

        return self.mod.format_row(row)


    def save_row_values(self, row_values, cur):

        table_name = self.mod.get_table_name()

        insert_string = "INSERT INTO %s VALUES (" % (table_name)
        value_string = ""

        for value in row_values[:len(row_values)-1]: 
            value_string += "$$%s$$," % (value)

        value_string += "$$%s$$);" % row_values[len(row_values)-1]

        cur.execute(insert_string + value_string)
