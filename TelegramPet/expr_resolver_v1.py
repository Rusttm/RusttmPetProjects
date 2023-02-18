# Урок 11. Jupyter Notebook и несколько слов об аналитике
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

""" модуль для решения строкового уравнения и нахождения его корней и максимумов"""

from math import *
import sympy
from sympy.plotting import plot

class ExpressionResolver:

    def __init__(self, user_name='1', expression_str='x*sin(x)', interval=(-10, 10), accuracy=3):
        self.user_name = user_name
        self.input_expression_str = expression_str
        self.left = min(interval)
        self.right = max(interval)
        self.accuracy = accuracy
        self.is_function = False
        self.result = {'roots': [], 'minmax': [], 'function+_': [], 'function_grow': []}
        self.roots = []
        self.minmax = {'min': [], 'max': []}
        self.posneg_func = {'pos': [], 'neg': []}
        self.growfall_func = {'grow': [], 'fall': []}




    def resolve(self):
        try:   # выдаст ошибку, если не cможет конвертировать строку
            self.format_expression()
            self.check_x()
        except Exception as e:
            print(e)
            return ["end", f"Выражение {self.input_expression_str} не распознано"]


        if not self.is_function:   # если это не функция возвращаем результат выражения
            try:
                return ["end", f"Выражение {self.corrected_expr} = {round(eval(self.corrected_expr), self.accuracy)}"]
            except Exception as e:
                print(e)
                return ["end", f"Выражение {self.input_expression_str} не корректно"]


        else:  # если это функция - решаем

            try: # проверяем, может ли конвертироваться в  sympy
                self.sympy_converter()
            except Exception as e:
                print(e)
                return ["end", f"Выражение {self.input_expression_str} не конвертируется в sympy"]


            try: # проверяем, может найти корни
                self.func_roots_resolver()  # находим корни уравнения
                # self.func_minmax_resolver()
            except Exception as e:
                print(e)
                return ["end", f"Не могу найти корни функции {self.input_expression_str}"]

            try: # проверяем, может найти минмакс
                self.func_minmax_resolver()
            except Exception as e:
                print(e)
                return ["end", f"Не могу найти минмакс функции {self.input_expression_str}"]



            return ["end", f"Решение {self.result} "]


    def format_expression(self):
        """ форматирует строку в нормальный формат пример 2xˆ4 -> 2*x**4 и создает правильную строку"""
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        multy = ['*', '/', '(', ')']
        symbols = [char for char in 'xabcdefghijklmnopqrstuvwyz']
        corrected_expr = ''
        for char in self.input_expression_str:
            if char == ' ':
                continue
            elif char in symbols:
                if (corrected_expr != ''):
                    if (corrected_expr[-1] in digits):
                        corrected_expr += '*' + char
                        continue
                corrected_expr += char
            elif char == '^':
                corrected_expr += '**'
            else:
                corrected_expr += char
        self.corrected_expr = corrected_expr
        print(self.corrected_expr)

    def check_x(self):
        """ проверяет является ли выражение функцией """
        checker_list = ['*x', 'x*', '(x', 'x)', ]
        for char in checker_list:
            if self.corrected_expr.count(char):
                self.is_function = True
                break

    def func_value(self, x0=0, diff=False):
        """ находит значение уравнения в заданной точке """
        x = x0
        if diff:
            return round(eval(self.dif_expr), self.accuracy)
        else:
            return round(eval(self.corrected_expr), self.accuracy)

    def func_roots_resolver(self):
        y_is_positive = self.func_value(self.left) >= 0
        left_accuracy = self.left*10**(self.accuracy)
        right_accuracy = self.right*10**(self.accuracy)
        if y_is_positive:
            pos = self.left
            neg = 0
        else:
            neg = self.left
            pos = 0
        for x_accuracy in range(left_accuracy, right_accuracy, 1):
            x = x_accuracy*10**(-self.accuracy)
            y = self.func_value(x)
            if (y_is_positive) ^ (y > 0):
                # self.roots.append([round(x, self.accuracy), round(y, self.accuracy)])
                self.roots.append(round(x, self.accuracy))
                y_is_positive = y > 0
                if pos:
                    self.posneg_func['pos'].append((round(pos, self.accuracy), round(x, self.accuracy)))
                    pos = 0
                    neg = x
                elif neg:
                    self.posneg_func['neg'].append((round(neg, self.accuracy), round(x, self.accuracy)))
                    neg = 0
                    pos = x

        self.result['roots'] = self.roots
        self.result['function+_'] = self.posneg_func

    def sympy_converter(self):
        self.sympy_expr = sympy.sympify(self.corrected_expr)
        x = sympy.Symbol('x')
        self.sympy_dif_expr = sympy.diff(self.sympy_expr, x)
        self.dif_expr = str(sympy.diff(self.sympy_expr, x))


    def func_minmax_resolver(self):
        """ находит производную и по ней ищет минимумы и максимумы """
        left_value = self.func_value(x0=self.left, diff=True)
        y_diff_is_positive = left_value >= 0
        # (True, False) - максимальные значения
        # (False, True) - минимальные значения
        left_accuracy = self.left*10**(self.accuracy)
        right_accuracy = self.right*10**(self.accuracy)
        grow = 0
        fall = 0
        if y_diff_is_positive:
            grow = self.left
            fall = 0
        else:
            grow = 0
            fall = self.left

        for x_accuracy in range(left_accuracy, right_accuracy, 1):
            x = x_accuracy*10**(-self.accuracy)
            y_diff = self.func_value(x, diff=True)
            if (y_diff_is_positive, y_diff > 0) == (True, False):
                y = self.func_value(x0=x)
                # self.minmax['max'].append([round(x, self.accuracy), round(y, self.accuracy)])
                self.minmax['max'].append((round(x, self.accuracy), round(y, self.accuracy)))
                self.growfall_func['grow'].append((round(grow, self.accuracy), round(x, self.accuracy)))
                grow = 0
                fall = x
            elif (y_diff_is_positive, y_diff > 0) == (False, True):
                y = self.func_value(x0=x)
                # self.minmax['min'].append([round(x, self.accuracy), round(y, self.accuracy)])
                self.minmax['min'].append((round(x, self.accuracy), round(y, self.accuracy)))
                self.growfall_func['fall'].append((round(fall, self.accuracy), round(x, self.accuracy)))
                grow = x
                fall = 0

            y_diff_is_positive = y_diff > 0
        self.result['function_grow'] = self.growfall_func
        self.result['minmax'] = self.minmax


    def draw_expression(self, name='sympy_img'):
        # sympy.init_printing()
        x = sympy.Symbol('x')
        graph = sympy.plot(self.sympy_expr, (x, self.left, self.right), show=False, title='Function')
        graph.save(f'{self.user_name}.png')
        graph = sympy.plot(sympy.diff(self.sympy_expr, x), (x, self.left, self.right), show=False, title='Derivative')
        graph.save(f'{self.user_name}_diff.png')


my_expression_str = '-12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30'
# my_expression_str = '-12x^4 - 18x^3+5x^2 + 10x - 30'
# my_expression_str = '-12/4 - 18*(3+5)  - 30'
new_expression = ExpressionResolver(expression_str=my_expression_str, interval=(10,-10), accuracy=4)
print(new_expression.resolve())
new_expression.draw_expression()

