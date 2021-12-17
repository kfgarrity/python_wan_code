import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()



if len(sys.argv) == 1:

    print("You must run the code with one argument. ", sys.argv)
    print("The possible arguments are: tate4_relaxed nbte4_relaxed tate4_unrelaxed")
    print("for example")
    print("python example.py tate4_relaxed")
    print("goodbye")
    print()
    exit()
    
elif sys.argv[1] == "tate4_relaxed":

    h = wan_ham('tate4_relaxed/qe_hr.dat') #load the hamiltonian
    nstr = "tate4_relaxed"
    fermi = 11.9540 # tate4 relaxed
    orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    metal = "Ta"
    
elif sys.argv[1] == "nbte4_relaxed":

    h = wan_ham('nbte4_relaxed/qe_hr.dat') #load the hamiltonian
    nstr = "nbte4_relaxed"
    fermi = 11.8691 # nbte4 relaxed
    orbital_info = [["Nb", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Nb"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    metal = "Nb"
    
elif sys.argv[1] == "tate4_unrelaxed":

    h = wan_ham('tate4_expt_coords/qe_hr.dat') #load the hamiltonian
    nstr = "nbte4_relaxed"
    fermi = 12.0470 # tate4 unrelaxed
    orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    metal = "Ta"
    
else:
    print("wrong choice ", sys.argv)
    print("correct choices are tate4_relaxed nbte4_relaxed tate4_unrelaxed")
    print("goodbye")
    print()
    exit()

    

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

h.trim(val=1e-4)
    
orbs_metal_dz2 = ops.get_orbitals(orbital_info, [[metal, "dz2"]], so=True)
orbs_metal_dxz_dyz = ops.get_orbitals(orbital_info, [[metal, "dxz"], [metal, "dyz"]], so=True)
orbs_metal_dx2y2 = ops.get_orbitals(orbital_info, [[metal, "dx2y2"]], so=True)
orbs_metal_dxy = ops.get_orbitals(orbital_info, [[metal, "dxy"]], so=True)

orbs_te_pz = ops.get_orbitals(orbital_info, [["Te", "pz"]], so=True)
orbs_te_px_py = ops.get_orbitals(orbital_info, [["Te", "px"], ["Te", "py"]], so=True)
    

fnames = ["proj_orbs_dz2_", "proj_orbs_dxz_dyz_", "proj_orbs_dx2y2_", "proj_orbs_dxy_", "proj_orbs_pz_", "proj_orbs_px_py_" ]
ORBS = [orbs_metal_dz2, orbs_metal_dxz_dyz, orbs_metal_dx2y2, orbs_metal_dxy, orbs_te_pz, orbs_te_px_py]

for n,orbs in zip(fnames, ORBS):

    vals, projs, name_info = ops.band_struct(h,kpts, proj=orbs, yrange=[-4, 4], names = names,  fermi=fermi, pdfname=n+nstr+".pdf")
    plt.clf()

    np.savetxt("vals_"+n+nstr+".csv", vals)
    np.savetxt(n+nstr+".csv", projs)

