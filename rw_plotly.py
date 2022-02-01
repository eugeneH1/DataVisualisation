from plotly.graph_objs import Bar, Layout

from random_walk import RandomWalk
from plotly import offline

steps = 50_000
rw = RandomWalk(steps)
rw.fill_walk()

# Get step data
right_steps = 0
left_steps = 0
up_steps = 0
down_steps = 0
step_size0 = 0
step_size1 = 0
step_size2 = 0
step_size3 = 0
step_size4 = 0

step_data = []

x_values = rw.x_values
y_values = rw.y_values


for i in range(len(x_values) - 1):
    step = x_values[i + 1] - x_values[i]
    step_size = abs(step)
    if step_size > 0:
        if abs(step) == 1:
            step_size1 += 1
        elif step_size == 2:
            step_size2 += 1
        elif step_size == 3:
            step_size3 += 1
        else:
            step_size4 += 1
    else:
        step_size0 += 1
    if step > 0:
        right_steps += 1
    elif step != 0:
        left_steps += 1

for i in range(len(y_values) - 1):
    step = y_values[i + 1] - y_values[i]
    step_size = abs(step)
    if step_size > 0:
        if abs(step) == 1:
            step_size1 += 1
        elif step_size == 2:
            step_size2 += 1
        elif step_size == 3:
            step_size3 += 1
        else:
            step_size4 += 1
    else:
        step_size0 += 1
    if step > 0:
        up_steps += 1
    elif step != 0:
        down_steps += 1

step_data.append(right_steps)
step_data.append(left_steps)
step_data.append(up_steps)
step_data.append(down_steps)
step_data.append(step_size0)
step_data.append(step_size1)
step_data.append(step_size2)
step_data.append(step_size3)
step_data.append(step_size4)
x_axis = ['Right Steps', 'Left Steps', 'Up Steps', 'Down Steps', '0', '1 Step', '2 Steps', '3 Steps', '4 Steps']
# Visualise the results
data = [Bar(x=x_axis, y=step_data)]


x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Total steps in each direction({steps} movements between 1-4 steps)', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='rw.html')
print(x_values)
print(y_values)
# print(up_steps)
# print(down_steps)
# print(right_steps)
# print(left_steps)
# for i in range(die_3.num_sides * 3 - 2):
#     print(f"{i + 3} = frequency = {frequencies[i]}")
