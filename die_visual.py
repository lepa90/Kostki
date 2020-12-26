from die import Die
"""utworzenie kosci typu d6"""
die = Die()
"""Wykonanie pewnej ilosci rzutow i umieszczenie wynikow na liscie"""
results = []
for roll_results in range(100):
    result = die.roll()
    results.append(result)

print(results)