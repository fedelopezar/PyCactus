import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from postcactus.simdir import SimDir
from postcactus import visualize as viz
from postcactus import grid_data as gd



# Sim dir:
sd = SimDir( "<simulation directory here>" )



# Func to plot:
func = 'rho'
minf = -9
maxf = 0
# Options:
dolog = 1
AMRboundaries = 1
cm = viz.get_color_map('viridis')
# Grid where to plot:
g = gd.RegGeom([400,400], [-10,-10], x1=[10,10])



# Get iterations and times, and loop
iters = sd.grid.xy.get_iters( func) 
times = sd.grid.xy.get_times( func) 
i = 0
for it in iters:
    print( "Plotting it = ", it )
    plt.clf()
    # Get data
    func_plot = sd.grid.xy.read(func, it, geom=g, order=1)
    if dolog != 0:
        func_plot = func_plot.log10()
    if AMRboundaries != 0 :
        rlvl = sd.grid.xy.read(func, it, geom=g, order=1, level_fill=True);
        lvl    = -0.5+np.arange(0,6);
        # Plot AMR boundaries
        viz.plot_contour(rlvl, levels=lvl);
    # Plot data and titles
    viz.plot_color( func_plot, bar=True, vmin=minf, vmax=maxf, cmap=cm, interpolation='bilinear')
    if dolog != 0:
        plt.title( 'log10 ' + func )
    else:
        plt.title( func )
    plt.title( 't = ' + str( round( times[i], 3) ), loc='right' )
    # Save fig
    it_label = str( it )
    it_label = (it_label.zfill(6))   
    if dolog != 0:
        plt.savefig( 'log10' + func + '_it=' + it_label + '.png' )
    else:
        plt.savefig( func + '_it=' + it_label + '.png' )
    i += 1


#print( sd.grid.x.get_grid_spacing(0, 'rho') )
