
from collections import deque as dq


"""
Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех
предприятий) и отдельно вывести наименования предприятий, чья
прибыль выше среднего и ниже среднего.
"""


def add_company(name, income):
    return [name, income]


# данные о количестве предприятий
companys_quatntity = int(input('Укажите количество предприятий:'))
# их наименования
company = dq()
total_income = int()
while companys_quatntity > 0:
    anual_income = 0
    company_name = input('Укажите название предприятия: ')
    for quarter in range(1, 5):
        income = float(input(f'Какая прибыль {company_name} за '
                             f'{quarter} квартал?'))
        # прибыль за 4 квартала
        anual_income += income
    # company.append(add_company(company_name, anual_income))
    company.append([company_name, anual_income])

    total_income += anual_income
    companys_quatntity -= 1

# среднюю прибыль (за год для всех предприятий)
average_income = total_income / len(company)
print(f'\nСредняя прибыль по всем предприятиям {average_income}\n')

# вывести наименования предприятий, чья прибыль выше среднего
print('Прибыльные предприятия, чья прибыль выше среднего:')
for item in company:
    if item[1] >= average_income:
        print(item[0])

# вывести наименования предприятий, чья прибыль ниже среднего
print('*' * 50, '\n\nУбыточные предприятия, чья прибыль ниже среднего:')
for item in company:
    if item[1] < average_income:
        print(item[0])
