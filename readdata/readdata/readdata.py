import os
import sys

def cm2inch(value):
    return value/2.54


path=os.path.abspath('.')
path+='\\result'


###read the resultN
jrN=[]
EnergyN=[]
#i=0
for firstdir in os.listdir(path):
    firstdirname=path+'\\'+firstdir

    if os.path.isdir(firstdirname):
        for seconddir in os.listdir(path+'\\'+firstdir):
            filename=path+'\\'+firstdir+'\\'+seconddir+'\\ResultN'
            #print(filename)
            if os.path.isfile(filename):
                #print(filename)
                with open(filename) as f:
                    datastr=f.read().split()
                    datastr
                    for str in datastr:
                        if str=='Jr=':
                            jrN.append(float(datastr[datastr.index(str)+1]))
                            #print(jr[i])
                            #i+=1
                            #break
                        elif str=='Energy=':
                            EnergyN.append(float(datastr[datastr.index(str)+1]))
                            #print(Energy[i])
                            #i+=1
                            break
jre={}
for i in range(len(jrN)):
    jre[jrN[i]]=EnergyN[i]
EnergyN=[jre[k] for k in sorted(jre.keys())]
jrN.sort()

##read the result P
jrP=[]
EnergyP=[]
for firstdir in os.listdir(path):
    firstdirname=path+'\\'+firstdir
    if os.path.isdir(firstdirname):
        for seconddir in os.listdir(path+'\\'+firstdir):
            filename=path+'\\'+firstdir+'\\'+seconddir+'\\ResultP'
            if os.path.isfile(filename):
                with open(filename) as f:
                    datastr=f.read().split()
                    datastr
                    for str in datastr:
                        if str=='Jr=':
                            jrP.append(float(datastr[datastr.index(str)+1]))
                            #print(jr[i])
                            #i+=1
                            #break
                        elif str=='Energy=':
                            EnergyP.append(float(datastr[datastr.index(str)+1]))
                            #print(Energy[i])
                            #i+=1
                            break
jre={}
for i in range(len(jrP)):
    jre[jrP[i]]=EnergyP[i]
EnergyP=[jre[k] for k in sorted(jre.keys())]
jrP.sort()

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc


##to make the label looks like the latex format.
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
##################################################################

fig=plt.figure(num=1, figsize=(cm2inch(8), cm2inch(6)))

font={'family':'Times New Roman','size':10}

plt.rc('font',**font)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
plt.plot(jrP, EnergyP, linewidth=1, marker='o', markerfacecolor='none', markersize=2, label='P')
plt.plot(jrN, EnergyN, linewidth=1, marker='s', markerfacecolor='none', markersize=2, 
         label='N')
plt.legend(frameon=False,loc=1)
plt.xticks([0, 0.05, 0.1])
#plt.yticks([-20,-10,0])

#plt.ylim((-28, 3))
plt.xlim((0, 0.12))

#rc('text', usetex=True)
plt.xlabel(r"$t$", fontsize=12)
plt.ylabel(r'$E_g$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
plt.tick_params(top=True, right=True, direction='in')

#ax=plt.axes()
#ax.arrow(0.35,-10,-0.1,-50)

ax1=fig.add_axes([0.35,0.35,0.3,0.3])
ax1.plot(jrP, EnergyP, linewidth=1, marker='o', markerfacecolor='none', markersize=2, label='Positive Energy')
ax1.plot(jrN, EnergyN, linewidth=1, marker='s', markerfacecolor='none', markersize=2, 
         label='Negative Energy')

ax1.set_xlim(0,0.06)
ax1.set_ylim(-33.2,-32)
ax1.set_yticks([-33,-32])
ax1.tick_params(top=True, right=True, direction='in')



plt.tight_layout()
plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\grgcr1energy.eps')

plt.show()