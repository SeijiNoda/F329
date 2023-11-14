# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023
from utils import print_m, hex_to_rgba, least_sqr_fit

import matplotlib.pyplot as plt
import numpy as np
import math

datasets = []
OPTIONS_DICT = ['current', 'resistance']
COLORS = ['#F26CA7', '#2ECEF5']

with open('./3exp/data/resistor.txt', 'r') as f:
    line = f.readline()

    matrix = []
    while line:
        # removes headers and moves on to the next table/matrix
        try:
            x = int(line.replace('-', '')[0])  # removes negative sign that fails the validation
        except:
            line = f.readline()
            datasets.append(matrix)
            matrix = []
        
        line = line.strip()         #removes \n
        values = line.split(',')
        values = [float(x) for x in values]
        matrix.append(values)  

        line = f.readline()
    datasets.append(matrix)
    datasets.pop(0)

    
    for setup in range(2):
        X = [] 
        Y = []
        ux = [] # uncertainty
        uy = []
        for i in range(len(datasets[setup])):
            X.append(datasets[setup][i][0])
            Y.append(datasets[setup][i][2])
            ux.append(datasets[setup][i][1])
            uy.append(datasets[setup][i][3])

        # Y = [y/1000 for y in X]
        (a, b) = least_sqr_fit(X, Y)
        print(f'{a}x + {b}')
        f = lambda x: a*x + b
        fx = np.linspace(-10, 10, 1000)
        fy = f(fx)

        fig, ax = plt.subplots()
        ax.set_xlabel('Voltagem (V)')
        ax.grid(which='both', axis='both', linestyle='--')
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
        ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        
        
        if OPTIONS_DICT[setup] == 'current':
            ax.plot(fx, fy, color=COLORS[setup], alpha=0.5, label=f'I(x) = ({a:.4f} ± )x + ({b:.4f} ± )')
            ax.plot(X, Y, marker='.', color=COLORS[setup], linestyle='none')
            ax.set_xlim((-1,1))
            ax.set_ylim((-9, 9))
            ax.set_ylabel('Corrente (mA)')     
            ax.set_title('Resistor: Voltagem x Corrente')
        else: # OPTIONS_DICT[setup] == 'resistance'
            ax.plot(fx, fy, color=COLORS[setup], alpha=0.5, label=f'R(x) = ({a:.4f} ± )x + ({b:.4f} ± )')
            ax.plot(X, Y, marker='.', color=COLORS[setup], linestyle='none')
            ax.set_xlim((-1,1))
            ax.set_ylim((0.1, 110))
            ax.set_ylabel('Resitência (Ω)')
            ax.set_title('Resistor: Voltagem x Resistência')
        ax.legend()
        
        #plt.errorbar(X, Y, xerr=ux, yerr=uy, fmt=".-", color=COLORS[setup], label=OPTIONS_DICT[setup])
        plt.show()