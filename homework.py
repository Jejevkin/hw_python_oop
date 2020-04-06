import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.current_date = dt.datetime.now().date()
        self.week_ago = self.current_date - dt.timedelta(days=7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        total_amount = 0
        for record in self.records:
            if record.date == self.current_date:
                total_amount += record.amount
        return total_amount

    def get_week_stats(self):
        week_total_amount = 0
        for record in self.records:
            if self.week_ago <= record.date <= self.current_date:
                week_total_amount += record.amount
        return week_total_amount


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if self.limit > super().get_today_stats():
            response = "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более "
            response += str(self.limit - super().get_today_stats()) + " кКал"
            return response
        else:
            return "Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00

    def get_today_cash_remained(self, currency):
        currencies = {'rub': [1, 'руб'],
                      'usd': [self.USD_RATE, 'USD'],
                      'eur': [self.EURO_RATE, 'Euro'],
                      }
        balance = round((self.limit - super().get_today_stats()) / currencies[currency][0], 2)
        debt = round((super().get_today_stats() - self.limit) / currencies[currency][0], 2)
        if self.limit > super().get_today_stats():
            response = f"На сегодня осталось {balance} {currencies[currency][1]}"
            return response
        elif self.limit < super().get_today_stats():
            response = f"Денег нет, держись: твой долг - {debt} {currencies[currency][1]}"
            return response
        else:
            return "Денег нет, держись"


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now()):
        self.amount = amount
        self.comment = comment
        if type(date) == str:
            date_format = '%d.%m.%Y'
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = date.date()