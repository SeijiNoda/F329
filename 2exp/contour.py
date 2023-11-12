# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023
from utils import print_m, hex_to_rgba

import matplotlib.pyplot as plt
import numpy as np
import math

datasets = []
OPTIONS_DICT = ['base', 'tip', 'ring']

with open('./data/contour.txt', 'r') as f:
    line = f.readline()
    
    matrix = []
    while line:
        # removes headers and moves on to the next table/matrix
        try:
            x = int(line[0])
        except:
            line = f.readline()
            datasets.append(matrix)
            matrix = []
        
        line = line.strip()         #removes \n
        values = line.split(',')
        values.pop(0)               # remove y coordinates indicator
        values = [float(x) for x in values]
        matrix.append(values)

        line = f.readline()
    datasets.append(matrix)
    datasets.pop(0)
    
# what datasets[0] should look like for base experiment setup without axis of symmetry
# x2 = [5.3, 5.3, 5.5, 5.5, 5.6, 5.6, 5.6]
# x1 = [3.0, 3.4, 3.5, 3.5, 3.6, 3.5, 3.6]
# x3 = [7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5]
# x4 = [9.3, 9.3, 9.3, 9.4, 9.4, 9.4, 9.4]
# x5 = [11.5, 11.5, 11.4, 11.4, 11.3, 11.2, 11.1]
# x6 = [13.6, 13.4, 13.4, 13.5, 13.3, 13.2, 13.2]
# x7 = [16.4, 16.0, 15.6, 15.5, 15.2, 15.1, 15.0]

for setup in range(3):
    X = datasets[setup]
    # print_m(X)

    Y = [[2*i]*7 for i in range(15)]
    # This line initializes the following matrix for range(7)
    # Y = [[ 0.,  0.,  0.,  0.,  0.,  0.,  0.],
    #      [ 2.,  2.,  2.,  2.,  2.,  2.,  2.,],
    #      [ 4.,  4.,  4.,  4.,  4.,  4.,  4.],
    #      [ 6.,  6.,  6.,  6.,  6.,  6.,  6.],
    #      [ 8.,  8.,  8.,  8.,  8.,  8.,  8.],
    #      [10., 10., 10., 10., 10., 10., 10.],
    #      [12., 12., 12., 12., 12., 12., 12.]]
    #      [...]

    z1 = np.linspace(0.5, 2, 7)
    z2 = np.linspace(0.5, 3.5, 7)
    z3 = z1
    z_array = [z1, z2, z3]
    Z = [z_array[setup]] * 15
    set_levels = lambda z: z + [z.pop() - 0.001]
    z_levels = set_levels(z_array[setup].tolist())

    fig, ax = plt.subplots()

    color_pallete = ['#05299e', '#5E4AE3', '#947BD3', '#F0A7A0', '#F26CA7', '#F26CA7', '#F26CA7']
    CS = ax.contour(X, Y, Z, levels=z_levels, colors=color_pallete)
    ax.set(xlim=(0, 19), ylim=(0, 28))
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_title(f'Setup: {OPTIONS_DICT[setup]}')
    
    for i in range(len(X[0])):
        color = hex_to_rgba(color_pallete[i], 0.5)
        for j in range(len(Y)):  
            plt.plot(X[j][i], Y[j][i], marker='.', color=color, linestyle='none')

            x0, y0, xa, ya = 0, 0, 0, 0
            if j == len(Y)-1:
                x0, y0, xa, ya = X[j][i], Y[j][i], X[j-1][i], Y[j-1][i]
            else:
                x0, y0, xa, ya = X[j][i], Y[j][i], X[j+1][i], Y[j+1][i]
            dx, dy = xa - x0, ya - y0

            norm = math.hypot(dx, dy) * 1/.3

            dx /= norm
            dy /= norm
            origin = np.array([[0, 0, 0],[0, 0, 0]])
            ax.arrow(x0,y0,-dy, dx, color=color, head_width=0.1)

    set_label_locations = lambda coords: [(x, 2.5) for x in coords]
    manual_locations = set_label_locations(X[0])

    ax.clabel(CS, CS.levels, inline=True, fmt=(lambda v: f'{v:.2f} V'), fontsize=9, manual=manual_locations)

    # plt.show()
    plt.savefig(f'./contour/contour_{OPTIONS_DICT[setup]}.pdf', format='pdf', bbox_inches='tight')
