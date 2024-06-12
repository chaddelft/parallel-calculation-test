import numpy as np
import matplotlib.pyplot as plt
from IPython.lib.display import Audio
from IPython.display import clear_output
import time
import pickle
import os
import sys

np.set_printoptions(threshold=10000)

def setstyle(**kwargs):
    """ Function to set notebook style for dark theme
    
    Dark theme command: (reload page) (requires jupyter themes installed)
    !jt -t gruvboxd -tf ptsans -tfs 14 -nf ptsans -nfs 13 -fs 12 -ofs 11 -cellw 97%
    
     -t theme, -tf text font, -tfs -tf size, -fs code font size, -ofs output size
     -dfs pandas dataframe size, -mathfs latex size, -nfs notebook controls size
    """
    notebook = kwargs.get('notebook',0)
    if not notebook:
        get_ipython().run_line_magic('matplotlib', 'inline')
        plt.style.use('seaborn-darkgrid')
        # print(plt.style.available)
    else:
        get_ipython().run_line_magic('matplotlib', 'notebook')
        
def end_signal():
    """ A loud beet to signal cell finished exec.
    
    Example: do_things()
             end_signal()
             
    Dependency: from IPython.lib.display import Audio
    """
    framerate = 4410
    play_time_seconds = 2
    t = np.linspace(0, play_time_seconds, framerate * play_time_seconds)
    audio_data = 0.2 * np.sin(2 * np.pi * 300 * t)
    return Audio(audio_data, rate=framerate, normalize=False, autoplay=True)

#------------------- A progress Bar----------------------
class prog_bar_build():
    """A Progress bar
    
    Example:    prog_bar = prog_bar_build(n)
                for i in range(n):
                    prog_bar.print_stat(i)
                    
    Dependancy:
        from IPython.display import clear_output
        import time
    """
    def __init__(self,n, long=False):
        self.start_time = time.time()      # start time = init time
        self.div        = np.ceil(n / 20)  # bar length
        self.n          = n                # Total number of iterations
        self.long       = long
    
    def print_stat(self,i):                # i = Current number of iterations
        if i % self.div == 0 | self.long:
            rem_time = int( (time.time() - self.start_time) 
                           * (self.n / (i+1) - 1)); 
            rem_min = rem_time // 60;
            rem_sec = rem_time - 60 * rem_min;
            clear_output(wait=True);
            print(( '=' * int( (i+1) * 20 / self.n) + 
                    '-' * int( (self.n -i -1) * 20 / self.n) +
                    '   {:.2f}%'.format( (i+1) * 100 / self.n ) + 
                    f', remaining time: {rem_min} min {rem_sec} s'
                  ),flush=True)

    def __call__(self,i):
        self.print_stat(i)
            

def std_fig(size=(8,8), dpi=150):
	"""Standard size plt fig"""
	plt.figure(figsize=size, dpi=dpi)
	
	
def save_fig(text, obj=plt):
    """Use (plt/ax[i], ['Title','x_label','y_label','file_name'])"""
    if np.sum(obj == plt) == 1: obj = [plt.gca()];
        
    for i in range(len(obj)):
        obj[i].set_title( text[0][i])
        obj[i].set_xlabel(text[1][i])
        obj[i].set_ylabel(text[2][i])
        
    plt.savefig(text[3]+'.png', bbox_inches='tight') #bbox_inches='tight'
	
	
def savefig(name, dpi=300):
    plt.savefig("imgs/"+name, dpi=dpi)
        
def write_pickle(workdir, name, dict_write):
    try: os.remove(workdir + "/pickled_data/"+name+".pickle")
    except: print('')
    with open(workdir + '/pickled_data/' + name + '.pickle', 'wb') as file_to_write:
        pickle.dump(dict_write, file_to_write)
        
def read_pickle(name):
    with open(name + '.pickle', 'rb') as file_to_read:
        ret = pickle.load(file_to_read)
    return ret


def sel_workdir(azure=0):
    if azure:
        workdir = "/dbfs/FileStore/user/george.vitanov@tatasteeleurope.com"
    else:
        workdir = "/media/user/AME_20H2_(2021-04-01)/ALL/TS"
    sys.path.append(workdir)
    return workdir
#shows whole jupyter kernel command history
#%history -g

#%%javascript
#IPython.OutputArea.prototype._should_scroll = function(lines) {return false;}
#// do not create scrollable cells in notebook

#%%html
#<style> .widget-readout{ color:white; } </style>
#<!--- Set white text style ---> 
	
	




