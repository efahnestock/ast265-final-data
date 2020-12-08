import pySALEPlot as psp
import matplotlib.pyplot as plt
import numpy as np


# This example plotting script designed to plot 
# a vertical pressure profile of the Chicxulub example

# Open the datafile
#model=psp.opendatfile('/media/sf_Public/data/job-1_6km/jdata.dat')
model=psp.opendatfile('./data/job-9i/jdata.dat')

# Set the distance units to mm
model.setScale('km')

[model.tru[u].truInfo() for u in range(model.tracer_numu)]

step0=model.readStep('TrM',0)
stepTrT0 = model.readStep('TrT', 0)

# Set up a pyplot figure
fig = plt.figure(figsize=(20, 10))

ax=fig.add_subplot(111,aspect='equal')

# Set the axis labels
ax.set_xlabel('r [km]')
ax.set_ylabel('z [km]')

# Set the axis limits
rad_km = 50
depth_km = 30
height_km = 10
ax.set_xlim(-rad_km,rad_km)
ax.set_ylim(-depth_km,height_km)
#stp = model.readStep('TrM',i)

# Read the time steps from the datafile
nstep=0
stepn=model.readStep('TrM',0)
# Plot the pressure field
for u in range(model.tracer_numu): #loop over tracer clouds
    tstart = model.tru[u].start
    tend = model.tru[u].end
    scat = ax.scatter(stepn.xmark[tstart:tend],stepn.ymark[tstart:tend],
                      c=stepn.TrM[tstart:tend],s=4,vmin=0,vmax=5)

    scat2 = ax.scatter(-stepn.xmark[tstart:tend],stepn.ymark[tstart:tend],
                      c=stepn.TrM[tstart:tend],s=4,vmin=0,vmax=5)


cb=fig.colorbar(scat)
cb.set_label('Material Properties')
for i in np.arange(0,5000,5):
    # Set up a pyplot figure
    ax.cla()
    rad_km = 40 
    depth_km = 15
    height_km =10
    ax.set_xlim(-rad_km,rad_km)
    ax.set_ylim(-depth_km,height_km)
    ax.set_xlabel("km")
    ax.set_ylabel("km")
    
    nstep=0
    stepn=model.readStep('TrM',i)
    #stepTrT = model.readStep('TrT',i)
    # Plot the pressure field
    for u in range(model.tracer_numu): #loop over tracer clouds
        tstart = model.tru[u].start
        tend = model.tru[u].end
        scat = ax.scatter(step0.xmark[tstart:tend],step0.ymark[tstart:tend],
                          c=step0.TrM[tstart:tend],s=4,vmin=0,vmax=5)

        scat2 = ax.scatter(-stepn.xmark[tstart:tend],stepn.ymark[tstart:tend],
                          c=stepn.TrM[tstart:tend],s=4,vmin=0,vmax=5)

        #scat2 = ax.scatter(-stepTrT.xmark[tstart:tend],stepTrT.ymark[tstart:tend],
        #        c=stepTrT.TrT[tstart:tend],s=4,vmin=0,vmax=3000)

    ax.set_title('Ice: T = {: 5.2f} s'.format(stepn.time))
    # Save the figure
    fig.savefig('./generatedPlots/Figure{:05d}.png'.format(i))
