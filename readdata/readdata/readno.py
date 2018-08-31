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

#fig=plt.figure(num=2, figsize=(cm2inch(8), cm2inch(5)))

font={'family':'Times New Roman','size':10}

plt.rc('font',**font)



#=======to make the subplots adjust==========
fig,axs=plt.subplots(2,1,sharex=True,figsize=(cm2inch(8), cm2inch(8)))

fig.subplots_adjust(left=0.2,bottom=0.15,hspace=0)

###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
axs[0].plot(ParticleN[0:-1:2,0], ParticleN[0:-1:2,1], '--r',linewidth=0.5,marker='o', 
         markerfacecolor='none', markersize=2, label='N')
axs[0].plot(ParticleP[1:-1:2,0], ParticleP[1:-1:2,1], '--b',linewidth=0.5,marker='s',
         markerfacecolor='none', markersize=2, label='P')
axs[0].legend(frameon=False,loc=3)

#axs[0].set_xticks([0,0.5,1])
axs[0].set_yticks([0.00,2.00, 4.00])

axs[0].set_ylim((0, 4))
#plt.xlim((0, 1))

#plt.xlabel(r"$t$", fontsize=12)
axs[0].set_ylabel(r'$\langle a^\dag a\rangle$', fontsize=12)
axs[0].text(0.05,3,'(a)',fontsize=12)
axs[0].yaxis.set_label_coords(-0.15,0.5)







##set the ticks. See the doc in class plt.tick_params
axs[0].tick_params(top=True, right=True, direction='in')

#plt.tight_layout()
#plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\AParticle.eps')

#plt.figure(figsize=(12,9))

#plt.show()




#######show the SigmaParticle###################


#plt.figure(num=3, figsize=(cm2inch(8), cm2inch(6)))

#font={'family':'Times New Roman','size':10}

#plt.rc('font',**font)

#ax=plt.subplot(1,2,2)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
axs[1].plot(ParticleN[0:-1:2,0], ParticleN[0:-1:2,2], '--r',linewidth=0.5,marker='o',
         markerfacecolor='none', markersize=2, label='N')
axs[1].plot(ParticleP[1:-1:2,0], ParticleP[1:-1:2,2], '--b',linewidth=0.5,marker='s',
         markerfacecolor='none', markersize=2, label='P')
axs[1].legend(frameon=False,loc=3)

#plt.xticks([0,0.5,1])
axs[1].set_yticks([0,0.05, 0.1])

axs[1].set_ylim((0, 0.12))
#plt.xlim((0, 1))
axs[1].set_ylabel(r'$\langle \sigma^+ \sigma^-\rangle$', fontsize=12)





axs[1].set_xlabel(r"$t$", fontsize=12)
axs[1].text(0.05,0.09,'(b)',fontsize=12)

#ax.yaxis.set_label_position('right')
#ax.yaxis.tick_right()
##set the ticks. See the doc in class plt.tick_params
plt.tick_params(top=True, right=True, direction='in')

#fig.tight_layout()
fig.savefig('D:\\books\\articles\\ARH\\2018_08_22\grgcr1Particle.eps')

#plt.figure(figsize=(12,9))

plt.show()