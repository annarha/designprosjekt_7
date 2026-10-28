import numpy as np
#Plotting
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
#Lese CSV
import csv


header = []
data = []
header2 = []
data2 = []
filename = 'orden_6_frekvensrespons_riktig.csv'
filename2 = 'orden_4_scope_311.csv'

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)
        
with open(filename2) as csvfile2:
    csvreader2 = csv.reader(csvfile2)


    header2 = next(csvreader2)
    for datapoint2 in csvreader2:
        values2 = [float(value2) for value2 in datapoint2]
        data2.append(values2)


time = [(p[0]) for p in data]
ch1 = [(p[3]) for p in data]
ch2 = [(p[2]) for p in data]
ch2_2 = [(q[2]) for q in data2]

frekvens1 = [p[0] for p in data]
frekvens2 = [q[0] for q in data2]

ch2_2_interpolert = np.interp(frekvens1, frekvens2, ch2_2)

# Kaskade i dB = addisjon
kaskade = [a + b for a, b in zip(ch2, ch2_2_interpolert)]


#Enkelt plot
#plt.plot(time, ch1)
#plt.plot(time, ch1, color='firebrick')
#plt.savefig('spektrum.png', dpi=500) #Lagrer figuren, endre filnavn
#plt.show() #Viser figuren



#Subplots
#fig, (channel1, channel2) = plt.subplots(2,1) #2 rader, 1 kolonne
#fig.suptitle('Frekvensrespons til filter med 84.7nF kondensator')
#channel1.plot(time, ch2) #Bruk labels med legend()
#channel2.plot(time, ch1)

#plt.savefig('filnavn2.png', dpi=500)


#Titler etc
fig, (ax1, ax2) = plt.subplots(2,1) #1 rad, 1 kolonne
fig.suptitle('Frekvensrespons til et 4. ordens butterworth-filter')
plt.subplots_adjust(hspace=0.5)
#ax1.plot(time, ch2, color = 'firebrick')
#ax1.plot(time,ch2, color = 'dodgerblue') # Bruk labels med legend()
#ax1.plot(frekvens1, kaskade, color='dodgerblue', label='Kaskade')
#ax2.plot(time, ch1, color = 'dodgerblue' )
#ax.plot(time,ch2, label = 'ch2', color='hotpink', ) #Endre farge

ax1.set_title('Amplituderespons')
ax1.set_xlabel('Frekvens [Hz]')
ax1.set_ylabel('dBV')
ax1.axvline(x=4150, color='firebrick', linestyle='--')
ax1.axvline(x=3115, color='firebrick', linestyle='--')
ax1.text(3115, 0.05, "0.75(f_s/2)", rotation=90, color='firebrick',
             transform=ax1.get_xaxis_transform(),
             ha='right', va='bottom', fontsize=10)
ax1.text(4150, 0.05, "(f_s/2)", rotation=90, color='firebrick',
             transform=ax1.get_xaxis_transform(),
             ha='right', va='bottom', fontsize=10)
ax1.axhline(y=-3, color='firebrick', linestyle='--')
ax1.axhline(y=-10, color='firebrick', linestyle='--')

#f1, f2 = 3115, 4150

#for f in (f1, f2):
    #ax1.axvline(f, color='firebrick', linestyle='--')
    #ax1.text(f, 0.05, "", rotation=90, color='firebrick',
             #transform=ax1.get_xaxis_transform(),
             #ha='right', va='bottom', fontsize=10)


ax2.set_title('Faserespons')
ax2.set_xlabel('Frekvens [Hz]')
ax2.set_ylabel('Fase °')

ax2.grid(True) 
ax1.grid(True)
ax1.set_xlim(left=1000, right=10000)
ax1.set_ylim(top=1, bottom=-40)
ax2.set_xlim(left=1000, right=10000)
ax1.set_xscale('log')
ax2.set_xscale('log')
ax1.xaxis.set_major_formatter(ScalarFormatter())
ax2.xaxis.set_major_formatter(ScalarFormatter())

f1, f2 = 3150, 4150        #x posisjon for linjer  
xmin, xmax = 1000, 10000
ymin, ymax = -40, 1

ax1.set_xscale('log')
ax1.set_xlim(xmin, xmax)
ax1.set_ylim(ymin, ymax)

ax1.fill_between([xmin, f1], ymin, -10, color='firebrick', alpha=0.25)   # nederst til venstre
ax1.fill_between([f2, xmax], -3, ymax, color='firebrick', alpha=0.25)    # øverst til høyre

ax1.fill_between([xmin, f1], -10, -3, color='firebrick', alpha=0.25)        # midten venstre
ax1.fill_between([f2, xmax], -10, -3, color='firebrick', alpha=0.25)        # midten høyre

ax1.xaxis.set_major_formatter(ScalarFormatter())
#plt.savefig('54_7_2.png', dpi=500)
plt.show()


