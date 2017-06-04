import datetime

class Yahoo_Statistics_Mod:

    def __init__(self):

        self.base_url = [
            "https://finance.yahoo.com/quote/",
            "/key-statistics?p="
        ]

        self.table_name = "yahoo_statistics_daily"
        
        self.column_names = [
            {'name': 'ticker', 'type': 'varchar(40)'},
            {'name': 'date', 'type': 'varchar(40)'},
            {'name': 'market_cap', 'type': 'varchar(40)'},
            {'name': 'enterprise_value', 'type': 'varchar(40)'},
            {'name': 'trailing_pe', 'type': 'varchar(40)'},
            {'name': 'forward_pe', 'type': 'varchar(40)'},
            {'name': 'peg_ratio', 'type': 'varchar(40)'},
            {'name': 'price_sales', 'type': 'varchar(40)'},
            {'name': 'price_book', 'type': 'varchar(40)'},
            {'name': 'enterprise_value_revenue', 'type': 'varchar(40)'},
            {'name': 'enterprise_value_ebitda', 'type': 'varchar(40)'},
            {'name': 'fiscal_year_ends', 'type': 'varchar(40)'},
            {'name': 'most_recent_quarter', 'type': 'varchar(40)'},
            {'name': 'profit_margin', 'type': 'varchar(40)'},
            {'name': 'operating_margin', 'type': 'varchar(40)'},
            {'name': 'return_on_assets', 'type': 'varchar(40)'},
            {'name': 'return_on_equity', 'type': 'varchar(40)'},
            {'name': 'revenue', 'type': 'varchar(40)'},
            {'name': 'revenue_per_share', 'type': 'varchar(40)'},
            {'name': 'quarterly_growth_revenue', 'type': 'varchar(40)'},
            {'name': 'gross_profit', 'type': 'varchar(40)'},
            {'name': 'ebitda', 'type': 'varchar(40)'},
            {'name': 'net_income_avi_to_common', 'type': 'varchar(40)'},
            {'name': 'diluted_eps', 'type': 'varchar(40)'},
            {'name': 'quarterly_earnings_growth', 'type': 'varchar(40)'},
            {'name': 'total_cash', 'type': 'varchar(40)'},
            {'name': 'total_cash_per_share', 'type': 'varchar(40)'},
            {'name': 'total_debt', 'type': 'varchar(40)'},
            {'name': 'total_debt_equity', 'type': 'varchar(40)'},
            {'name': 'current_ratio', 'type': 'varchar(40)'},
            {'name': 'book_value_per_share', 'type': 'varchar(40)'},
            {'name': 'operating_cash_flow', 'type': 'varchar(40)'},
            {'name': 'levered_free_cash_flow', 'type': 'varchar(40)'},
            {'name': 'beta', 'type': 'varchar(40)'},
            {'name': 'fifty_two_week_change', 'type': 'varchar(40)'},
            {'name': 'sp_five_hundred_fifty_two_week_change', 'type': 'varchar(40)'},
            {'name': 'fifty_two_week_high', 'type': 'varchar(40)'},
            {'name': 'fifty_two_week_low', 'type': 'varchar(40)'},
            {'name': 'fifty_day_moving_average', 'type': 'varchar(40)'},
            {'name': 'two_hundred_day_moving_average', 'type': 'varchar(40)'},
            {'name': 'avg_vol_three_month', 'type': 'varchar(40)'},
            {'name': 'avg_vol_ten_day', 'type': 'varchar(40)'},
            {'name': 'shares_outstanding', 'type': 'varchar(40)'},
            {'name': 'float', 'type': 'varchar(40)'},
            {'name': 'held_by_insiders', 'type': 'varchar(40)'},
            {'name': 'held_by_institutions', 'type': 'varchar(40)'},
            {'name': 'shares_short', 'type': 'varchar(40)'},
            {'name': 'short_ratio', 'type': 'varchar(40)'},
            {'name': 'short_of_float', 'type': 'varchar(40)'},
            {'name': 'shares_short_prior_month', 'type': 'varchar(40)'},
            {'name': 'forward_annual_dividend_rate', 'type': 'varchar(40)'},
            {'name': 'forward_annual_dividend_yield', 'type': 'varchar(40)'},
            {'name': 'trailing_annual_dividend_rate', 'type': 'varchar(40)'},
            {'name': 'trailing_annual_dividend_yield', 'type': 'varchar(40)'},
            {'name': 'five_year_average_dividend_yield', 'type': 'varchar(40)'},
            {'name': 'payout_ratio', 'type': 'varchar(40)'},
            {'name': 'dividend_rate', 'type': 'varchar(40)'},
            {'name': 'ex_dividend_rate', 'type': 'varchar(40)'},
            {'name': 'last_split_factor', 'type': 'varchar(40)'},
            {'name': 'last_split_date', 'type': 'varchar(40)'}
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
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[2].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[3].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[4].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[5].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[6].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[7].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[0].findAll("tr")[8].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[1].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[1].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[2].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[2].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[3].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[3].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[2].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[3].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[4].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[5].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[6].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[4].findAll("tr")[7].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[5].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[5].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[5].findAll("tr")[2].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[5].findAll("tr")[3].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[5].findAll("tr")[4].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[5].findAll("tr")[5].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[6].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[6].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[2].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[3].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[4].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[5].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[7].findAll("tr")[6].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[2].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[3].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[4].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[5].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[6].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[7].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[8].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[8].findAll("tr")[9].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[0].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[1].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[2].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[3].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[4].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[5].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[6].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[7].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[8].findAll("td")[1].get_text().strip(),
            row.findAll("table", {"class": "table-qsp-stats"})[9].findAll("tr")[9].findAll("td")[1].get_text().strip()
        ]

    def get_data(self, cur): 
        pass
