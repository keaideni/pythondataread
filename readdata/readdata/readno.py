import os
import sys

def cm2inch(value):
    return value/2.54


path=os.path.abspath('.')
path+='\\result'


###read the resultN
jrN=[]
AParticleNoN=[]
SigmaParticleNoN=[]
#i=0
for firstdir in os.listdir(path):
    firstdirname=path+'\\'+firstdir
    if os.path.isdir(firstdirname):
        for seconddir in os.listdir(path+'\\'+firstdir):
            filename=path+'\\'+firstdir+'\\'+seconddir+'\\ResultN'
            if os.path.isfile(filename):
                with open(filename) as f:
                    datastr=f.read().split()
                    datastr
                    for str in datastr:
                        if str=='Jr=':
                            jrN.append(float(datastr[datastr.index(str)+1]))
                            #print(jr[i])
                            #i+=1
                            #break
                        elif str=='AParticleNo=':
                            AParticleNoN.append(float(datastr[datastr.index(str)+1]))
                        elif str=='SigmaParticleNo=':
                            SigmaParticleNoN.append(float(datastr[datastr.index(str)+1]))
                            #print(Energy[i])
                            #i+=1
                            break


##read the result P
jrP=[]
AParticleNoP=[]
SigmaParticleNoP=[]
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
                        elif str=='AParticleNo=':
                            AParticleNoP.append(float(datastr[datastr.index(str)+1]))
                        elif str=='SigmaParticleNo=':
                            SigmaParticleNoP.append(float(datastr[datastr.index(str)+1]))
                            #print(Energy[i])
                            #i+=1
                            break


###### use lexsort to sort the data by jr.
import numpy as np
indN=np.lexsort((SigmaParticleNoN, AParticleNoN, jrN))
ParticleN=np.array([(jrN[k], AParticleNoN[k], SigmaParticleNoN[k]) for k in indN])

indP=np.lexsort((SigmaParticleNoP, AParticleNoP, jrP))
ParticleP=np.array([(jrP[k], AParticleNoP[k], SigmaParticleNoP[k]) for k in indP])



import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc


##to make the label looks like the latex format.
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
#############show AParticle#################################

plt.figure(num=2, figsize=(cm2inch(8), cm2inch(6)))

font={'family':'Times New Roman','size':10}

plt.rc('font',**font)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
plt.plot(ParticleN[0:-1:2,0], ParticleN[0:-1:2,1], '--r',linewidth=0.5,marker='o', markerfacecolor='none', markersize=2)
plt.plot(ParticleP[1:-1:2,0], ParticleP[1:-1:2,1], '--b',linewidth=0.5,marker='s', markerfacecolor='none', markersize=2)

plt.xticks([0,0.5,1])
plt.yticks([0,2, 4])

plt.ylim((0, 4))
plt.xlim((0, 1))

plt.xlabel(r"$t$", fontsize=12)
plt.ylabel(r'$\langle a^\dag a\rangle$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
plt.tick_params(top=True, right=True, direction='in')

plt.tight_layout()
plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\AParticle.eps')

#plt.figure(figsize=(12,9))

#plt.show()




#######show the SigmaParticle###################


plt.figure(num=3, figsize=(cm2inch(8), cm2inch(6)))

font={'family':'Times New Roman','size':10}

plt.rc('font',**font)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
plt.plot(ParticleN[0:-1:2,0], ParticleN[0:-1:2,2], '--r',linewidth=0.5,marker='o', markerfacecolor='none', markersize=2)
plt.plot(ParticleP[1:-1:2,0], ParticleP[1:-1:2,2], '--b',linewidth=0.5,marker='s', markerfacecolor='none', markersize=2)

plt.xticks([0,0.5,1])
plt.yticks([0,0.05, 0.1])

plt.ylim((0, 0.1))
plt.xlim((0, 1))

plt.xlabel(r"$t$", fontsize=12)
plt.ylabel(r'$\langle a^\dag a\rangle$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
plt.tick_params(top=True, right=True, direction='in')

plt.tight_layout()
plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\SigmaParticle.eps')

#plt.figure(figsize=(12,9))

plt.show()