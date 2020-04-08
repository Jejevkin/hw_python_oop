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
        remained = self.limit - self.get_today_stats()
        if remained > 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал"
        else:
            return "Хватит есть!"


class CashCalculator(Calculator):
    USD_RATE = 67.00
    EURO_RATE = 78.00

    def get_today_cash_remained(self, currency):
        currencies = {'rub': [1, 'руб'],
                      'usd': [self.USD_RATE, 'USD'],
                      'eur': [self.EURO_RATE, 'Euro'],
                      }
        balance = self.limit - self.get_today_stats()
        balance = round(balance / currencies[currency][0], 2)
        currency_name = currencies[currency][1]
        if balance > 0:
            return f"На сегодня осталось {balance} {currency_name}"
        elif balance < 0:
            return f"Денег нет, держись: твой долг - {abs(balance)} {currency_name}"
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