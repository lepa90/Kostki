from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

"""utworzenie kosci typu d6"""
die1 = Die()
die2 = Die()
"""Wykonanie pewnej ilosci rzutow i umieszczenie wynikow na liscie"""
results = []

for roll_results in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequiences = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequiences.append(frequency)

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequiences)]
x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwosc wystepowania wartosci'}
my_layout = Layout(title='Wynik rzucania pojedyncza koscia D6 tysiac razy', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')