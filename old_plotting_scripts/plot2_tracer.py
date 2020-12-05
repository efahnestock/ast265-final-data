import pySALEPlot as psp
import matplotlib.pyplot as plt
import numpy as np

# This example plotting script designed to plot 
# a vertical pressure profile of the Chicxulub example

# Open the datafile
model=psp.opendatfile('../demo2D/jdata.dat')

# Set the distance units to mm
model.setScale('km')

# Set up a pyplot figure
fig = plt.figure(figsize=(20, 10))

ax=fig.add_subplot(111,aspect='equal')

# Set the axis labels
ax.set_xlabel('r [km]')
ax.set_ylabel('z [km]')

# Set the axis limits
ax.set_xlim(-10,10)
ax.set_ylim(-10,5)


# Read the time steps from the datafile
nstep=0
step0=model.readStep('TrM',0)
step1=model.readStep('TrM',10) #hint for future work

# Plot the pressure field
for u in range(model.tracer_numu): #loop over tracer clouds
    tstart = model.tru[u].start
    tend = model.tru[u].end
    scat = ax.scatter(step0.xmark[tstart:tend],step0.ymark[tstart:tend],
                      c=step0.TrM[tstart:tend],s=4,vmin=0,vmax=5)


cb=fig.colorbar(scat)
cb.set_label('Material Properties')

# Save the figure
fig.savefig('tracer.png')
