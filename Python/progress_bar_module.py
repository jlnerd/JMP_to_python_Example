import tkinter as tk
from tkinter import *
from tkinter import ttk

def init_progress_bar_window(maxValue=100,window_title = 'Progress'):
    
    """
    initializes the progressbar variable and progress_bar_window
    
    Arguments:
        maxValue: The total length of the for loop
    Returns:
        progress_bar_window,progressbar
    Example:
        import progress_bar_module as pgm
        import time

        maxValue=100
        progress_bar_window, progressbar = pgm.init_progress_bar_window(maxValue=maxValue)

        for i in range(maxValue):
            time.sleep(.1)
            progressbar["value"]=i
            progressbar.update() # Force an update of the GUI
        progress_bar_window.destroy()
    """
    
    progress_bar_window = Tk()
    
    progressbar=ttk.Progressbar(progress_bar_window,orient="horizontal",length=300,mode="determinate")
    progressbar.pack(side=tk.TOP)
    progressbar.winfo_toplevel().title(window_title)

    currentValue=0
    progressbar["value"]=currentValue
    progressbar["maximum"]=maxValue
    
    return progress_bar_window, progressbar