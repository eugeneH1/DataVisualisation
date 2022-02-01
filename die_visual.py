from plotly.graph_objs import Bar, Layout
from random_walk import RandomWalk

from die import Die
from plotly import offline

die_1 = Die()
die_2 = Die()
# die_3 = Die()
rw = RandomWalk(100)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for i in range(1_000_000)]



# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides # + die_3.num_sides
frequencies = [results.count(i) for i in range(2, max_result + 1)]


# Visualise the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]
#data = [Bar(x=rw.x_values, y=rw.y_values)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling two die 1 000 000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

# print(results)
# print()
# print(frequencies)
# for i in range(die_3.num_sides * 3 - 2):
#     print(f"{i + 3} = frequency = {frequencies[i]}")
