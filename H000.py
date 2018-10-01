"""
Created on Fri Sep 28 14:20:01 2018

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from netCDF4 import Dataset

#%% loading Data

# for all heights. 36m is row 11
time_SBL = np.arange(10,310,10) 
time_CBL = np.arange(30,630,30)

#H000
budget0 = np.load('budget0.npy')
height0 = budget0[:,1]
height_SBL = height0[:128] #0 t0 127 is one time step for all heights. To get 
#such a profile you have to identify the correct indices by multiplication.

budget0_360 = budget0[budget0[:,1] == 35.938]

#total_tke0 = budget0[:,2] #at all heights
#total_tke0_36 = budget0_360[:,2]

buoyancy0 = budget0[:,3]
buoyancy0_36 = budget0_360[:,3]

shear0 = budget0[:,4]
shear0_36 = budget0_360[:,4] 

transport0 = budget0[:,5]
transport0_36 = budget0_360[:,5]

pres0 = budget0[:,6]
pres0_36 = budget0_360[:,6]

dissipation0 = budget0[:,7]
dissipation0_36 = budget0_360[:,7]

#H001
budget1 = np.load('budget1.npy')
height1 = budget1[:,1]
budget1_360 = budget1[budget1[:,1] == 35.938]

#total_tke1 = budget1[:,2] #at all heights
#total_tke1_36 = budget1_360[:,2]

buoyancy1 = budget1[:,3]
buoyancy1_36 = budget1_360[:,3]

shear1 = budget1[:,4]
shear1_36 = budget1_360[:,4] 

transport1 = budget1[:,5]
transport1_36 = budget1_360[:,5]

pres1 = budget1[:,6]
pres1_36 = budget1_360[:,6]

dissipation1 = budget1[:,7]
dissipation1_36 = budget1_360[:,7]

#H002
budget2 = np.load('budget2.npy')
height2 = budget2[:,1]
budget2_360 = budget2[budget2[:,1] == 35.938]

#total_tke2 = budget2[:,2] #at all heights
#total_tke2_36 = budget2_360[:,2]

buoyancy2 = budget2[:,3]
buoyancy2_36 = budget2_360[:,3]

shear2 = budget2[:,4]
shear2_36 = budget2_360[:,4] 

transport2 = budget2[:,5]
transport2_36 = budget2_360[:,5]

pres2 = budget2[:,6]
pres2_36 = budget2_360[:,6]

dissipation2 = budget2[:,7]
dissipation2_36 = budget2_360[:,7]


#H003
budget3 = np.load('budget3.npy')
height3 = budget3[:,1]
budget3_360 = budget3[budget3[:,1] == 35.938]

#total_tke3 = budget3[:,2] #at all heights
#total_tke3_36 = budget3_360[:,2]

buoyancy3 = budget3[:,3]
buoyancy3_36 = budget3_360[:,3]

shear3 = budget3[:,4]
shear3_36 = budget3_360[:,4] 

transport3 = budget3[:,5]
transport3_36 = budget3_360[:,5]

pres3 = budget3[:,6]
pres3_36 = budget3_360[:,6]

dissipation3 = budget3[:,7]
dissipation3_36 = budget3_360[:,7]



#H007
budget7 = np.load('budget7.npy')
height7 = budget7[:,1]
height_CBL = height7[:96]
#budget7_360 = budget7[budget7[:,1] == 35.938]
tke7 = budget7[:,2] #resolved tke at all heights
#total_tke7_36 = budget7_360[:,2]
buoyancy7 = budget7[:,3]
#buoyancy7_36 = budget7_360[:,3]
shear7 = budget7[:,4]
#shear7_36 = budget7_360[:,4] 
transport7 = budget7[:,5]
#transport7_36 = budget7_360[:,5]
pres7 = budget7[:,6]
dissipation7 = budget7[:,7]
#dissipation7_36 = budget7_360[:,7]

#nc files
#row is the height profile so to select a time period you need to pick a row 
#and all the columns 
#H000
profile0 = Dataset('profiles.000.nc')
res_tke0 = profile0.variables['tker'][:] #at all heights 
sub_tke0 = profile0.variables['sbtke'][:]
thl_0 = profile0.variables['sbtke'][:]

res_tke0_36 = profile0.variables['tker'][:,12] #at 36m
sub_tke0_36 = profile0.variables['sbtke'][:,12]

#H001
profile1 = Dataset('profiles.001.nc')
res_tke1 = profile1.variables['tker'][:]
sub_tke1 = profile1.variables['sbtke'][:]

res_tke1_36 = profile1.variables['tker'][:,12] #at 36m
sub_tke1_36 = profile1.variables['sbtke'][:,12]

#H002
profile2 = Dataset('profiles.002.nc')
res_tke2 = profile2.variables['tker'][:]
sub_tke2 = profile2.variables['sbtke'][:]

res_tke2_36 = profile2.variables['tker'][:,12] #at 36m
sub_tke2_36 = profile2.variables['sbtke'][:,12]

#H003
profile3 = Dataset('profiles.003.nc')
res_tke3 = profile3.variables['tker'][:]
sub_tke3 = profile3.variables['sbtke'][:]

res_tke3_36 = profile3.variables['tker'][:,12] #at 36m
sub_tke3_36 = profile3.variables['sbtke'][:,12]

#H007
profile7 = Dataset('profiles.007.nc')
res_tke7 = profile7.variables['tker'][:]
sub_tke7 = profile7.variables['sbtke'][:]

res_tke7_36 = profile7.variables['tker'][:,12] #at 36m
sub_tke7_36 = profile7.variables['sbtke'][:,12]


#Calculation of total tke

total_tke0_36 = res_tke0_36 + sub_tke0_36
total_tke1_36 = res_tke1_36 + sub_tke1_36
total_tke2_36 = res_tke2_36 + sub_tke2_36
total_tke2_36 = res_tke3_36 + sub_tke3_36


#%% Plotting


#Part 1b - Plot resolved, sub-grid and total TKE as a function of time @ 36m height

#H000 with dx = 3.125m
plt.figure(1)
plt.plot(time_SBL,total_tke0_36, 'navy')
plt.plot(time_SBL,res_tke0_36, 'm')
plt.plot(time_SBL,sub_tke0_36, 'c')
plt.xlabel('time in minutes')
plt.ylabel('TKE in (m/s)^2')
plt.legend(('Total','Resolved','Sub-grid'),loc = 'best')
plt.title('Total, resolved & sub-grid Fluxes @ 36m for dx = dy = 3.125m')

#H001 with dx = 6.25m
plt.figure(2)
plt.plot(time_SBL,total_tke1_36, 'navy')
plt.plot(time_SBL,res_tke1_36, 'm')
plt.plot(time_SBL,sub_tke1_36, 'c')
plt.xlabel('time in minutes')
plt.ylabel('TKE in (m/s)^2')
plt.legend(('Total','Resolved','Sub-grid'),loc = 'best')
plt.title('Total, resolved & sub-grid Fluxes @ 36m for dx = dy = 6.25m')

#H002 with dx = 12.5m
plt.figure(3)
plt.plot(time_SBL,total_tke2_36, 'navy')
plt.plot(time_SBL,res_tke2_36, 'm')
plt.plot(time_SBL,sub_tke2_36, 'c')
plt.xlabel('time in minutes')
plt.ylabel('TKE in (m/s)^2')
plt.legend(('Total','Resolved','Sub-grid'),loc = 'best')
plt.title('Total, resolved & sub-grid Fluxes @ 36m for dx = dy = 12.5m')

#H003 with dx = 25m
plt.figure(4)
plt.plot(time_SBL,total_tke3_36, 'navy')
plt.plot(time_SBL,res_tke3_36, 'm')
plt.plot(time_SBL,sub_tke3_36, 'c')
plt.xlabel('time in minutes')
plt.ylabel('TKE in (m/s)^2')
plt.legend(('Total','Resolved','Sub-grid'),loc = 'best')
plt.title('Total, resolved & sub-grid Fluxes @ 36m for dx = dy = 25m')

ratio_0 = np.zeros((30))
ratio_1 = np.zeros((30))
ratio_2 = np.zeros((30))
ratio_3 = np.zeros((30))

for i in range(30):
    ratio_0[i] = np.divide(res_tke0_36[i]/total_tke0_36[i])
    ratio_1[i] = np.divide(res_tke1_36[i]/total_tke1_36[i])
    ratio_2[i] = np.divide(res_tke2_36[i]/total_tke2_36[i]) #index 1
    ratio_3[i] = np.divide(res_tke3_36[i]/total_tke3_36[i])
#ratio_3_min = np.argwhere(ratio_3 == np.min(ratio_0))

#Select a time period where resolved/total is minimum and plot for all heights
# index 1 =  @ 1:00:00 hr or 60 min

plt.figure(5) #do we do this for all runs?
plt.plot(sub_tke1[1,:],height_SBL)
plt.xlabel('Sub-grid TKE in (m/s)^2')
plt.ylabel('Height in m')
plt.title('Sub-grid Fluxes @ 1:00:00 hr for all heights for dx = dy = 6.25m')


#%% Exercise 2 - resolved TKE budget

#Part 2a - Let us take the first index here as well
#do we do this for all runs? and for what time?

plt.figure(6)
plt.plot(buoyancy0,height0)
plt.plot(shear0,height0)
plt.plot(transport0,height0)
plt.plot(pres0,height0)
plt.plot(dissipation0,height0)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')


plt.figure(7)
plt.plot(buoyancy0[128:256],height_SBL)
plt.plot(shear0[128:256],height_SBL)
plt.plot(transport0[128:256],height_SBL)
plt.plot(pres0[128:256],height_SBL)
plt.plot(dissipation0[128:256],height_SBL)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')

plt.figure(8)
plt.plot(buoyancy1,height0)
plt.plot(shear1,height0)
plt.plot(pres1,height0)
plt.plot(transport1,height0)
plt.plot(dissipation1,height0)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')


plt.figure(9)
plt.plot(buoyancy1[128:256],height_SBL)
plt.plot(shear1[128:256],height_SBL)
plt.plot(transport1[128:256],height_SBL)
plt.plot(pres1[128:256],height_SBL)
plt.plot(dissipation1[128:256],height_SBL)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')

plt.figure(10)
plt.plot(buoyancy2,height0)
plt.plot(shear2,height0)
plt.plot(transport2,height0)
plt.plot(pres2,height0)
plt.plot(dissipation2,height0)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')


plt.figure(11)
plt.plot(buoyancy2[128:256],height_SBL)
plt.plot(shear2[128:256],height_SBL)
plt.plot(transport2[128:256],height_SBL)
plt.plot(pres2[128:256],height_SBL)
plt.plot(dissipation2[128:256],height_SBL)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')

plt.figure(12)
plt.plot(buoyancy3,height0)
plt.plot(shear3,height0)
plt.plot(transport3,height0)
plt.plot(pres3,height0)
plt.plot(dissipation3,height0)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')


plt.figure(13)
plt.plot(buoyancy3[128:256],height_SBL)
plt.plot(shear3[128:256],height_SBL)
plt.plot(transport3[128:256],height_SBL)
plt.plot(pres3[128:256],height_SBL)
plt.plot(dissipation3[128:256],height_SBL)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')

#Part 2b

plt.figure(14)
plt.plot(buoyancy7,height7)
plt.plot(shear7,height7)
plt.plot(transport7,height7)
plt.plot(pres7,height7)
plt.plot(dissipation7,height7)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')

plt.figure(15)
plt.plot(buoyancy7[96:192],height_CBL)
plt.plot(shear7[96:192],height_CBL)
plt.plot(transport7[96:192],height_CBL)
plt.plot(pres7[96:192],height_CBL)
plt.plot(dissipation7[96:192],height_CBL)
plt.xlabel('TKE Budget')
plt.ylabel('Height in m')
plt.legend(('Buoyancy','Shear','Transport','Pressure Transport','Dissipation'), loc = 'best')
plt.title('TKE Budget Terms')
