class Wiki_Mod:

    def __init__(self):

        self.base_url = [
                "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        ]

        self.table_name = "basic_data"
        self.column_names = [
            {'name': 'ticker', 'type': 'varchar(10)'},
            {'name': 'company', 'type': 'varchar(100)'},
            {'name': 'sector', 'type': 'varchar(100)'},
            {'name': 'sub_sector', 'type': 'varchar(100)'}
        ]

    def get_table_name(self): return self.table_name
    def get_column_names(self): return self.column_names

    def generate_url(self, variable):

        return self.base_url[0]

    def get_unformatted_rows(self, soup):

        data = soup.findAll("table")
        stock_table = data[0]
        return stock_table.findAll("tr")[1:]

    def format_row(self, row):

        row = row.findAll("td")

        return [
            row[0].find("a").get_text(),
            row[1].find("a").get_text(),
            row[3].get_text(),
            row[4].get_text()
        ]
