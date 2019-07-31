# factor out bodies of if/else to:
# 1. give a name/ID purpose
# 2. isolate code for testing
# multiple methods sharing variables means we should use a class with instance variables.


class DateCalculator3:
    def __init__(self, days, year):
        self.days = days
        self.year = year

    def convert(self):
        year = 1980
        while self.days > 365:
            if self.is_leap_year():
                self.add_leap_year()
            else:
                self.add_regular_year()
        return year

    def is_leap_year(self):
        return self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0)

    def add_leap_year(self):
        if self.days > 366:
            self.days -= 366
            self.year += 1

    def add_regular_year(self):
        self.days -= 365
        self.year += 1


# test leap year detection 225 days into the year
dc = DateCalculator3(225, 2004)
assert dc.is_leap_year()
dc = DateCalculator3(225, 1900)
assert not dc.is_leap_year()
dc = DateCalculator3(225, 2000)
assert dc.is_leap_year()


dc = DateCalculator3(225, 2008)
dc.add_leap_year()
assert dc.year == 2008, "expect year to stay the same if not a year's worth of days"

dc = DateCalculator3(400, 2008)
dc.add_leap_year()
assert dc.year == 2009, "expect year to increment if >1 year's worth of days left"

dc = DateCalculator3(366, 2008)
dc.add_leap_year()
assert dc.year == 2009, "expect year to increment if exactly 1 leap year's worth of days left"
