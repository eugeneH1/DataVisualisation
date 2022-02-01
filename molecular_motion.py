import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

fig, ax = plt.subplots()

ax.plot(rw.x_values, rw.y_values, linewidth=1, c='red')

plt.show()
