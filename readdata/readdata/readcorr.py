import os
import sys
import numpy as np


def cm2inch(value):
    return value/2.54


path=os.path.abspath('.')
path+='\\result'


###read the resultN


#########read the file Correlation P/N##########

#### to create the R size label############
Rname=path+'\\result_1\\1\\CorrelationP'
R=[]
with open(Rname) as f:
    datastr=f.read().split()
    for i in range(len(datastr)):
        if datastr[i]=='R=':
            R.append(float(datastr[i+1]))

corrp=np.array(R)
sigmacorrp=np.array(R)

Rname=path+'\\result_1\\1\\CorrelationN'
R=[]
with open(Rname) as f:
    datastr=f.read().split()
    for i in range(len(datastr)):
        if datastr[i]=='R=':
            R.append(float(datastr[i+1]))

corrn=np.array(R)
sigmacorrn=np.array(R)


jrN=[-1]
for firstdir in os.listdir(path):
    firstdirname=path+'\\'+firstdir
    if os.path.isdir(firstdirname):
        for seconddir in os.listdir(path+'\\'+firstdir):
            filename=path+'\\'+firstdir+'\\'+seconddir+'\\ResultN'
            if os.path.isfile(filename):
                with open(filename) as f:
                    datastr=f.read().split()
                    #datastr
                    for str in datastr:
                        if str=='Jr=':
                            jrN.append(float(datastr[datastr.index(str)+1]))
                            break


            ####for correlation N###########
            filenamecorr=path+'\\'+firstdir+'\\'+seconddir+'\\CorrelationN'
            if os.path.isfile(filenamecorr):
                corrdata=[]
                with open(filenamecorr) as f:
                    datastr=f.read().split()
                    for i in range(len(datastr)):
                        if datastr[i]==',Corr(R)=':
                            corrdata.append(float(datastr[i+1]))
                corrn=np.c_[corrn, [cell/corrdata[0] for cell in corrdata]]





            ####for SigmaCorrelationN#######
            filenamecorr=path+'\\'+firstdir+'\\'+seconddir+'\\SigmaCorrelationN'
            if os.path.isfile(filenamecorr):
                corrdata=[]
                with open(filenamecorr) as f:
                    datastr=f.read().split()
                    for i in range(len(datastr)):
                        if datastr[i]==',Corr(R)=':
                            corrdata.append(float(datastr[i+1]))
                sigmacorrn=np.c_[sigmacorrn, [cell/corrdata[0] for cell in corrdata]]


jrP=[-1]
for firstdir in os.listdir(path):
    firstdirname=path+'\\'+firstdir
    if os.path.isdir(firstdirname):
        for seconddir in os.listdir(path+'\\'+firstdir):
            filename=path+'\\'+firstdir+'\\'+seconddir+'\\ResultP'
            if os.path.isfile(filename):
                with open(filename) as f:
                    datastr=f.read().split()
                    #datastr
                    for str in datastr:
                        if str=='Jr=':
                            jrP.append(float(datastr[datastr.index(str)+1]))
                            break
            ##for correlation P###########
            filenamecorr=path+'\\'+firstdir+'\\'+seconddir+'\\CorrelationP'
            if os.path.isfile(filenamecorr):
                corrdata=[]
                with open(filenamecorr) as f:
                    datastr=f.read().split()
                    for i in range(len(datastr)):
                        if datastr[i]==',Corr(R)=':
                            corrdata.append(float(datastr[i+1]))
                corrp=np.c_[corrp, [cell/corrdata[0] for cell in corrdata]]

           


            ####for SigmaCorrelationP#######
            filenamecorr=path+'\\'+firstdir+'\\'+seconddir+'\\SigmaCorrelationP'
            if os.path.isfile(filenamecorr):
                corrdata=[]
                with open(filenamecorr) as f:
                    datastr=f.read().split()
                    for i in range(len(datastr)):
                        if datastr[i]==',Corr(R)=':
                            corrdata.append(float(datastr[i+1]))
                sigmacorrp=np.c_[sigmacorrp, [cell/corrdata[0] for cell in corrdata]]



           
ajrP=np.array(jrP).reshape(1,len(jrP))
ajrN=np.array(jrN).reshape(1,len(jrN))
corrp=np.r_[ajrP, corrp]
corrn=np.r_[ajrN, corrn]
sigmacorrp=np.r_[ajrP, sigmacorrp]
sigmacorrn=np.r_[ajrN, sigmacorrn]


#####sort the matrix by jr values###############
fcorrp=corrp[:,corrp[0,:].argsort()]
fcorrn=corrn[:,corrn[0,:].argsort()]
fsigmacorrp=sigmacorrp[:,sigmacorrp[0,:].argsort()]
fsigmacorrn=corrn[:,corrn[0,:].argsort()]


