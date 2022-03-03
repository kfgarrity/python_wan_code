import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

#matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()




h = wan_ham('qe_hr.dat') #load the hamiltonian
nstr = "tate4_cdw_NOSOC"
fermi = 8.2903 # tate4 relaxed
orbital_info = [["Ta", 24, ["d"]], ["Te", 96, ["p"]]] #ta case    
orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=False)
orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=False)


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
vals, projs_metal, name_info = ops.band_struct(h,kpts, yrange=[-5, 5], names = names,  fermi=fermi, pdfname="band_struct_NOPROJ_"+nstr+".pdf")
plt.clf()
vals, projs_metal, name_info = ops.band_struct(h,kpts, proj=orbs_metal, yrange=[-1.5, 0.5], names = names,  fermi=fermi, pdfname="band_struct_ZOOM_NOPROJ_"+nstr+".pdf")
plt.clf()
#exit()

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
energies, dos, pdos_metal, vals_grid, proj_metal_grid = ops.dos(h, [4,4,3], proj=orbs_metal, fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_metal_"+nstr+".pdf")
plt.clf()
energies, dos, pdos_te, vals_grid, proj_te_grid  =    ops.dos(h, [3,4,4], proj=orbs_te   , fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_te_"+nstr+".pdf")
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
IMAGE, VALS, points = ops.fermi_surf_2d(h, fermi, [-0.5,0.0, -0.5], [1.0, 0.0, 0.0], [0.0,0.0,1.0], 30, 30, 0.05)

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
