import matplotlib.pyplot as plt


def input_size(num, color):

    x_axis = [i for i in range(1, num)]
    y_axis = [x**3 for x in x_axis]

    fig, ax = plt.subplots()
    cmap_string = f"{color.title()}"
    ax.scatter(x_axis, y_axis, c=y_axis, cmap=cmap_string)


input_size(5000, 'blues')
plt.show()

