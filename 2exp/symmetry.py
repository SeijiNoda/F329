# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023
from utils import print_m

import matplotlib.pyplot as plt
import numpy as np

datasets = []
OPTIONS_DICT = ['ring', 'base', 'tip']

with open('./data/symmetry.txt', 'r') as f:
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
        #values = [float(x) for x in values]
        matrix.append(float(values[1]))
        #matrix.append(values)

        line = f.readline()
    datasets.append(matrix)
    datasets.pop(0)
print_m(datasets[2])

#ax.set(xlim=(0, 19), ylim=(0, 4))
colors = ['#2ECEF5', '#F5E002', '#F51B68']
color_index = 0

X = np.linspace(0, 19, 39)
yerr = [0.07004041405,0.0700445601,0.07005116416,0.07006068798,0.07007103253,0.0700779145,0.07009418235,0.07010208913,0.07012061038,0.07012954085,0.07013691539,0.0701503129,0.07016229472,0.07017898546,0.07024884341,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07027467538,0.07031297462,0.07033597657,0.07036282328,0.07039069541,0.07041633049,0.07044277394,0.07046657435,0.07049808224,0.07052329332,0.07055286032,0.07057556305,0.07060262035,0.07063831043,0.07065449809]
xerr = [0.1]*39
#plt.plot(X, datasets[0], '.-', color=colors[0], label=OPTIONS_DICT[0])
#plt.plot(X, datasets[2], '.-', color=colors[2], label=OPTIONS_DICT[2])
plt.errorbar(X, datasets[1], xerr=xerr, yerr=yerr, fmt=".-", color=colors[1], label=OPTIONS_DICT[1])
plt.errorbar(X, datasets[0], xerr=xerr, yerr=yerr, fmt=".-", color=colors[0], label=OPTIONS_DICT[0])
plt.errorbar(X, datasets[2], xerr=xerr, yerr=yerr, fmt=".-", color=colors[2], label=OPTIONS_DICT[2])
plt.legend(loc='best')
plt.xlabel('x (cm)')
plt.ylabel('DDP (V)')
plt.title('DDP ao longo do eixo de simetria')
plt.savefig(f'./symmetry/symmetry.pdf', format='pdf', bbox_inches='tight')
plt.show()