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

elif sys.argv[1] == "nbte4_relaxed":

    h = wan_ham('nbte4_relaxed/qe_hr.dat') #load the hamiltonian
    nstr = "nbte4_relaxed"
    fermi = 11.8691 # nbte4 relaxed
    orbital_info = [["Nb", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Nb"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    
elif sys.argv[1] == "tate4_unrelaxed":

    h = wan_ham('tate4_expt_coords/qe_hr.dat') #load the hamiltonian
    nstr = "nbte4_relaxed"
    fermi = 12.0470 # tate4 unrelaxed
    orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    
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


#plot band structure
#returns eigenvalues, projections, 

ops.num_k  = 10 #faster 
vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-5, 5], names = names,  fermi=fermi, pdfname="band_struct_metal_faster_"+nstr+".pdf")
plt.clf()

np.savetxt("vals_bandstruct_"+nstr+".csv", vals)
np.savetxt("proj_bandstruct_metal_"+nstr+".csv", projs_metal)
print("kpoint name_info")
print(name_info)
print()

energies, dos, pdos_metal, vals_grid, proj_metal_grid = ops.dos(h, [4,4,4], proj=orbs_metal, fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_metal_faster_"+nstr+".pdf")
