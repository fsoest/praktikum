import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


# characteristic Curve:
U = [300, 304, 308, 312, 316, 320, 324, 328, 332, 350, 370, 390, 410, 430, 450, 470, 490]
N = [264, 417, 433, 459, 489, 478, 494, 458, 479, 513, 458, 530, 475, 511, 464, 503, 472]
sigma = [i/np.sqrt(i) for i in N]

reg_U = U[5:]
reg_N = N[5:]
U_for_lin_plot = np.arange(min(U)-20, max(U)+20, 1)
slope, intercept, r_value, p_value, std_err = stats.linregress(reg_U, reg_N)
N_for_lin_plot = slope * U_for_lin_plot + intercept

fig, ax = plt.subplots()
ax.errorbar(U, N, yerr=sigma, fmt='x', capsize=5)
ax.set(xlabel='Voltage [V]', ylabel='Impulses [-]',
       title='GMC characteristic curve')
reg_data = "N(U) = {1:.5} 1/V * U + {2:.5} \nR value: {0:.2}".format(r_value, slope, intercept)
fig.text(0.5, 0.5, reg_data, size=10, ha="left", va="center")
ax.plot(U_for_lin_plot, N_for_lin_plot,'b-')


# concentration of K2CO3
fig2 = plt.figure()

# Plot 4mol Histogram
mol_4 = np.loadtxt('4mol.csv', skiprows=1012, delimiter=';', encoding='latin1')
ax1 = plt.subplot(311)
ax1.bar(mol_4[:,0], mol_4[:,1])
ax1.set(title='Histogram for c = 4mol K2C03', ylabel='Absolute\nfrequency [-]',)

# Plot X Mol Histrogram
mol_x = np.loadtxt('xmol.csv', skiprows=1012, delimiter=';', encoding='latin1')
ax2 = plt.subplot(312)
ax2.bar(mol_x[:,0], mol_x[:,1])
ax2.set(title='Histogram for unknown concentration K2C03', ylabel='Absolute\nfrequency [-]',)


# Plot distilled water histogram
mol_0 = np.loadtxt('0mol.csv', skiprows=1012, delimiter=';', encoding='latin1')
ax3 = plt.subplot(313)
ax3.bar(mol_0[:,0], mol_0[:,1])
ax3.set(title='Histogram for distilled water', xlabel='Impulses [-]', ylabel='Absolute\nfrequency [-]',)

fig2.tight_layout()
#fig.savefig('charac.pdf', format='pdf')
fig2.savefig('hist.pdf', format='pdf')

plt.show()
