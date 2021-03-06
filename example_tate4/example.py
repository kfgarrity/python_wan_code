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
vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-5, 5], names = names,  fermi=fermi, pdfname="band_struct_metal_"+nstr+".pdf")
plt.clf()
vals, projs_te   , name_info = ops.band_struct(h,kpts, proj=orbs_te, yrange=[-5, 5], names = names,  fermi=fermi, pdfname="band_struct_"+nstr+".pdf")
plt.clf()

np.savetxt("vals_bandstruct_"+nstr+".csv", vals)
np.savetxt("proj_bandstruct_metal_"+nstr+".csv", projs_metal)
np.savetxt("proj_bandstruct_te_"+nstr+".csv", projs_te)
print("kpoint name_info")
print(name_info)
print()

#                                                                 k-grid        #projection                                               smearing(eV)                               
energies, dos, pdos_metal, vals_grid, proj_metal_grid = ops.dos(h, [12,12,12], proj=orbs_metal, fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_metal_"+nstr+".pdf")
plt.clf()
energies, dos, pdos_te, vals_grid, proj_te_grid  =    ops.dos(h, [12,12,12], proj=orbs_te   , fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_te_"+nstr+".pdf")
plt.clf()

np.savetxt("DOS_energies_"+nstr+".csv", energies)
np.savetxt("DOS_tot_"+nstr+".csv", dos)
np.savetxt("DOS_pdos_metal_"+nstr+".csv", pdos_metal)
np.savetxt("DOS_pdos_te_"+nstr+".csv", pdos_te)

np.save("DOS_vals_grid_"+nstr+".npy", vals_grid)
np.save("DOS_proj_grid_metal_"+nstr+".npy", proj_metal_grid)
np.save("DOS_proj_grid_te_"+nstr+".npy", proj_te_grid)

#this plots the fermi surface in 2D. in the kx-kz plane as a 50x50 grid
#                                                    zero point         axis1             axis2       n1   n2   smearing(eV)
IMAGE, VALS, points = ops.fermi_surf_2d(h, fermi, [-0.5,0.0, -0.5], [1.0, 0.0, 0.0], [0.0,0.0,1.0], 50, 50, 0.05)

np.savetxt("fermi_image_"+nstr+".csv", IMAGE)
np.save("fermi_image_VALS_"+nstr+".npy", VALS)

#this creates the image
plt.clf()

plt.imshow(IMAGE.T, origin="lower")
plt.savefig("fermi_surf.pdf")
plt.clf()


#now the plot the points only.
p = np.array(points)

np.savetxt("fermi_points_"+nstr+".csv", p)

plt.scatter(p[:,0], p[:,1], 5.0)
plt.ylim(-0.5,0.5)
plt.xlim(-0.5,0.5)

ax = plt.subplot()
ax.set_aspect('equal', adjustable='box')

plt.savefig("fermi_points_"+nstr+".pdf")
#plt.show()


print("done")
print()
