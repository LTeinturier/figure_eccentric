import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams['font.size']=24
plt.rcParams['xtick.labelsize']=24
plt.rcParams['ytick.labelsize']=24
plt.rcParams['legend.fontsize']=20
plt.rcParams['figure.figsize']=[16,12]

fig, ax = plt.subplots(1)
# temp = np.loadtxt('profile')
p = np.loadtxt("pressure.dat")
kcl = np.loadtxt("profile_KCl_vap")[1:]
al = np.loadtxt("profile_Al_vap")[1:]
Fe = np.loadtxt("profile_Fe_vap")[1:]
Mg = np.loadtxt("profile_Mg_vap")[1:]
Na = np.loadtxt("profile_Na_vap")[1:]
# ax[0].semilogy(temp,p/100)
ax.loglog(kcl,p/100,label='KCl')
ax.loglog(al,p/100.,label='Al$_{\mathrm{2}}$O$_{\mathrm{3}}$')
ax.loglog(Fe,p/100.,label='Fe')
ax.loglog(Mg,p/100.,label='Mg$_{\mathrm{ 2}}$SiO$_{\mathrm{ 4}}$')

ax.loglog(Na,p/100.,label='Na$_{\mathrm{ 2}}$S')
# for aa in ax:
#     aa.grid()
#     aa.legend()
#     aa.invert_yaxis()

ax.grid()
h,l = ax.get_legend_handles_labels()
leg=fig.legend(h,l,ncol=len(h),loc='lower center',bbox_to_anchor=(0.5,0.88))
ax.invert_yaxis()
ax.set_xlabel("Mass Mixing Ratio [kg.kg$^{-1}$]")
ax.set_ylabel("Pressure [mbar]")
# plt.tight_layout()
plt.savefig("clouds_profiles.pdf",format='pdf',bbox_inches='tight')
# plt.savefig("clouds_profiles.png",format='png',bbox_extra_artists=(leg,),bbox_inches='tight')
# plt.show()