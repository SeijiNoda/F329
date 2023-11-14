# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023
from utils import print_m, hex_to_rgba, least_sqr_fit

import matplotlib.pyplot as plt
import numpy as np
import math

datasets = []
OPTIONS_DICT = ['current', 'resistance']
COLORS = ['#F26CA7', '#2ECEF5']
log = True

with open('./3exp/data/diode.txt', 'r') as f:
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
        
        

        fig, ax = plt.subplots()
        #ax.set_xlim((-10, 10))
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
            # 
            if log:
                start = 0
                while Y[start] == 0:
                    start += 1
                (a, b) = least_sqr_fit(X[start:], np.log(Y[start:]))
                print(f'{a}x + {b}')
                f = lambda x: a*x + b
                fx = np.linspace(-10, 10, 1000)
                fy = f(fx)
                ax.plot(fx, fy, color=COLORS[setup], linestyle='-', alpha=0.5, label=f'I(x) = ({a:.4f} ±)x + ({b:.4f} ±)')
                ax.legend()

                ax.set_xlim((0.3, 0.7))
                ax.set_ylim((-10, 10))
                ax.set_ylabel('Log Corrente (ln(mA))')     
                ax.set_title('Diodo: Voltagem x Log da Corrente')
                ax.plot(X[start:], np.log(Y[start:]), marker='.', color=COLORS[setup], linestyle='none')
            else:                
                ax.set_xlim((-0.2, 0.7))
                ax.set_ylim((-0.5, 6))
                ax.set_ylabel('Corrente (mA)')     
                ax.set_title('Diodo: Voltagem x Corrente')
                ax.plot(X, Y, marker='.', color=COLORS[setup], linestyle='none')
        else: # OPTIONS_DICT[setup] == 'resistance'
            if log:
                start = 0
                while Y[start] == 0:
                    start += 1
                (a, b) = least_sqr_fit(X[start:], np.log(Y[start:]))
                print(f'{a}x + {b}')
                f = lambda x: a*x + b
                fx = np.linspace(-10, 10, 1000)
                fy = f(fx)
                ax.plot(fx, fy, color=COLORS[setup], linestyle='-', alpha=0.5, label=f'R(x) = ({a:.4f} ±)x + ({b:.4f} ±)')
                ax.legend()

                ax.set_xlim((0, 1))
                ax.set_ylim((0, 20))
                ax.set_ylabel('Log Resistência (ln(Ω))')     
                ax.set_title('Diodo: Voltagem x Log da Corrente')
                ax.plot(X[start:], np.log(Y[start:]), marker='.', color=COLORS[setup], linestyle='--')
            else:
                ax.set_xlim((-0.15, 0.75))
                ax.set_ylim((0, 10000))
                ax.set_ylabel('Resitência (Ω)')
                ax.set_title('Diodo: Voltagem x Resistência')
                ax.plot(X, Y, marker='.', color=COLORS[setup], linestyle='--')
            
        #plt.errorbar(X, Y, yerr=u, fmt=".-", color=COLORS[setup], label=OPTIONS_DICT[0])
        plt.show()