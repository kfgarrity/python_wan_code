import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()



h = wan_ham('qe_hr.dat') #load the hamiltonian
nstr = "spgr_164_taas_relaxed"

fermi = 10.6113 # tate4 relaxed
orbital_info = [["S", 2, ["p"]], ["Ta", 1, ["d"]]]

orbs_s = ops.get_orbitals(orbital_info, [["S"]], so=True)
orbs_ta = ops.get_orbitals(orbital_info, [["Ta"]], so=True)


    

#kpoint info for high symmetry lines

#d = {}
#d["A"] = [0.5000000000, 0.5000000000,0.5000000000]
#d["$\Gamma$"] = [0.0000000000, 0.0000000000, 0.0000000000]
#d["M"] = [0.5000000000, 0.5000000000, 0.0000000000]
#d["R"] = [0.0000000000, 0.5000000000, 0.5000000000]
#d["X"] = [0.0000000000, 0.5000000000, 0.0000000000]
#d["Z"] = [0.0000000000, 0.0000000000, 0.5000000000]

d = {}
d["A"] = [	0.0000000000,	0.0000000000,	0.5000000000]
d["A'"] = [	-0.0000000000,	-0.0000000000,	-0.5000000000]
d["$\Gamma$"] = [	0.0000000000,	0.0000000000,	0.0000000000]
d["H"] = [	0.3333333333,	0.3333333333,	0.5000000000]
d["H'"] = [	-0.3333333333,	-0.3333333333,	-0.5000000000]
d["H2"] = [	0.3333333333,	0.3333333333,	-0.5000000000]
d["H2'"] = [	-0.3333333333,	-0.3333333333,	0.5000000000]
d["K"] = [	0.3333333333,	0.3333333333,	0.0000000000]
d["K'"] = [	-0.3333333333,	-0.3333333333,	-0.0000000000]
d["L"] = [	0.5000000000,	0.0000000000,	0.5000000000]
d["L'"] = [	-0.5000000000,	-0.0000000000,	-0.5000000000]
d["M"] = [	0.5000000000,	0.0000000000,	0.0000000000]
d["M'"] = [	-0.5000000000,	-0.0000000000,	-0.0000000000]

names = ["$\Gamma$", "M", "K", "$\Gamma$", "A", "L", "H", "A", "L", "M", "H", "K"]

kpts = []
for n in names:
    kpts.append(d[n])


#plot band structure
#returns eigenvalues, projections, 
vals, projs_ta, name_info = ops.band_struct(h,kpts, proj=orbs_ta, yrange=[-4, 4], names = names,  fermi=fermi, pdfname="band_struct_ta_"+nstr+".pdf")
plt.clf()
vals, projs_s   , name_info = ops.band_struct(h,kpts, proj=orbs_s, yrange=[-4, 4], names = names,  fermi=fermi, pdfname="band_struct_s_"+nstr+".pdf")
plt.clf()


np.savetxt("vals_bandstruct_"+nstr+".csv", vals)
np.savetxt("proj_bandstruct_ta_"+nstr+".csv", projs_ta)
np.savetxt("proj_bandstruct_s_"+nstr+".csv", projs_s)
print("kpoint name_info")
print(name_info)
print()

orbs_ta_dz2 = ops.get_orbitals(orbital_info, [["Ta", "dz2"]], so=True)
orbs_ta_dxz_dyz = ops.get_orbitals(orbital_info, [["Ta", "dxz"], ["Ta", "dyz"]], so=True)
orbs_ta_dx2y2 = ops.get_orbitals(orbital_info, [["Ta", "dx2y2"]], so=True)
orbs_ta_dxy = ops.get_orbitals(orbital_info, [["Ta", "dxy"]], so=True)

orbs_s_pz = ops.get_orbitals(orbital_info, [["S", "pz"]], so=True)
orbs_s_px_py = ops.get_orbitals(orbital_info, [["S", "px"], ["S", "py"]], so=True)
    
#orbs_fe_dz2 = ops.get_orbitals(orbital_info, [["Fe", "dz2"]], so=True)
#orbs_fe_dxz_dyz = ops.get_orbitals(orbital_info, [["Fe", "dxz"], ["Fe", "dyz"]], so=True)
#orbs_fe_dx2y2 = ops.get_orbitals(orbital_info, [["Fe", "dx2y2"]], so=True)
#orbs_fe_dxy = ops.get_orbitals(orbital_info, [["Fe", "dxy"]], so=True)


fnames = ["proj_orbs_ta_dz2_", "proj_orbs_ta_dxz_dyz_", "proj_orbs_ta_dx2y2_", "proj_orbs_ta_dxy_", "proj_orbs_s_pz_", "proj_orbs_s_px_py_" ]


ORBS = [orbs_ta_dz2, orbs_ta_dxz_dyz, orbs_ta_dx2y2, orbs_ta_dxy, orbs_s_pz, orbs_s_px_py]

for n,orbs in zip(fnames, ORBS):

    vals, projs, name_info = ops.band_struct(h,kpts, proj=orbs, yrange=[-4, 4], names = names,  fermi=fermi, pdfname=n+nstr+".pdf")
    plt.clf()

    np.savetxt("vals_"+n+nstr+".csv", vals)
    np.savetxt(n+nstr+".csv", projs)

