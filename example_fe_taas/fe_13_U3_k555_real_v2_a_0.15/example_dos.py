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

#h = wan_ham('tate4_relaxed_U1/qe_hr.dat') #load the hamiltonian
#nstr = "tate4_relaxed_U1"
#fermi = 11.9964 # tate4 unrelaxed
#orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]] #ta case    
#orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
#orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
#metal = "Ta"


h = wan_ham('qe_hr.dat') #load the hamiltonian
nstr = "fe_taas_relaxed"

fermi = 11.6764 # tate4 relaxed
orbital_info = [["S", 12, ["p"]], ["Fe", 2, ["d"]], ["Ta", 2, ["d"]]]

orbs_s = ops.get_orbitals(orbital_info, [["S"]], so=True)
orbs_fe = ops.get_orbitals(orbital_info, [["Fe"]], so=True)
orbs_ta = ops.get_orbitals(orbital_info, [["Ta"]], so=True)


h.trim(val=5e-4)
    

#kpoint info for high symmetry lines

kg = [24,24,24]

#                                                                 k-grid        #projection                                               smearing(eV)                               
energies, dos, pdos_metal, vals_grid, proj_metal_grid = ops.dos(h, kg, proj=orbs_ta, fermi=fermi, nenergy = 500, xrange=[-5,5], sig = 0.04, pdf="DOS_ta_denseK_"+nstr+".pdf")

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


points = ops.fermi_surf_3d(h, fermi, 24,24,24)

pts = np.array(points)

np.savetxt("fermi_points_3d.csv", pts)

x = pts[:,0]
y = pts[:,1]
z = pts[:,2]
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z,c=z)
plt.savefig("fermi_points_k.pdf")

plt.clf()

A = np.array(  [[5.741957115 ,  0.000000000,   0.000000000],[ -2.870978557 ,  4.972680729 ,  0.000000000], [  0.000000000 ,  0.000000000  ,12.178046146]])

B = 2 * np.pi * np.linalg.inv(A)
Bt = B.T

p2 = np.dot(pts, Bt)
x = p2[:,0]
y = p2[:,1]
z = p2[:,2]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(x,y,z,c=z)
plt.savefig("fermi_points_Bk.pdf")

plt.clf()


               



#plt.show()



print("done")
print()
