from sys import argv

_, how_hours, cash_per_hour, premium = argv
how_hours = int(how_hours)
cash_per_hour = int(cash_per_hour)
premium = int(premium)


def wage(how_hours, cash_per_hour, premium):
    worker_wage = (how_hours * cash_per_hour) + premium
    return worker_wage



print(wage(how_hours, cash_per_hour, premium))
