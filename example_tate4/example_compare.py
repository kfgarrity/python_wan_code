import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()



h = wan_ham('tate4_relaxed/qe_hr.dat') #load the hamiltonian
nstr = "tate4_relaxed"
fermi = 11.9540 # tate4 relaxed
orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)


    

    

#kpoint info for high symmetry lines

d = {}
d["A"] = [0.5000000000, 0.5000000000,0.5000000000]
d["$\Gamma$"] = [0.0000000000, 0.0000000000, 0.0000000000]
d["M"] = [0.5000000000, 0.5000000000, 0.0000000000]
d["R"] = [0.0000000000, 0.5000000000, 0.5000000000]
d["X"] = [0.0000000000, 0.5000000000, 0.0000000000]
d["Z"] = [0.0000000000, 0.0000000000, 0.5000000000]

names = ["$\Gamma$", "X", "M", "$\Gamma$", "Z", "R", "A", "Z", "X", "R", "M", "A"]

kpts = []
for n in names:
    kpts.append(d[n])


#plot band structure
#returns eigenvalues, projections, 
vals_U0, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-5, 5], names = names,  fermi=fermi)


h = wan_ham('tate4_relaxed_U3/qe_hr.dat') #load the hamiltonian
nstr = "tate4_relaxed_U3"
fermi = 12.0871 # tate4 unrelaxed
orbital_info = [["Te", 8, ["p"]], ["Ta", 2, ["d"]] ] #ta case    
orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
metal = "Ta"

vals_U3, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-5, 5], names = names,  fermi=fermi)

plt.clf()
plt.plot(vals_U0[:,0], color="blue", label="U=0 eV")
plt.plot(vals_U0[:,1:], color="blue")
plt.plot(vals_U3[:,0], color="orange",label="U=3 eV")
plt.plot(vals_U3[:,1:], color="orange")
plt.legend(loc="upper right")
plt.ylim(-2,2)
plt.savefig("bs_compare_U0_U3.pdf")

