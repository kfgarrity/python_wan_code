import numpy as np

from wan_ham import wan_ham
from ham_ops import ham_ops

import matplotlib
matplotlib.use('Agg')  #for turning off display and only using pdf or png output
import matplotlib.pyplot as plt 
import  sys

ops = ham_ops()



coords_small = """
Ta 0.000000000 0.000000000 0.750000000
Ta 0.000000000 0.000000000 0.250000000
Te 0.855602965 0.675470809 0.000000000
Te 0.144397035 0.324529191 -0.000000000
Te 0.855602965 0.324529191 0.500000000
Te 0.675470809 0.855602965 0.500000000
Te 0.675470809 0.144397035 -0.000000000
Te 0.324529191 0.855602965 -0.000000000
Te 0.324529191 0.144397035 0.500000000
Te 0.144397035 0.675470809 0.500000000
"""

coords_big = """
Ta 0.0   0.0   0.096700306
Ta 0.0   0.0   0.596700306
Ta 0.0   0.0   0.403299694
Ta 0.0   0.0   0.903299694
Ta 0.5   0.5   0.903298154
Ta 0.5   0.5   0.403298154
Ta 0.5   0.5   0.596701846
Ta 0.5   0.5   0.096701846
Ta 0.0   0.0   0.25
Ta 0.0   0.0   0.75
Ta 0.5   0.5   0.75
Ta 0.5   0.5   0.25
Ta 0.0   0.5   0.418101397
Ta 0.0   0.5   0.918101397
Ta 0.5   0.0   0.081898603
Ta 0.5   0.0   0.581898603
Ta 0.0   0.5   0.264244061
Ta 0.0   0.5   0.764244061
Ta 0.5   0.0   0.235755939
Ta 0.5   0.0   0.735755939
Ta 0.0   0.5   0.07009365
Ta 0.0   0.5   0.57009365
Ta 0.5   0.0   0.42990635
Ta 0.5   0.0   0.92990635
Te 0.938954278   0.843805124   0.999411567
Te 0.061045722   0.156194876   0.999411567
Te 0.938954278   0.156194876   0.499411567
Te 0.843805124   0.938954278   0.500588433
Te 0.843805124   0.061045722   0.000588433
Te 0.156194876   0.938954278   0.000588433
Te 0.156194876   0.061045722   0.500588433
Te 0.061045722   0.843805124   0.499411567
Te 0.438953204   0.343812818   0.000588699
Te 0.438953204   0.656187182   0.500588699
Te 0.343812818   0.438953204   0.499411301
Te 0.343812818   0.561046796   0.999411301
Te 0.656187182   0.438953204   0.999411301
Te 0.656187182   0.561046796   0.499411301
Te 0.561046796   0.343812818   0.500588699
Te 0.561046796   0.656187182   0.000588699
Te 0.419772679   0.835855214   0.002034332
Te 0.580227321   0.164144786   0.002034332
Te 0.419772679   0.164144786   0.502034332
Te 0.835855214   0.419772679   0.497965668
Te 0.835855214   0.580227321   0.997965668
Te 0.164144786   0.419772679   0.997965668
Te 0.164144786   0.580227321   0.497965668
Te 0.580227321   0.835855214   0.502034332
Te 0.919768861   0.335858421   0.997964185
Te 0.919768861   0.664141579   0.497964185
Te 0.335858421   0.919768861   0.502035815
Te 0.335858421   0.080231139   0.002035815
Te 0.664141579   0.919768861   0.002035815
Te 0.664141579   0.080231139   0.502035815
Te 0.080231139   0.335858421   0.497964185
Te 0.080231139   0.664141579   0.997964185
Te 0.835599659   0.920680516   0.168912758
Te 0.164400341   0.079319484   0.168912758
Te 0.835599659   0.079319484   0.668912758
Te 0.920680516   0.835599659   0.331087242
Te 0.920680516   0.164400341   0.831087242
Te 0.079319484   0.835599659   0.831087242
Te 0.079319484   0.164400341   0.331087242
Te 0.164400341   0.920680516   0.668912758
Te 0.335600284   0.420684909   0.831086029
Te 0.335600284   0.579315091   0.331086029
Te 0.420684909   0.335600284   0.668913971
Te 0.420684909   0.664399716   0.168913971
Te 0.579315091   0.335600284   0.168913971
Te 0.579315091   0.664399716   0.668913971
Te 0.664399716   0.420684909   0.331086029
Te 0.664399716   0.579315091   0.831086029
Te 0.334479952   0.425087293   0.169635367
Te 0.665520048   0.574912707   0.169635367
Te 0.334479952   0.574912707   0.669635367
Te 0.425087293   0.334479952   0.330364633
Te 0.425087293   0.665520048   0.830364633
Te 0.574912707   0.334479952   0.830364633
Te 0.574912707   0.665520048   0.330364633
Te 0.665520048   0.425087293   0.669635367
Te 0.834484935   0.925073654   0.830366029
Te 0.834484935   0.074926346   0.330366029
Te 0.925073654   0.834484935   0.669633971
Te 0.925073654   0.165515065   0.169633971
Te 0.074926346   0.834484935   0.169633971
Te 0.074926346   0.165515065   0.669633971
Te 0.165515065   0.925073654   0.330366029
Te 0.165515065   0.074926346   0.830366029
Te 0.332280847   0.929523316   0.163162803
Te 0.667719153   0.070476684   0.163162803
Te 0.332280847   0.070476684   0.663162803
Te 0.929523316   0.332280847   0.336837197
Te 0.929523316   0.667719153   0.836837197
Te 0.070476684   0.332280847   0.836837197
Te 0.070476684   0.667719153   0.336837197
Te 0.667719153   0.929523316   0.663162803
Te 0.832277872   0.429525149   0.836835218
Te 0.832277872   0.570474851   0.336835218
Te 0.429525149   0.832277872   0.663164782
Te 0.429525149   0.167722128   0.163164782
Te 0.570474851   0.832277872   0.163164782
Te 0.570474851   0.167722128   0.663164782
Te 0.167722128   0.429525149   0.336835218
Te 0.167722128   0.570474851   0.836835218
Te 0.845824562   0.435363223   0.167552262
Te 0.154175438   0.564636777   0.167552262
Te 0.845824562   0.564636777   0.667552262
Te 0.435363223   0.845824562   0.332447738
Te 0.435363223   0.154175438   0.832447738
Te 0.564636777   0.845824562   0.832447738
Te 0.564636777   0.154175438   0.332447738
Te 0.154175438   0.435363223   0.667552262
Te 0.345811423   0.935374793   0.832447797
Te 0.345811423   0.064625207   0.332447797
Te 0.935374793   0.345811423   0.667552203
Te 0.935374793   0.654188577   0.167552203
Te 0.064625207   0.345811423   0.167552203
Te 0.064625207   0.654188577   0.667552203
Te 0.654188577   0.935374793   0.332447797
Te 0.654188577   0.064625207   0.832447797
"""

