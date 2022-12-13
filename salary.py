import json
from random import randint


class WorkHours:

    def work_hours(self, month, year):
        return randint(20, 23)*8   

class perHourIncome:

    def per_hour_income(salary, month, year):
        hour_income = salary/WorkHours().work_hours(month,year)
        return round(hour_income, 2)


def main():

    with open('input.json', 'r') as inp:
        data = json.load(inp)
        salary, month, year = data.get("salary"), data.get('month'), data.get('year')
        perHourSalary = perHourIncome.per_hour_income(salary, month, year)

    with open('output.json', 'w') as out:
        data["hour_income"] = perHourSalary
        out.write(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    main()