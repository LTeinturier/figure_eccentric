import numpy as np
import matplotlib.pyplot as plt 
import h5py 
from dataclasses import dataclass
plt.rcParams['font.size']=24
plt.rcParams['xtick.labelsize']=24
plt.rcParams['ytick.labelsize']=24
plt.rcParams['legend.fontsize']=20
plt.rcParams['figure.figsize']=[16,12]

# class GetAttr:
#     def __getitem_(cls,x):
#         return getattr(cls,x)
@dataclass
class Simulation():
    file: str 
    temp : np.array = np.zeros(1)
    p : np.array = np.zeros(1)
    # Kzz: np.array = np.zeros(1)
    CH4: np.array = np.zeros(1)
    NH3: np.array = np.zeros(1)
    CO: np.array = np.zeros(1)
    CO2: np.array = np.zeros(1)
    FeH: np.array = np.zeros(1)
    H2O: np.array = np.zeros(1)
    H2S: np.array = np.zeros(1)
    HCN: np.array = np.zeros(1)
    K: np.array = np.zeros(1)
    Na: np.array = np.zeros(1)
    PH3: np.array = np.zeros(1)
    TiO: np.array = np.zeros(1)
    VO: np.array = np.zeros(1)
    
    def set(self):
        data = h5py.File(self.file,'r')
        self.temp = data['outputs']['layers']['temperature'][...]
        self.p = data['outputs']['layers']['pressure'][...]
        # self.Kzz = data['outputs']['layers']['eddy_diffusion_coefficient'][...]
        self.CH4 = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['CH4'][...]
        self.NH3 = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['NH3'][...]
        self.CO = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['CO'][...]
        self.CO2 = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['CO2'][...]
        self.FeH = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['FeH'][...]
        self.H2O = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['H2O'][...]
        self.H2S = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['H2S'][...]
        self.HCN = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['HCN'][...]
        self.K = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['K'][...]
        self.Na = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['Na'][...]
        self.PH3 = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['PH3'][...]
        self.TiO = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['TiO'][...]
        self.VO = data['outputs']['layers']['volume_mixing_ratios']['absorbers']['VO'][...]
        
    def __getitem__(self,key):
        if key =='CH4':
            return self.CH4
        elif key =='CO':
            return self.CO
        elif key =='CO2':
            return self.CO2
        elif key =='FeH':
            return self.FeH
        elif key =='H2O':
            return self.H2O
        elif key =='H2S':
            return self.H2S
        elif key =='HCN':
            return self.HCN
        elif key =='K':
            return self.K
        elif key =='Na':
            return self.Na
        elif key =='NH3':
            return self.NH3
        elif key =='PH3':
            return self.PH3
        elif key =='TiO':
            return self.TiO
        elif key =='VO':
            return self.VO
        elif key =='temp':
            return self.temp
        elif key =='p':
            return self.p
            
        else:
            raise KeyError("{} doesn't exist".format(key))

        
def plotter(filelist):
    colors = {
    'CH4': 'C7',
    'CO': 'C3',
    'CO2': 'C5',
    'FeH': 'C4',
    'H2O': 'C0',
    'H2S': 'olive',
    'HCN': 'darkblue',
    'K': 'C8',
    'Na': 'gold',
    'NH3': 'C9',
    'PH3': 'C1',
    'TiO': 'C2',
    'VO': 'darkgreen',
    }
    fig,ax = plt.subplots(1,2)
    plt.subplots_adjust(wspace=0.)
    linestyle = ['-','--',':']
    for ii, ff in enumerate(filelist):
        simu= Simulation(ff)
        simu.set()
        for sp in colors.keys():
            ax[0].loglog(simu[sp],simu.p/100.,linestyle=linestyle[ii],color=colors[sp],label = sp)
        name = simu.file.split("/")[2]
        if name=='refcase':
            name = "e = 0.52"
        else:
            name = name.replace("e","e = ")
        ax[1].semilogy(simu.temp,simu.p/100,color='black',linestyle=linestyle[ii],label=name)
    ax[-1].invert_yaxis()
    ax[0].invert_yaxis()
    ax[0].set_xlim(1.e-12,1.e-2)
    h1,l1 = ax[0].get_legend_handles_labels()
    # ax[0].legend(h[:13],l[:13],loc='upper right')
    # ax[0].legend(h[:13],l[:13],ncol = 4,loc='lower center',bbox_to_anchor=(0.5,0.9))
    h2,l2 = ax[1].get_legend_handles_labels()
    # fig.legend(h,l,ncol=len(h),loc='lower center',bbox_to_anchor=(0.5,0.9))
    # ax[1].legend(h,l,ncol=len(h),loc='lower center',bbox_to_anchor=(0.5,0.9))
    h = h1[:13]+h2
    l = l1[:13]+l2
    print(l)
    fig.legend(h,l,ncol=len(h)//4,loc='lower center',bbox_to_anchor=(0.5,0.88))
    ax[0].set_xlabel("Volume Mixing Ratio")
    ax[0].set_ylabel("Pressure [mbar]")
    ax[1].set_xlabel("Temperature [K]")
    ax[-1].set_yticks([])
    ax[-1].set_yticklabels([])
    plt.savefig("exorem_profiles.pdf",format='pdf',bbox_inches='tight')
    plt.show()
        
def main():
    flist = ['../exorem/e0/eccentric0_apo.h5',
             '../exorem/e25/eccentric025_apo.h5',
             '../exorem/refcase/HATP2_apo.h5'
             ]
    plotter(flist)
    
if __name__ == "__main__":
    main()
    
    