coords1, types1 = ops.parse_coords(coords_small)
coords2, types2 = ops.parse_coords(coords_big)



#print(coords1)
#print(types1)

#coords_super = ops.coords_ordering(coords1, coords2, [1,1,2])
#print("cs")
#print(coords_super)

#ops.match_coords(coords1, coords2, [1,1,2])

orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]]]
supercell = [2,2,3]
nss = np.prod(supercell)
orbital_info_big = [["Ta", 2*nss, ["d"]], ["Te", 8*nss, ["p"]]]

match, match_orbs = ops.match_orbitals(coords1, coords2, supercell, orbital_info, orbital_info_big,True)


h = wan_ham('../qe_hr.dat') #load the hamiltonian
h_super_r = ops.reorganize_ham(h, match_orbs)


nstr = "tate4_cdw"
fermi = 8.3088 # tate4 relaxed

#orbital_info = [["Ta", 24, ["d"]], ["Te", 96, ["p"]]] #ta case    
#orbs_metal = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
#orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)

fermi_super = 8.45 # tate4 relaxed

###h_small = wan_ham('../small_nod/qe_hr.dat') #load the hamiltonian
h_small = wan_ham('../../small_nod/qe_hr.dat') #load the hamiltonian


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


#image, limits = ops.unfold_bandstructure(h_small, h_super_r,[2,2,3],kpts, yrange = [-3, 3], names = names, temp=0.02, fermi=fermi, pdfname="unfold_cdw.pdf", num_energies=300)
#ops.plot_image(image, limits, names=names, pdfname="unfold_cdw_image.pdf")
#np.savetxt("unfold_cdw_image.csv", image)
#plt.clf()


