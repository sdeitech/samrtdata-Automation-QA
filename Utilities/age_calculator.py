import datetime


class Calculate_Year:

    def get_date_before_num_years(self, years, days):
        old_date = datetime.datetime.now() - datetime.timedelta(days=int(int(years) * 365.25)+1+days)
        return old_date.strftime("%d/%m/%Y")
