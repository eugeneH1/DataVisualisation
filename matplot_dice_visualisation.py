import matplotlib.pyplot as plt
from die import Die

die_1 = Die()
die_2 = Die()
# die_3 = Die()

# Make some rolls, and store results in a list.
rolls = 1000
results = [die_1.roll() + die_2.roll() for i in range(rolls)]



# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides# + die_3.num_sides
frequencies = [results.count(i) for i in range(2, max_result + 1)]

x_axis = [i for i in range(2, max_result + 1)]


# Set up pyplot
plt.style.use('classic')
fig, ax = plt.subplots()

ax.plot(x_axis, frequencies)

plt.show()
# print(frequencies)