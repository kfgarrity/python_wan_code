import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

import matplotlib.pyplot as plt 
import os
from os.path import exists


#This code does surface Chern number calculations starting from the
#mbt bulk afm structure We do an even number of layers, and we also
#delete the top and bottom layer to create two odd layer calculations.

#The even calculation should have C=0, the odd ones should be C = +/- 1


#SOC
if not exists("bmt_afm_hr.dat"):
    print("unzipping the hr file, only do this once")
    os.system("gunzip bmt_afm_hr.dat.gz")

fermi = 10.5203
nocc = 6*8 + 2*5  #number of occupied wannier functions 
    

h_soc = wan_ham('bmt_afm_hr.dat')
h_soc.trim() #slightly faster

ops = ham_ops()


#must be in same order as .win file, I use Fe for Mn spin down
orbital_info = [["Bi", 4, ["p"]], ["Te", 8, ["p"]], ["Mn", 1, ["d"]], ["Fe", 1, ["d"]]]

#for figuring out which atom goes with which septuple layer
atoms_frac_str = """
Mn  0.0 0.0 0.25
Bi  0.304627206 0.847686397 0.3857312545
Bi  0.695372794 0.152313603 0.1142687455
Te  0.465534406 0.267232797 0.4503934315
Te  0.534465594 0.732767203 0.0496065685
Te  0.820541764 0.589729117 0.192351675
Te  0.179458356 0.410270823 0.30764828
Fe  0.0 0.0 0.75
Bi  0.304627206 0.847686397 0.8857312545
Bi  0.695372794 0.152313603 0.6142687455
Te  0.465534406 0.267232797 0.9503934315
Te  0.534465594 0.732767203 0.5496065685
Te  0.820541764 0.589729117 0.692351675
Te  0.179458356 0.410270823 0.80764828
"""


top_inds, bot_inds = ops.figure_out_layers(atoms_frac_str, orbital_info, direction="z", cut=0.5, so=True)

#surface, keep all layers
supercell = [1,1,5] #10 septuple layers
hsurf = ops.generate_supercell(h_soc, supercell, cut=[0,0,1], sparse=False)


#first surface, delete 1 layer
hsurf_del1 = ops.delete_orbitals(hsurf, bot_inds)

#other surface, we delete atoms on the other side, which are the top atoms plus the thickness of the cell
top_inds_surf = np.array(top_inds)+h_soc.nwan * (np.prod(supercell) - 1)
hsurf_del2 = ops.delete_orbitals(hsurf, top_inds_surf)


#surface band structure

nk1 = 15 #number of surface kpoints
nk2 = 15

dir1=[1.0,0.0,0.0]  #xy plane
dir2=[0.0,1.0,0.0]

nocc_surf = nocc * np.prod(supercell)
nocc_surf_del = nocc * np.prod(supercell) - nocc//2   #fewer atoms because we deleted half a layer


cnum, direct_gap, indirect_gap =  ops.chern_number(hsurf,nocc, dir1,dir2, nk1, nk2)
print("CHERN even numberlayers ", cnum, " directgap ", direct_gap, " indirect_gap ", indirect_gap)

cnumD1, direct_gapD1, indirect_gapD1 =  ops.chern_number(hsurf_del1,nocc_surf_del, dir1,dir2, nk1, nk2)
print("CHERN delete layer surf1 ", cnumD1, " directgap ", direct_gapD1, " indirect_gap ", indirect_gapD1)

cnumD2, direct_gapD2, indirect_gapD2 =  ops.chern_number(hsurf_del2,nocc_surf_del, dir1,dir2, nk1, nk2)
print("CHERN delete layer surf2 ", cnumD2, " directgap ", direct_gapD2, " indirect_gap ", indirect_gapD2)


print()
print("done")




