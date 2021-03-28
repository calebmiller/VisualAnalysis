import tkinter as tk
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class histmaker():
	def __init__(self):	
		self.df=pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
	def get_hist(self,col):
		ax=self.df.hist(column=self.df.columns[col], bins=12)	
		print(ax)	
		return ax[0][0].get_figure()


root = tk.Tk()

hm=histmaker()	
fig = hm.get_hist(1)

# creating the Tkinter canvas 
# containing the Matplotlib figure 
canvas = FigureCanvasTkAgg(fig,root) 
canvas.draw() 
# placing the canvas on the Tkinter window 
canvas.get_tk_widget().pack() 

root.mainloop()
