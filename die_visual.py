from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

"""utworzenie kosci typu d6"""
die = Die()
"""Wykonanie pewnej ilosci rzutow i umieszczenie wynikow na liscie"""
results = []
for roll_results in range(1000):
    result = die.roll()
    results.append(result)

frequiences = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequiences.append(frequency)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequiences)]
x_axis_config = {'title': 'Wynik'}
y_axis_config = {'title': 'Częstotliwosc wystepowania wartosci'}
my_layout = Layout(title='Wynik rzucania pojedyncza koscia D6 tysiac razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')