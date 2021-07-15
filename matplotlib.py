import random
import matplotlib.pyplot as plt
import numpy as np

print('Statistics diagram program.')

name = input('Name: ')
lower_number = int(input('Lower number: '))
upper_number = int(input('Upper number[max=15]: '))
diagram = input('[subplot,line,bar]> Diagram: ')
number_x = []
number_y = []


class Diagraminfo(object):
    def checknumbers(self):
        for i in range(0, 16):
            num = random.randint(lower_number, upper_number)
            number_x.append(i)
            number_y.append(num)
        if diagram == 'line':
            now = diagramspec()
            now.linediag()
        elif diagram == 'bar':
            now1 = diagramspec()
            now1.bardiag()
        elif diagram == 'subplot':
            now2 = diagramspec()
            now2.plotting()
        else:
            print('Diagram is incorrect. Try again!')


class diagramspec(Diagraminfo):
    def linediag(self):
        plt.plot(number_x, number_y, label='Price', linestyle='-.', linewidth='1', marker='o', markersize='4',
                 color='red')
        plt.rc('grid', color='#bbb', linestyle='--')
        plt.title(f'{name} diagram statistics.', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xlabel('Days', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.ylabel('Statistics', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.legend()
        plt.grid()
        plt.show()

    def bardiag(self):
        plt.bar(number_x, number_y, label='Price', align='center', color='green')
        plt.title(f'{name} diagram statistics.', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xlabel('Days', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.ylabel('Statistics', fontdict={'fontname': 'Courier New', 'fontsize': 20})
        plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        plt.legend()
        plt.show()

    def plotting(self):
        x = np.arange(0, 3 * np.pi, 0.1)
        y_sin = np.sin(x)
        y_cos = np.cos(x)

        plt.subplot(2, 1, 1)
        plt.plot(x, y_sin)
        plt.title(f'{name} sine diagram statistics.', fontdict={'fontname': 'Courier New', 'fontsize': 10})
        plt.subplot(2, 1, 2)
        plt.plot(x, y_cos)
        plt.title(f'{name} cose diagram statistics.', fontdict={'fontname': 'Courier New', 'fontsize': 10})
        plt.show()


i = Diagraminfo()
i.checknumbers()
