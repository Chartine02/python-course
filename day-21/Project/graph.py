from matplotlib import pyplot

x_data = [ 1, 2, 3, 4, 5]
y_data = [5.5, 6.4, 5.3, 4.4, 7.9]

figure = pyplot.figure()
pyplot.scatter(x_data, y_data)
figure.savefig("graph.png")

x_data = [ 1, 2, 3, 4, 5]
y_data = [1.3, 4.4, 5.3, 6.6, 7.7]

figure = pyplot.figure()
pyplot.scatter(x_data, y_data)
figure.savefig("graph.png")