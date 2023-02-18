import matplotlib.pyplot as plt
import base64
from io import BytesIO
from . import expression as resolver

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)

    graph = graph.decode('utf-8')

    buffer.close()
    return graph
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5, 5))
    plt.title('test matplotlib')
    plt.plot(x, y)
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout
    graph = get_graph()
    return graph

def get_func(function_string='sin(x)', range = (-10,10), accuracy=3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7, 5))
    plt.title(function_string)
    function = resolver.ExpressionResolver(expression_str=function_string, interval=range, accuracy=accuracy)
    if function.CheckExpression():
        function.sympy_converter()
        x, y = function.GetValues()
        plt.plot(x, y)
        x_diff, y_diff = function.GetDiff()
        plt.plot(x_diff, y_diff, ls=':')
        plt.grid()
    else:
        plt.plot([0], [0])
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.tight_layout
    graph = get_graph()
    return graph

