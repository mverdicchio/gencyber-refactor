# step 1: fix bad variable names
class DateCalculator:

    def convert(days):
        year = 1980
        while days > 365:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 == 0):
                if days > 366:
                    days -= 366
                    year += 1
            else:
                days -= 365
                year += 1

        return year
