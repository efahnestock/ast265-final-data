import pySALEPlot as psp
import matplotlib.pyplot as plt
import numpy as np

# Need this for the colorbars we will make on the mirrored plot
from mpl_toolkits.axes_grid1 import make_axes_locatable

# If viridis colormap is available, use it here
try:
    plt.set_cmap('viridis')
except:
    plt.set_cmap('YlGnBu_r')

# This example plotting script designed to plot 
# damage and pressure for the demo2D example

# Make an output directory
dirname = 'Plots'
psp.mkdir_p(dirname)

# Open the datafile
model = psp.opendatfile('./demo2D/jdata.dat')

# Set the distance units to km
model.setScale('km')

# Set up a pylab figure
fig = plt.figure(figsize=(8, 4))

ax = fig.add_subplot(111, aspect='equal')
divider = make_axes_locatable(ax)

# Loop over timesteps
for i in np.arange(0,210,10):

    # Set the axis labels
    ax.set_xlabel('r [km]')
    ax.set_ylabel('z [km]')

    # Set the axis limits
    ax.set_xlim([-15, 15])
    ax.set_ylim([-15, 5])

    # Read the time step 'i' from the datafile: 
    # read two or more fields by making a list of their abbreviations
    step=model.readStep(['Pre', 'Dam'],i)
    
    # -- the classic iSALEPlot mirrored setup. Plot the second field
    # -- using negative x values
    p1=ax.pcolormesh(model.x, model.y, step.data[1],
            cmap='Blues_r', vmin=0., vmax=1.)
    p2=ax.pcolormesh(-model.x, model.y, step.data[0],
            vmin=0, vmax=1.0E9)

    # Material boundaries
    ax.contour(model.xc, model.yc, step.cmc[0], levels=[0.5], colors='k', linewidths=1.)
    ax.contour(-model.xc, model.yc, step.cmc[0], levels=[0.5], colors='k', linewidths=1.)

    # Add colorbars; only need to do this once
    if i == 0: 
        # Right plot legend
        cx = divider.append_axes("right", size="5%", pad=0.7)
        cbr = fig.colorbar(p1, cax=cx)
        cbr.set_label(psp.longFieldName(step.plottype[1]))
        # Left plot legend
        cx = divider.append_axes("left", size="5%", pad=0.7)
        cbl = fig.colorbar(p2, cax=cx)
        cbl.set_label(psp.longFieldName(step.plottype[0]))
        # Need to set the labels on the left for this colorbar
        cx.yaxis.tick_left()
        cx.yaxis.set_label_position('left')

    ax.set_title('demo2D: T = {: 5.2f} s'.format(step.time))
    
    # Save the figure
    fig.savefig('{}/DamPre-{:05d}.png'.format(dirname, i), format='png', dpi=300)
    
    # Remove the field, ready for the next timestep to be plotted
    ax.cla()
