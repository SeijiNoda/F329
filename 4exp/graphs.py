# code by Matheus Seiji L. N. for F 329 - Experimental Physics III in 2s/2023
import matplotlib.pyplot as plt

# osciloscope formatting settings
OSCILOSCOPE_HEADER_LENGTH = 18
DATA_COLUMN_OFFSET = 3
DATA_COLUMN_LENGTH = 2
DATA_COLUMN_LIMIT = DATA_COLUMN_LENGTH + DATA_COLUMN_OFFSET

COLORS = ['#FFC665', '#52B1FA']

# input settings
SETUPS = {
    'resistor': {
        'name': 'Resistor',
        'inputs': ['1 - resistor/F0001CH1.csv', '1 - resistor/F0001CH2.csv'],
        'output': './out/resistor/',
        'xrange': (-15.05, 5.05),
    },
    'diode': {
        'name': 'Diodo',
        'inputs': ['2 - diode/F0004CH1.csv', '2 - diode/F0004CH2.csv'],
        'output': './out/diode/',
        'xrange': (-15.05, 5.05),
    },
    'cap-sin-low': {
        'name': r'Capacitor ($sin$) [$f_c/10$]',
        'inputs': ['3 - sin capacitor (low freq)/F0002CH1.csv', '3 - sin capacitor (low freq)/F0002CH2.csv'],
        'output': './out/cap-sin-low/',
        'xrange': (-50, 50),
    },
    'cap-sin-fc': {
        'name': r'Capacitor ($sin$) [$f_c$]',
        'inputs': ['4 - sin capacitor (fc)/F0004CH1.csv', '4 - sin capacitor (fc)/F0004CH2.csv'],
        'output': './out/cap-sin-fc/',
        'xrange': (-5, 5),
    },
    'cap-sin-high': {
        'name': r'Capacitor ($sin$) [$10f_c$]',
        'inputs': ['5 - sin capacitor (high freq)/F0003CH1.csv', '5 - sin capacitor (high freq)/F0003CH2.csv'],
        'output': './out/cap-sin-high/',
        'xrange': (-0.5, 0.5),
    },
    'cap-sqr-low': {
        'name': r'Capacitor ($sqr$) [$f_c/10$]',
        'inputs': ['6 - sqr capacitor (low freq)/F0000CH1.csv', '6 - sqr capacitor (low freq)/F0000CH2.csv'],
        'output': './out/cap-sqr-low/',
        'xrange': (-50, 50),
    },
    'cap-sqr-fc': {
        'name': r'Capacitor ($sqr$) [$f_c$]',
        'inputs': ['7 - sqr capacitor (fc)/F0001CH1.csv', '7 - sqr capacitor (fc)/F0001CH2.csv'],
        'output': './out/cap-sqr-fc/',
        'xrange': (-5, 5),
    },
    'cap-sqr-high': {
        'name': r'Capacitor ($sqr$) [$10f_c$]',
        'inputs': ['8 - sqr capacitor (high freq)/F0002CH1.csv', '8 - sqr capacitor (high freq)/F0002CH2.csv'],
        'output': './out/cap-sqr-high/',
        'xrange': (-0.5, 0.5),
    },
}

datasets = []
header = []

setup = 'cap-sqr-high'

for i in range(2):
    with open(f'./data/' + SETUPS[setup]['inputs'][i], 'r') as f:
        for _ in range(OSCILOSCOPE_HEADER_LENGTH):
            header.append(f.readline())
        
        matrix = []
        line = f.readline().strip()
        while line:
            values = []
            offset_index = 0
            for x in line.split(','):
                if offset_index >= DATA_COLUMN_OFFSET:
                    values.append(float(x))
                offset_index += 1
                if offset_index == DATA_COLUMN_LIMIT:
                    offset_index = 0
                    
            matrix.append(values)
            line = f.readline().strip()
        datasets.append(matrix)
    f.close()

ch1X = []
ch1Y = []
ch2X = []
ch2Y = []
min_ch_len = min(len(datasets[0]), len(datasets[1]))
for i in range(min_ch_len):
    ch1X.append(datasets[0][i][0] * 1000)
    ch1Y.append(datasets[0][i][1])
    ch2X.append(datasets[1][i][0] * 1000)
    ch2Y.append(datasets[1][i][1])

fig, ax = plt.subplots()
ax.set_xlabel(r'Tempo $\Delta t_0$ (ms)')
ax.grid(which='both', axis='both', linestyle='--')
ax.axhline(y=0, color='#9F9F9F')
ax.set_xlim(SETUPS[setup]['xrange'])
# ax.set_ylim((0, 8))
ax.set_ylabel(r'Amplitude')     
ax.set_title(f'{SETUPS[setup]["name"]}: Amplitude x tempo (CH1 e CH2)')
                    

ax.plot(ch1X, ch1Y, marker='.', color=COLORS[0], label='CH1', linestyle='-')
ax.plot(ch2X, ch2Y, marker='.', color=COLORS[1], label='CH2', linestyle='-')
ax.legend()
plt.savefig(SETUPS[setup]['output'] + setup + '.pdf', format='pdf')
#plt.show()