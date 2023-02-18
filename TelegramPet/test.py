import sympy
import os
from PIL import Image, ImageChops
import matplotlib.pyplot as plt
import platform

sympy.init_printing()
user_name = 15
sympy_expr = sympy.sympify('cos(x)')
x = sympy.Symbol('x')
graph = sympy.plot(sympy_expr, (x, -3, 3), show=False, title=f'Function: \n{sympy_expr}')
# graph.save(os.path.join(os.path.dirname(__file__), f'{user_name}.png'))
# graph.save('234.png')
# graph.saveimage('plot.png', format='png')

# im = Image.open(graph)
for plot in graph:
    pts = plot.get_points()
    plt.plot(pts[0], pts[1])
# plt.show()
plt.savefig('foo.pdf')
print(os.path.join(os.path.dirname(__file__), f'{user_name}.png'))
print(platform.system())