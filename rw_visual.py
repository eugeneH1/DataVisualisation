import matplotlib.pyplot as plt
from random_walk import RandomWalk

#while True:
rw = RandomWalk()
rw.fill_walk()

# Set up pyplot
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
point_numbers = range(rw.num_points)

# Plot points in the walk
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap='Blues', edgecolors='none', s=1)

# Emphasize the starting position (0, 0)
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
# Emphasize the last point
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n':
    #     break

