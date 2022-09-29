import pandas as pd

table = pd.read_excel('data\commands_perfomances.xlsx')
print(table['WTP'][0])