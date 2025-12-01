from matplotlib import pyplot

def create_chart(x,y,filename):
    pyplot.scatter(x, y, alpha=0.5)
    pyplot.savefig(f"{filename}.png")

# if you want separated graphs
# def create_chart(x,y):
#     figure = pyplot.figure()
#     pyplot.scatter(x, y, alpha=0.5)
#     figure.savefig("chart.png")
