# Урок 11. Jupyter Notebook и несколько слов об аналитике
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

""" модуль для решения строкового уравнения и нахождения его корней и максимумов
    используется в боте

"""

# from math import *
import sympy
from sympy.plotting import plot
from sympy import *
from sympy.abc import x
from sympy import Symbol, solve
import platform
import matplotlib.pyplot as plt

class ExpressionResolver:

    def __init__(self, user_name='1', expression_str='x*sin(x)', interval=(-10, 10), accuracy=3):
        self.user_name = user_name
        self.queue = 4 # ['accuracy', 'range', 'expression']
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
        # self.func_value = lambdify(x, self.input_expression_str)


    def CheckExpression(self):
        """ проверяет выражение ли это? """
        try:
            self.format_expression()
            self.check_x()
            return True

        except:
            return False

    def GetValues(self):
        left_accuracy = self.left * 10 ** (self.accuracy)
        right_accuracy = self.right * 10 ** (self.accuracy)
        x_list = []
        y_list = []
        try:
            for x_accuracy in range(left_accuracy, right_accuracy+1, 1):
                x = x_accuracy * 10 ** (-self.accuracy)
                x_list.append(x)
                y_list.append(self.func_value(x))
            return (x_list, y_list)
        except Exception as e:
            print(e)
            return ([0],[0])

    def GetDiff(self):
        left_accuracy = self.left * 10 ** (self.accuracy)
        right_accuracy = self.right * 10 ** (self.accuracy)
        x_list = []
        y_list = []
        try:
            for x_accuracy in range(left_accuracy, right_accuracy+1, 1):
                x = x_accuracy * 10 ** (-self.accuracy)
                x_list.append(x)
                y_list.append(self.func_diff_value(x))
            return (x_list, y_list)
        except Exception as e:
            print(e)
            return ([0],[0])




    def resolve(self):
        # убрать для бота
        # self.is_function = True
        # self.format_expression()
        #

        if not self.is_function:   # если это не функция возвращаем результат выражения
            try:
                return ["end", f"Выражение {self.corrected_expr} = {round(solve(self.corrected_expr), self.accuracy)}"]
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



            return ["end", f"{self.answer_formatting()} "]


    def format_expression(self):
        """ форматирует строку в нормальный формат пример 2xˆ4 -> 2*x**4 и создает правильную строку"""
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        multy = ['*', '/', '(', ')']
        symbols = [char for char in 'xabcdefghijklmnopqrstuvwyz']
        corrected_expr = ''
        self.input_expression_str = self.input_expression_str.lower()
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

    def func_roots_resolver(self):
        temp = self.func_value(self.left)
        y_is_positive = temp >= 0
        left_accuracy = self.left*10**(self.accuracy)
        right_accuracy = self.right*10**(self.accuracy)
        if y_is_positive:
            pos = self.left
            neg = 0
        else:
            neg = self.left
            pos = 0
        for x_accuracy in range(left_accuracy, right_accuracy+1, 1):
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
        # if pos:
        #     self.posneg_func['pos'].append((round(pos, self.accuracy), round(x, self.accuracy)))
        #     pos = 0
        #     neg = x
        # elif neg:
        #     self.posneg_func['neg'].append((round(neg, self.accuracy), round(x, self.accuracy)))
        #     neg = 0
        #     pos = x


        self.result['roots'] = self.roots
        self.result['function+_'] = self.posneg_func

    def sympy_converter(self):
        try:
            self.sympy_expr = sympy.sympify(self.corrected_expr)
            x = sympy.Symbol('x')
            self.sympy_dif_expr = sympy.diff(self.sympy_expr, x)
            self.dif_expr = str(sympy.diff(self.sympy_expr, x))
            self.func_value = lambdify(x, self.sympy_expr)
            self.func_diff_value = lambdify(x, self.sympy_dif_expr)
            return True
        except Exception as e:
            print(e)
            return False


    def func_minmax_resolver(self):
        """ находит производную и по ней ищет минимумы и максимумы """

        left_value = self.func_diff_value(self.left)
        y_diff_is_positive = left_value >= 0
        # (True, False) - максимальные значения
        # (False, True) - минимальные значения
        left_accuracy = self.left*10**(self.accuracy)
        right_accuracy = self.right*10**(self.accuracy)
        grow = 0
        fall = 0
        # крайняя левая точка
        y = self.func_value(left_value)
        if y_diff_is_positive:
            grow = self.left
            fall = 0
            self.minmax['min'].append((round(left_value, self.accuracy), round(y, self.accuracy)))
        else:
            grow = 0
            fall = self.left
            self.minmax['max'].append((round(left_value, self.accuracy), round(y, self.accuracy)))

        for x_accuracy in range(left_accuracy, right_accuracy+1, 1):
            x = x_accuracy*10**(-self.accuracy)
            y_diff = self.func_diff_value(x)
            if (y_diff_is_positive, y_diff > 0) == (True, False):
                y = self.func_value(x)
                # self.minmax['max'].append([round(x, self.accuracy), round(y, self.accuracy)])
                self.minmax['max'].append((round(x, self.accuracy), round(y, self.accuracy)))
                self.growfall_func['grow'].append((round(grow, self.accuracy), round(x, self.accuracy)))
                grow = 0
                fall = x
            elif (y_diff_is_positive, y_diff > 0) == (False, True):
                y = self.func_value(x)
                # self.minmax['min'].append([round(x, self.accuracy), round(y, self.accuracy)])
                self.minmax['min'].append((round(x, self.accuracy), round(y, self.accuracy)))
                self.growfall_func['fall'].append((round(fall, self.accuracy), round(x, self.accuracy)))
                grow = x
                fall = 0
            y_diff_is_positive = y_diff > 0

        # крайняя правая точка
        y = self.func_value(x)
        if grow:
            self.minmax['max'].append((round(x, self.accuracy), round(y, self.accuracy)))
            self.growfall_func['grow'].append((round(grow, self.accuracy), round(x, self.accuracy)))
        else:
            self.minmax['min'].append((round(x, self.accuracy), round(y, self.accuracy)))
            self.growfall_func['fall'].append((round(fall, self.accuracy), round(x, self.accuracy)))

        self.result['function_grow'] = self.growfall_func
        self.result['minmax'] = self.minmax


    def answer_formatting(self):
        result_string = 'Решение:\n'
        if self.result['roots'] != []:
            result_string += 'Корни уравнения f(x)=0: \n'
            for i, elem in enumerate(self.result['roots']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'x{i}={elem}'
            result_string += '\n'
        else:
            result_string += 'Корней нет\n'

        if self.result['minmax']['min'] != []:
            result_string += 'Минимумы функции f(x): \n'
            for i, elem in enumerate(self.result['minmax']['min']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'x{i}={elem[0]} y{i}={elem[1]}'
            result_string += '\n'
        else:
            result_string += 'Минимумов нет\n'

        if self.result['minmax']['max'] != []:
            result_string += 'Максимумы функции f(x): \n'
            for i, elem in enumerate(self.result['minmax']['max']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'x{i}={elem[0]} y{i}={elem[1]}'
            result_string += '\n'
        else:
            result_string += 'Максимумов нет\n'

        if self.result['function+_']['pos'] != []:
            result_string += 'Функция f(x) положительна на отрезках: \n'
            for i, elem in enumerate(self.result['function+_']['pos']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'({elem[0]}:{elem[1]})'
            result_string += '\n'
        else:
            result_string += 'Функция не положительна \n'

        if self.result['function+_']['neg'] != []:
            result_string += 'Функция f(x) отрицательна на отрезках: \n'
            for i, elem in enumerate(self.result['function+_']['neg']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'({elem[0]}:{elem[1]})'
            result_string += '\n'
        else:
            result_string += 'Функция не отрицательна \n'

        if self.result['function_grow']['grow'] != []:
            result_string += 'Функция f(x) растет на отрезках: \n'
            for i, elem in enumerate(self.result['function_grow']['grow']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'({elem[0]}:{elem[1]})'
            result_string += '\n'
        else:
            result_string += 'Функция не растет \n'

        if self.result['function_grow']['fall'] != []:
            result_string += 'Функция f(x) падает на отрезках: \n'
            for i, elem in enumerate(self.result['function_grow']['fall']):
                if i != 0:
                    result_string += ', \n'
                result_string += f'({elem[0]}:{elem[1]})'
            result_string += '\n'
        else:
            result_string += 'Функция не падает\n'

        return result_string

    def draw_expression(self, name='sympy_img'):
        try:
            # sympy.init_printing()
            user_name = str(self.user_name)
            x = sympy.Symbol('x')
            graph_f = sympy.plot(self.sympy_expr, (x, self.left, self.right), show=False, title=f'Function: \n{self.corrected_expr}')
            graph_f_diff = sympy.plot(sympy.diff(self.sympy_expr, x), (x, self.left, self.right), show=False, title=f'Derivative: \n{self.dif_expr}')
            if platform.system() == 'Linux':
                # sympy не имплементировал запись на линуксе
                for plot in graph_f:
                    pts = plot.get_points()
                    plt.plot(pts[0], pts[1])
                plt.title(f'Function: \n{self.corrected_expr}\n')
                plt.savefig(f'{user_name}.png')

                for plot2 in graph_f_diff:
                    pts2 = plot2.get_points()
                    plt.plot(pts2[0], pts2[1])
                plt.title(f'Function: \n{self.corrected_expr}\n and \n Derivative ({self.dif_expr})')
                plt.savefig(f'{user_name}_diff.png')



            else:
                graph_f.save(f'{user_name}.png')
                graph_f_diff.save(f'{user_name}_diff.png')
            return True
        except Exception as e:
            print(e)
            return False

if __name__ == '__main__':
    my_expression_str = '-12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30'
    # my_expression_str = '-12x^4 - 18x^3+5x^2 + 10x - 30'
    # my_expression_str = '-12/4 - 18*(3+5)  - 30'
    # my_expression_str = 'cos(x+0.1)'
    new_expression = ExpressionResolver(expression_str=my_expression_str, interval=(-1,1), accuracy=4)
    print(new_expression.resolve())
    new_expression.draw_expression()

