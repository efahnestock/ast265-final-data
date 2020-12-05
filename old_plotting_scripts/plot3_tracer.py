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
stepTrT0 = model.readStep('TrT', 0)
stepTrT = model.readStep('TrT',sp_idx)
# Plot the pressure field
for u in range(model.tracer_numu): #loop over tracer clouds
    tstart = model.tru[u].start
    tend = model.tru[u].end
    scat = ax.scatter(step0.xmark[tstart:tend],step0.ymark[tstart:tend],
                      c=step0.TrM[tstart:tend],s=4,vmin=0,vmax=5)

    scat2 = ax.scatter(-stepn.xmark[tstart:tend],stepn.ymark[tstart:tend],
                      c=stepn.TrM[tstart:tend],s=4,vmin=0,vmax=5)
    #scat2 = ax.scatter(-stepTrT0.xmark[tstart:tend],stepTrT0.ymark[tstart:tend],
    #        c=stepTrT.TrT[tstart:tend],s=4,vmin=0,vmax=3000)




cb=fig.colorbar(scat)
cb.set_label('Material Properties (T=0)')
cb2=fig.colorbar(scat2)
cb.set_label('Material Properties (T={})'.format(stepn.time))
#cb2.set_label('Peak Temperature (K)')
ax.set_title('demo2D: T = {: 5.2f} s'.format(stepTrT.time))

# Save the figure
fig.savefig('./Plots/Figure7.1.png')
