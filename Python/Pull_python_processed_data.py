
# coding: utf-8

# In[1]:


print("Pulling python processed data...")

import numpy as np
import pandas as pd
import sys, os, warnings, time, multiprocessing
from decimal import Decimal
from subprocess import Popen, PIPE

path_root_folder = sys.argv[1]
path_python_script = path_root_folder+'/Python/'
path_temp_folder = path_root_folder+'/Temp/'
path_LUT_folder = path_root_folder+'/LUTs/'

path_save_folder = sys.argv[2]
if path_save_folder[0]=="/":
    path_save_folder = path_save_folder[1:10000]
    
# append to python script path to cwd if not already present
if path_python_script not in sys.path:
    sys.path.append(path_python_script)

#import custom python libraries
import progress_bar_module as pgm


# In[23]:


#Load a data set
x = np.linspace(0,1).reshape(-1, 1)
y = x + np.random.normal(0,.1,len(x)).reshape(-1, 1) # dummy data of a line with random noisey data

# setup dummy progress bar and a dummy for loop
n_iterations = 10
progress_bar_window, progressbar = pgm.init_progress_bar_window(maxValue=n_iterations,
                                                                window_title = 'python running')
# run a dummy for loop
for i in range(n_iterations):
    
    progressbar["value"]=i
    progressbar.update() # Force an update of the GUI
    time.sleep(0.5) #Dummy sleep time
    
progress_bar_window.destroy()

print("Running linear regression...")
#do some kind of operation, here we just do basic linear regression
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(x, y)
y_pred = reg.predict(x)
print("...linear regression finished")

#compile all the data
df = pd.DataFrame()
df['x'] = x[:,0]
df['y_true'] = y
df['y_pred'] = y_pred


# In[25]:


filename_base = 'df_python_processed_data.csv'
df.to_csv(path_temp_folder+filename_base, index=False) # save in a temp folder so you can easily fetch from another program
df.to_csv(path_save_folder+filename_base, index=False) # save in the users prefered folder


# In[26]:


#if you need to run some other python program that you can't just load from the start:
# p = Popen([python_executable,
#        path_python_script+"your_next_python_program.py",
#        path_root_folder,
#        path_save_folder], stdin=PIPE, stdout=PIPE, stderr=PIPE)
# output, error = p.communicate(b"input data that is passed to subprocess' stdin")
# output = output.decode('ascii')
# error = error.decode('ascii')
# print(output)
# print(error)

