import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()




h = wan_ham('qe_hr.dat') #load the hamiltonian
nstr = "center"
fermi = 11.9461
orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)


    
#         R     X     R
#    
#
#         Z     G     Z
#
#
#         R     X     R






#         A     M     A
#    
#
#         R     X     R
#
#
#         A     M     A




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
#vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-3, 3], names = names,  fermi=fermi, pdfname="band_struct.pdf")
#vals, projs_metal, name_info = ops.band_struct(h,kpts, yrange=[-3, 3], names = names,  fermi=fermi, pdfname="band_struct_noproj.pdf")


#vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=range(0, h.nwan,2), yrange=[-2, 2], names = names,  fermi=fermi, pdfname="band_struct_up.pdf")

#vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=range(1, h.nwan,2), yrange=[-2, 2], names = names,  fermi=fermi, pdfname="band_struct_dn.pdf")

h.num_k=200

vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=range(0, h.nwan,2), yrange=[-0.4, 0.4], names = names,  fermi=fermi, pdfname="band_struct_up_zoom.pdf")

vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=range(1, h.nwan,2), yrange=[-0.4, 0.4], names = names,  fermi=fermi, pdfname="band_struct_dn_zoom.pdf")

