import tkinter as tk					 
from tkinter import ttk
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 



# plot function is created for 
# plotting the graph in 
# tkinter window 
def plot(slope,tmaster=None): 

	# the figure that will contain the plot 
	fig = Figure(figsize = (5, 5), dpi = 100) 

	# list of squares 
	y = slope*[i**2 for i in range(101)] 

	# adding the subplot 
	plot1 = fig.add_subplot(111) 

	# plotting the graph 
	plot1.plot(y) 

	# creating the Tkinter canvas 
	# containing the Matplotlib figure 
	canvas = FigureCanvasTkAgg(fig,tmaster) 
	canvas.draw() 

	# placing the canvas on the Tkinter window 
	canvas.get_tk_widget().pack() 

	# creating the Matplotlib toolbar 
	toolbar = NavigationToolbar2Tk(canvas,tmaster) 
	toolbar.update() 

	# placing the toolbar on the Tkinter window 
	canvas.get_tk_widget().pack() 

# the main Tkinter window 
root = tk.Tk() 

# setting the title 
root.title("Tab Widget") 
tabControl = ttk.Notebook(root) 

# dimensions of the main window 
root.geometry("500x500") 

#tab setup
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 

tabControl.add(tab1, text ='Tab 1') 
tabControl.add(tab2, text ='Tab 2') 
tabControl.pack(expand = 1, fill ="both") 

# button that displays the plot 
plot_button1 = Button(tab1, command = lambda: plot(1,tab1), height = 2, width = 10, text = "Plot") 
plot_button2 = Button(tab2, command = lambda: plot(2,tab2), height = 2, width = 10, text = "Plot") 

# place the button 
# in window 
plot_button1.pack() 
plot_button2.pack() 

# run the gui 

root.mainloop() 