#orbital_info = [["Ta", 24, ["d"]], ["Te", 96, ["p"]]] #ta case    

orbital_info = [["Ta", 2, ["d"]], ["Te", 8, ["p"]], ["Ta", 2, ["d"]], ["Te", 8, ["p"]], ["Ta", 2, ["d"]], ["Te", 8, ["p"]], ["Ta", 2, ["d"]], ["Te", 8, ["p"]], ["Ta", 2, ["d"]], ["Te", 8, ["p"]], ["Ta", 2, ["d"]], ["Te", 8, ["p"]]]

orbs_ta = ops.get_orbitals(orbital_info, [["Ta"]], so=True)
orbs_te = ops.get_orbitals(orbital_info, [["Te"]], so=True)
orbs_ta_dz2 = ops.get_orbitals(orbital_info, [["Ta", "dz2"]], so=True)
orbs_te_pz = ops.get_orbitals(orbital_info, [["Te", "pz"]], so=True)

ORBS = [orbs_ta,orbs_te,orbs_ta_dz2,orbs_te_pz]
    
#for fermi_adj in [0.0, -0.05, -0.1, -0.15]:
for fermi_adj in [0.0, 0.1, -0.1, 0.2, -0.2, 0.3, -0.3]:
    
    for ky in [0.0,0.25,0.5]:

        k, image2, image2proj = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi-fermi_adj, [-0.5,ky, -0.5], [1.0,0.0,0.0], [0.0,0.0,1.0], 50, 50, temp=0.04, PROJARR=ORBS)
        plt.clf()
        plt.imshow(image2, vmax = 8)
        image2 = image2 / np.max(image2)
        image2proj = image2proj / np.max(image2)
        print("min ", np.min(image2), " max ", np.max(image2))
        plt.xlabel("kz")
        plt.ylabel("kx")
        plt.title("ky_is_"+str(ky)+" fermi "+str(fermi_adj) )
        plt.savefig("fermi_unfold_cdw_2d_KY_is_"+str(ky)+"_kx_kz_50_fermi_"+str(fermi_adj)+".pdf")
        np.savetxt("fermi_unfold_cdw_2d_KY_is_"+str(ky)+"_kx_kz_50_fermi_"+str(fermi_adj)+".txt", image2)

        for pind in range(4):
            plt.clf()
            plt.imshow(image2proj[:,:,pind], vmax = 8)
            plt.xlabel("kz")
            plt.ylabel("kx")
            plt.title("ky_is_"+str(ky)+" fermi "+str(fermi_adj) )
            plt.savefig("fermi_unfold_cdw_2d_KY_is_"+str(ky)+"_kx_kz_50_fermi_"+str(fermi_adj)+"proj_"+str(pind)+".pdf")
            np.savetxt("fermi_unfold_cdw_2d_KY_is_"+str(ky)+"_kx_kz_50_fermi_"+str(fermi_adj)+"proj_"+str(pind)+".txt", image2proj[:,:,pind])


