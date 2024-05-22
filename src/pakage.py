import csv
import pandas as pd


with open('../data/transactions.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

data = pd.read_excel("..\\data\\transactions_excel.xlsx")
print(data)
