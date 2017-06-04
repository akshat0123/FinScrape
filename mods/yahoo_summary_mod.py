import datetime

class Yahoo_Summary_Mod:

    def __init__(self):

        self.base_url = [
                "https://finance.yahoo.com/quote/",
                "/?p="
        ]

        self.table_name = "yahoo_summary_daily"

        self.column_names = [
            {'name': 'ticker', 'type': 'varchar(40)'},
            {'name': 'date', 'type': 'varchar(40)'},
            {'name': 'previous_close', 'type': 'varchar(40)'},
            {'name': 'open', 'type': 'varchar(40)'},
            {'name': 'bid', 'type': 'varchar(40)'},
            {'name': 'ask', 'type': 'varchar(40)'},
            {'name': 'days_range', 'type': 'varchar(40)'},
            {'name': 'fifty_two_week_range', 'type': 'varchar(40)'},
            {'name': 'volume', 'type': 'varchar(40)'},
            {'name': 'average_volume', 'type': 'varchar(40)'},
            {'name': 'market_cap', 'type': 'varchar(40)'},
            {'name': 'beta', 'type': 'varchar(40)'},
            {'name': 'pe_ratio', 'type': 'varchar(40)'},
            {'name': 'eps', 'type': 'varchar(40)'},
            {'name': 'earnings_date', 'type': 'varchar(40)'},
            {'name': 'dividend_and_yield', 'type': 'varchar(40)'},
            {'name': 'ex_dividend_date', 'type': 'varchar(40)'},
            {'name': 'one_year_target', 'type': 'varchar(40)'}
        ]

        self.ticker = ''

    def get_table_name(self): return self.table_name
    def get_column_names(self): return self.column_names

    def generate_url(self, variable):

        self.ticker = variable

        url = self.base_url[0] + variable + self.base_url[1] + variable
        return url

    def get_unformatted_rows(self, soup):

        return [soup]

    def format_row(self, row):

        return [
            str(self.ticker),
            str(datetime.datetime.now().date()),
            row.find("td", {"data-test": "PREV_CLOSE-value"}).find("span").get_text(),
            row.find("td", {"data-test": "OPEN-value"}).find("span").get_text(),
            row.find("td", {"data-test": "BID-value"}).get_text().strip(' '),
            row.find("td", {"data-test": "ASK-value"}).get_text().strip(' '),
            row.find("td", {"data-test": "DAYS_RANGE-value"}).get_text().strip(' '),
            row.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).get_text().strip(' '),
            row.find("td", {"data-test": "TD_VOLUME-value"}).find("span").get_text(),
            row.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).find("span").get_text(),
            row.find("td", {"data-test": "MARKET_CAP-value"}).find("span").get_text(),
            row.find("td", {"data-test": "BETA-value"}).find("span").get_text(),
            row.find("td", {"data-test": "PE_RATIO-value"}).find("span").get_text(),
            row.find("td", {"data-test": "EPS_RATIO-value"}).find("span").get_text(),
            row.find("td", {"data-test": "EARNINGS_DATE-value"}).get_text(),
            row.find("td", {"data-test": "DIVIDEND_AND_YIELD-value"}).get_text(),
            row.find("td", {"data-test": "EXDIVIDEND_DATE-value"}).find("span").get_text(),
            row.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).find("span").get_text()
        ]

    def get_data(self, cur):
        pass