###### use lexsort to sort the data by jr.
#indN=np.lexsort((SigmaParticleNoN, AParticleNoN, jrN))
#ParticleN=np.array([(jrN[k], AParticleNoN[k], SigmaParticleNoN[k]) for k in indN])

#indP=np.lexsort((SigmaParticleNoP, AParticleNoP, jrP))
#ParticleP=np.array([(jrP[k], AParticleNoP[k], SigmaParticleNoP[k]) for k in indP])



import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc


##to make the label looks like the latex format.
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
#############show AParticle#################################

#plt.figure(num=1, figsize=(cm2inch(8), cm2inch(6)))


font={'family':'Times New Roman','size':10}

plt.rc('font',**font)



fig, axs=plt.subplots(2,2,sharex=True, sharey=True, figsize=(cm2inch(8), cm2inch(6)))
fig.subplots_adjust(bottom=0.18,left=0.18,hspace=0.12,wspace=0.12)

###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
for i in range(1,len(fcorrp[1,:])):
    axs[1,0].plot(fsigmacorrp[:,0], fsigmacorrp[:,i], linewidth=0.5, markerfacecolor='none'
             , markersize=2 )

axs[1,0].set_xticks([0,10,20])
axs[1,0].set_yticks([0,0.5, 1])

axs[1,0].set_ylim((0, 1.1))
axs[1,0].set_xlim((0, 20))

axs[1,0].set_xlabel(r"$R$", fontsize=12)
axs[1,0].set_ylabel(r'$\langle \sigma_0^+ \sigma_R\rangle$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
axs[1,0].tick_params(top=True, right=True, direction='in')






#plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\Corrp.eps')




#######show the SigmaParticle###################


#plt.figure(num=2, figsize=(cm2inch(8), cm2inch(6)))

#font={'family':'Times New Roman','size':10}

#plt.rc('font',**font)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
for i in range(1,len(fcorrp[1,:])):
    axs[0,0].plot(fcorrp[:,0], fcorrp[:,i], linewidth=0.5, markerfacecolor='none'
             , markersize=2 )
axs[0,0].set_xticks([0,10,20])
axs[0,0].set_yticks([0,0.5, 1])

axs[0,0].set_ylim((0, 1.1))
axs[0,0].set_xlim((0, 20))

#axs[0,0].set_xlabel(r"$R$", fontsize=12)
axs[0,0].set_ylabel(r'$\langle a_0^\dag a_R\rangle$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
axs[0,0].tick_params(top=True, right=True, direction='in')

#plt.tight_layout()

#plt.tight_layout()
#plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\SigmaCorrp.eps')

#plt.show()


#plt.figure(num=3, figsize=(cm2inch(8), cm2inch(6)))

#font={'family':'Times New Roman','size':10}

#plt.rc('font',**font)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
for i in range(1,len(fcorrp[1,:])):
    axs[0,1].plot(fcorrn[:,0], fcorrn[:,i], linewidth=0.5, markerfacecolor='none'
             , markersize=2 )



axs[0,1].set_xticks([0,10,20])
axs[0,1].set_yticks([0,0.5, 1])

axs[0,1].set_ylim((0, 1.1))
axs[0,1].set_xlim((0, 20))

#axs[0,1].set_xlabel(r"$R$", fontsize=12)
#axs[0,1].set_ylabel(r'$\langle a_0^\dag a_R\rangle$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
axs[0,1].tick_params(top=True, right=True, direction='in')

#plt.tight_layout()
#plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\Corrn.eps')




#######show the SigmaParticle###################


#plt.figure(num=4, figsize=(cm2inch(8), cm2inch(6)))

#font={'family':'Times New Roman','size':10}

#plt.rc('font',**font)


###c is the parameter to control the center of marker. Empty means no center.
###this is for scatter

##for plot, we use markerfacecolor
for i in range(1,len(fcorrp[1,:])):
    axs[1,1].plot(fsigmacorrn[:,0], fsigmacorrn[:,i], linewidth=0.5, markerfacecolor='none'
             , markersize=2 )

axs[1,1].set_xticks([0,10,20])
axs[1,1].set_yticks([0,0.5, 1])

axs[1,1].set_ylim((0, 1.1))
axs[1,1].set_xlim((0, 20))

axs[1,1].set_xlabel(r"$R$", fontsize=12)
#axs[1,1].set_ylabel(r'$\langle \sigma_0^+ \sigma_R\rangle$', fontsize=12)

##set the ticks. See the doc in class plt.tick_params
axs[1,1].tick_params(top=True, right=True, direction='in')

#plt.tight_layout()
axs[0,0].text(15,0.7,'(a)', fontsize=12)
axs[1,0].text(15,0.7,'(b)', fontsize=12)
axs[0,1].text(15,0.7,'(c)', fontsize=12)
axs[1,1].text(15,0.7,'(d)', fontsize=12)
plt.savefig('D:\\books\\articles\\ARH\\2018_08_22\grgcr1Corr.eps')

plt.show()