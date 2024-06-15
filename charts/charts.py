import matplotlib.pyplot as plotpy # type: ignore

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plotpy.subplots()
    ax.pie(values, labels=labels)
    plotpy.savefig('pie.png')
    plotpy.close()

generate_pie_chart()