##exit()


#    k, image2 = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi, [-0.5,-0.5, 0.5], [0.0,1.0,0.0], [1.0,0.0, 0.0], 100, 100, temp=0.04)
#plt.clf()
#plt.imshow(image2, vmax = 8.0)
#plt.xlabel("kx")
#plt.ylabel("ky")
#plt.savefig("fermi_unfold_cdw_2d_KZ=0.5_kx_ky_100.pdf")
#np.savetxt("fermi_unfold_cdw_2d_KZ=0.5_kx_ky_100.txt", image2)



#k, image2 = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi, [0.0,-0.5,-0.5], [0.0,1.0,0.0], [0.0,0.0,1.0], 100, 100, temp=0.04)
#plt.clf()
#plt.imshow(image2)
#plt.xlabel("kz")
#plt.ylabel("ky")
#plt.savefig("fermi_unfold_cdw_2d_KX=0_ky_kz_100.pdf")
#np.savetxt("fermi_unfold_cdw_2d_KX=0_ky_kz_100.txt", image2)

#k, image2 = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi, [-0.5,0.5, -0.5], [1.0,0.0,0.0], [0.0,0.0,1.0], 100, 100, temp=0.04)
#plt.clf()
#plt.imshow(image2)
#plt.xlabel("kz")
#plt.ylabel("kx")
#plt.savefig("fermi_unfold_cdw_2d_KY=0.5_kx_kz_100.pdf")
#np.savetxt("fermi_unfold_cdw_2d_KY=0.5_kx_kz_100.txt", image2)

#exit()


#k, image2 = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi, [-0.5,-0.5, 0.0], [0.0,1.0,0.0], [1.0,0.0, 0.0], 100, 100, temp=0.04)
#plt.clf()
#plt.imshow(image2)
#plt.xlabel("kx")
#plt.ylabel("ky")
#plt.savefig("fermi_unfold_cdw_2d_KZ=0_kx_ky_100.pdf")
#np.savetxt("fermi_unfold_cdw_2d_KZ=0_kx_ky_100.txt", image2)

#k, image2 = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi, [-0.5,-0.5, 0.5], [0.0,1.0,0.0], [1.0,0.0, 0.0], 100, 100, temp=0.04)
#plt.clf()
#plt.imshow(image2)
#plt.xlabel("kx")
#plt.ylabel("ky")
#plt.savefig("fermi_unfold_cdw_2d_KZ=0.5_kx_ky_100.pdf")
#np.savetxt("fermi_unfold_cdw_2d_KZ=0.5_kx_ky_100.txt", image2)

#exit()

#k, image2 = ops.unfold_fermi_surf_2d(h_small, h_super_r,supercell,fermi, [-0.5,-0.5, 0.0], [0.0,1.0,0.0], [1.0,0.0, 0.0], 100, 100, temp=0.04)
#plt.clf()
#plt.imshow(image2)
#plt.xlabel("kx")
#plt.ylabel("ky")
#plt.savefig("fermi_unfold_cdw_2d_kx_ky100.pdf")
#np.savetxt("fermi_unfold_cdw_2d_kx_ky100.txt", image2)


#exit()

n = [24,24,24]
K, image_3d = ops.unfold_fermi_surf(h_small, h_super_r,supercell,n, temp=0.04, fermi=fermi)
dat = open("cdw_fermi_data.csv", "w")
for c1 in range(n[0]+1):
    for c2 in range(n[1]+1):
        for c3 in range(n[2]+1):
            st = str(c1)+ " " + str(c2)+ " " + str(c3)+ " " + str(K[c1,c2,c3,0])+ " " + str(K[c1,c2,c3,1])+ " " + str(K[c1,c2,c3,2])+ " " + str(image_3d[c1,c2,c3])+"\n"
            dat.write(st)

dat.close()





            #plt.imshow(image_3d[25,:,:])
#plt.savefig("fermi.pdf")

