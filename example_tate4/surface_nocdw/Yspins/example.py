import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()




h = wan_ham('../Xspins/qe_hr.dat') #load the hamiltonian
nstr = "center"
fermi = 11.9464
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
d["A"] =        [ 0.5000000000, 0.5000000000, 0.5000000000]
d["$\Gamma$"] = [ 0.0000000000, 0.0000000000, 0.0000000000]
d["M"] =        [ 0.5000000000, 0.0000000000, 0.5000000000]
d["R"] =        [ 0.5000000000, 0.5000000000, 0.0000000000]
d["X"] =        [ 0.5000000000, 0.0000000000, 0.0000000000]
d["Z"] =        [ 0.0000000000, 0.5000000000, 0.0000000000]

names = ["$\Gamma$", "X", "M", "$\Gamma$", "Z", "R", "A", "Z", "X", "R", "M", "A"]

kpts = []
for n in names:
    kpts.append(d[n])


#plot band structure
#returns eigenvalues, projections, 
#vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-3, 3], names = names,  fermi=fermi, pdfname="band_structYdir.pdf")
#vals, projs_metal, name_info = ops.band_struct(h,kpts, yrange=[-3, 3], names = names,  fermi=fermi, pdfname="band_struct_noprojYdir.pdf")

supercell = [1,1,6] #10 septuple layers                                                                                                                                                                                                                
hsurf = ops.generate_supercell(h, supercell, cut=[0,0,1], sparse=False)


ds = {}
#ds["A"] = [0.5000000000, 0.5000000000,0.5000000000]
#ds["M"] = [0.5000000000, 0.5000000000, 0.0000000000]

ds["X"] =        [0.5000000000, 0.0000000000, 0.0000000000]
ds["R"] =        [0.5000000000, 0.5000000000, 0.0000000000]
ds["$\Gamma$"] = [0.0000000000, 0.0000000000, 0.0000000000]
ds["Z"] =        [0.0000000000, 0.5000000000, 0.0000000000]

names = ["$\Gamma$", "X", "R", "$\Gamma$", "Z", "R"]

kpts = []
for n in names:
    kpts.append(ds[n])

#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, yrange=[-3, 3], names = names,  fermi=fermi, pdfname="surf_band_struct_noprojYdir.pdf")


proj_surf = []
for i in range(68):
    proj_surf.append(i)
    proj_surf.append(i+340)

proj_surf_spin = []
for i in range(1, 68, 2):
    proj_surf_spin.append(i)
    proj_surf_spin.append(i+340-1)
    

vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-3, 3], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_spin2Ydir.pdf")

ds2 = {}
#ds["A"] = [0.5000000000, 0.5000000000,0.5000000000]
#ds["M"] = [0.5000000000, 0.5000000000, 0.0000000000]

ds2["X"] =        [ 0.5000000000,  0.0000000000  , 0.0000000000]
ds2["-X"] =       [-0.5000000000,  0.0000000000  , 0.0000000000]
ds2["R"] =        [ 0.5000000000,  0.5000000000  , 0.0000000000]
ds2["-R"] =       [-0.5000000000,  -0.5000000000 , 0.0000000000]
ds2["$\Gamma$"] = [ 0.0000000000,  0.0000000000  , 0.0000000000]
ds2["Z"] =        [ 0.0000000000,  0.5000000000  , 0.0000000000]
ds2["-Z"] =       [ 0.0000000000,  -0.5000000000 , 0.0000000000]

ds2["oR"] =        [ 0.5000000000,  -0.5000000000  , 0.0000000000]
ds2["-oR"] =       [0.5000000000,  -0.5000000000 , 0.0000000000]

names = ["-X", "$\Gamma$", "X"]

kpts = []
for n in names:
    kpts.append(ds2[n])

#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-2, 1], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_XYdir.pdf")

names = ["-Z", "$\Gamma$", "Z"]

kpts = []
for n in names:
    kpts.append(ds2[n])

#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-2, 1], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_ZYdir.pdf")


names = ["-R", "$\Gamma$", "R"]

kpts = []
for n in names:
    kpts.append(ds2[n])

#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-2, 1], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_RYdir.pdf")

names = ["X", "R", "Z"]

kpts = []
for n in names:
    kpts.append(ds2[n])

#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-2, 1], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_XRZYdir.pdf")

names = ["-oR", "$\Gamma$", "oR"]

kpts = []
for n in names:
    kpts.append(ds2[n])
#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-2, 1], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_oRYdir.pdf")

names = ["X", "oR", "Z"]

kpts = []
for n in names:
    kpts.append(ds2[n])

#vals, projs_metal, name_info = ops.band_struct(hsurf,kpts, proj=proj_surf_spin, yrange=[-2, 1], names = names,  fermi=fermi, pdfname="surf_band_struct_projsurf_XoRZYdir.pdf")
