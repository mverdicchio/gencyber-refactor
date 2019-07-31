# step 2: factor out the method
class DateCalculator2:

    @staticmethod
    def convert(days):
        year = 1980
        while days > 365:
            if DateCalculator2.is_leap_year(year):
                if days > 366:
                    days -= 366
                    year += 1
            else:
                days -= 365
                year += 1

        return year

    @staticmethod
    def is_leap_year(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


assert DateCalculator2.is_leap_year(2004)
assert not DateCalculator2.is_leap_year(1900)
assert DateCalculator2.is_leap_year(2000)
