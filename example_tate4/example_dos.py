import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()


#h = wan_ham('tate4_relaxed/qe_hr.dat') #load the hamiltonian
#nstr = "tate4_relaxed"
#fermi = 11.9540 # tate4 relaxed
#orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
#orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
#orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)

h = wan_ham('tate4_relaxed_U1/qe_hr.dat') #load the hamiltonian
nstr = "tate4_relaxed_U1"
fermi = 11.9964 # tate4 unrelaxed
orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
metal = "Ta"



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

elif sys.argv[1] == "tate4_relaxed_U1":

    h = wan_ham('tate4_relaxed_U1/qe_hr.dat') #load the hamiltonian
    nstr = "tate4_relaxed_U1"
    fermi = 11.9964 # tate4 unrelaxed
    orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    metal = "Ta"

elif sys.argv[1] == "tate4_relaxed_U2":

    h = wan_ham('tate4_relaxed_U2/qe_hr.dat') #load the hamiltonian
    nstr = "tate4_relaxed_U2"
    fermi = 12.0410 # tate4 unrelaxed
    orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    metal = "Ta"

elif sys.argv[1] == "tate4_relaxed_U3":

    h = wan_ham('tate4_relaxed_U3/qe_hr.dat') #load the hamiltonian
    nstr = "tate4_relaxed_U3"
    fermi = 12.0871 # tate4 unrelaxed
    orbital_info = [["Te", 8, ["p"]], ["Ta", 2, ["d"]] ] #ta case    
    orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
    orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
    metal = "Ta"
    
elif sys.argv[1] == "nod":

    h = wan_ham('nod/qe_hr.dat') #load the hamiltonian
    nstr = "tate4_NOD"
    fermi = 8.6984 # tate4 unrelaxed
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

h.trim(val=5e-4)
    

#kpoint info for high symmetry lines

kg = [24,24,24]

#                                                                 k-grid        #projection                                               smearing(eV)                               
energies, dos, pdos_metal, vals_grid, proj_metal_grid = ops.dos(h, kg, proj=orbs_metal, fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_metal_denseK_"+nstr+".pdf")

print("done dos")

kgrid = ops.generate_kgrid(kg)

nwan = h.nwan

outf = open("vals_grid_"+nstr+".csv", "w")
st = ""
for i in range(kg[0]):
    print("running ", i)
    for j in range(kg[1]):
        for k in range(kg[2]):
            n = k  + j * kg[1] + i * kg[1]*kg[2]
            st = ""
            st += str(i)+" "+str(j)+" "+str(k)+" "+str(kgrid[n][0])+" "+str(kgrid[n][1])+" "+str(kgrid[n][2])+" "
            for aa in range(nwan):
#                print(n, aa)
                st = st + str(vals_grid[n,aa])+" "
            st = st + "\n"
            

            outf.write(st)
            
outf.close()


print("done")
print()
