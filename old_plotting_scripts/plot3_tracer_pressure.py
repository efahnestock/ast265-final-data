import pySALEPlot as psp
import matplotlib.pyplot as plt
import numpy as np

# This example plotting script designed to plot 
# a vertical pressure profile of the Chicxulub example

# Open the datafile
model=psp.opendatfile('./demo2D/jdata.dat')

# Set the distance units to mm
model.setScale('km')

[model.tru[u].truInfo() for u in range(model.tracer_numu)]

# Set up a pyplot figure
fig = plt.figure(figsize=(20, 10))

ax=fig.add_subplot(111,aspect='equal')

# Set the axis labels
ax.set_xlabel('r [km]')
ax.set_ylabel('z [km]')

# Set the axis limits
ax.set_xlim(-10,10)
ax.set_ylim(-10,5)

sp_idx = 0
for i in range(1000):
    stp = model.readStep('TrM',i)
    if stp.time > 4.5:
        sp_idx = i
        break

print("Chose step {}".format(sp_idx))

# Read the time steps from the datafile
nstep=0
step0=model.readStep('TrM',0)
stepn=model.readStep('TrM',sp_idx)
stepPrT0 = model.readStep('TrP', 0)
stepPrT = model.readStep('TrP',sp_idx)
# Plot the pressure field
for u in range(model.tracer_numu): #loop over tracer clouds
    tstart = model.tru[u].start
    tend = model.tru[u].end
    scat = ax.scatter(stepPrT0.xmark[tstart:tend],stepPrT0.ymark[tstart:tend],
            c=stepPrT.TrP[tstart:tend]/1e9,s=4,vmin=0,vmax=max(stepPrT.TrP[tstart:tend]/1e9))

    scat2 = ax.scatter(-stepPrT.xmark[tstart:tend],stepPrT.ymark[tstart:tend],
            c=stepPrT.TrP[tstart:tend]/1e9,s=4,vmin=0,vmax=max(stepPrT.TrP[tstart:tend]/1e9))
    #scat2 = ax.scatter(-stepPrT0.xmark[tstart:tend],stepPrT0.ymark[tstart:tend],
    #        c=stepPrT.TrT[tstart:tend],s=4,vmin=0,vmax=3000)




cb=fig.colorbar(scat)
cb.set_label('Peak Pressure (GPa)')
cb2=fig.colorbar(scat2)
cb2.set_label('Peak Pressure (GPa)')
#cb2.set_label('Peak Temperature (K)')
ax.set_title('demo2D: T = {: 5.2f} s'.format(stepPrT.time))

# Save the figure
fig.savefig('./Plots/Figure7.2.png')
