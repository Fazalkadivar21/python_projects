import datetime


class Age:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def age_calc(self):
        sys_date = datetime.date.today()
        given_date = datetime.date(self.year, self.month, self.day)

        age = sys_date.year - given_date.year

        if sys_date.month < given_date.month or (sys_date.month == given_date.month and sys_date.day < given_date.day):
            age -= 1

        return age


date = int(input("enter date : "))
month = int(input("enter month : "))
year = int(input("enter year : "))

x = Age(year, month, date)

print(x.age_calc())
