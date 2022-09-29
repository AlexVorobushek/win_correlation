from typing import Iterable
import pandas as pd


# def get_Pirson_coefficient(X: Iterable, Y: Iterable) -> float:
#     n = len(X) # == len(Y)
#     E = lambda expression: sum([eval(expression.format(x, y)) for x, y in zip(X, Y)])
#     return (n*E('{0} - {1}') - ( E('{0}') * E('{1}') )) / ( n*E('{0}**2') - E('{0}')**2*n*E('{1}**2') - E('{1}')**2 )**0.5

def get_Pirson_coefficient(X: Iterable, Y: Iterable) -> float:
    n = len(X) # == len(Y)
    xm = sum(X) / n  # middle of X
    ym = sum(Y) / n  # middle of Y
    numerator = sum([x-xm for x in X])*sum([y-ym for y in Y])
    denominator = (sum([(x-xm)**2 for x in X])*sum([(y-ym)**2 for y in Y]))**0.5
    return numerator / denominator


table = pd.read_excel('data\commands_perfomances.xlsx')
perfomances: pd.core.indexes.base.Index = table.columns[5:]

data_of_win_persents: list = table['W %'].tolist()

correlations_by_perfomance = dict()
for perfomance in perfomances:
    data_of_perfomanse: list = table[perfomance].tolist()
    correlations_by_perfomance[perfomance] = get_Pirson_coefficient(data_of_win_persents, data_of_perfomanse)

print(*sorted(correlations_by_perfomance.items(), key=lambda x: x[1]), sep='\n')
