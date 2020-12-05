import pySALEPlot as psp
from pylab import figure,arange,colorbar
# Need this for the colorbars we will make on the mirrored plot
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Script to plot density and pressure for Ice example

# Output directory
dirname='./YldDam'
psp.mkdir_p(dirname)

# Open data file
model=psp.opendatfile('../Ice/jdata.dat')

# Set the distance units to mm
model.setScale('km')

# Set up a pylab figure
fig=figure()
ax=fig.add_subplot(111,aspect='equal')

# Loop over timesteps
for i in [0,1]:
	# set axis labels
	ax.set_xlabel('x [km]')
	ax.set_ylabel('y [km]')

	# set axis limits
	ax.set_xlim([-17.444,17.444])
	ax.set_ylim(model.yhires)

	# Read the time step i
	step=model.readStep(['Dam','Yld'],i)
	
	# Plot field
	p1=ax.pcolormesh(model.x,model.y,step.data[1]*1e-6,cmap='jet',vmin=0,vmax=10)
	p2=ax.pcolormesh(-model.x,model.y,step.data[0],cmap='jet',vmin=0,vmax=1)

	# add color bar
	if i == 0:

		# create colorbars to either side of the plot
        	divider = make_axes_locatable(ax)
        	cx1=divider.append_axes("right", size="5%", pad=0.7)
        	cx2=divider.append_axes("left", size="5%", pad=0.7)
		cb3=fig.colorbar(p1,cax=cx1)
		cb3.set_label('Yield Strength [MPa]')
		cb4=fig.colorbar(p2,cax=cx2)
		cb4.set_label('Damage')
		
		# set labels on left for left side colorbar
		cx2.yaxis.tick_left()
		cx2.yaxis.set_label_position('left')

	

	# set title
	ax.set_title('{: 5.2f} s'.format(step.time))
	
	# save the figure
	fig.savefig('{}/YldDam{:05d}.png'.format(dirname,i))

	# clear axis for next step
	ax.cla()