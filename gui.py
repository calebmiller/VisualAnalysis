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

def plotall():
	for i in range(len(tabs)):
		plot(i,tabs[i])

def BuildTabs():
	plots=NplotsEntry.get()
	for i in range(int(plots)):
		tabs[i] = ttk.Frame(tabControl) 
		tabControl.add(tabs[i], text ='Tab '+str(i)) 

	tabControl.pack(expand = 1, fill ="both") 

# the main Tkinter window 
root = tk.Tk() 

# setting the title 
root.title("Tab Widget") 
tabControl = ttk.Notebook(root) 

# dimensions of the main window 
root.geometry("500x500") 

tabs={}

#tab setup
maintab = ttk.Frame(tabControl) 
tabControl.add(maintab, text ='Main') 
plot_button1 = Button(maintab, command = lambda: plotall(), height = 2, width = 10, text = "Plot") 
plot_button1.pack() 
NplotsEntry= tk.Entry(maintab)
BTabs = Button(maintab, command = lambda: BuildTabs(), height = 2, width = 10, text = "BuildTabs") 
NplotsEntry.pack()
BTabs.pack()
tabControl.pack(expand = 1, fill ="both") 



# run the gui 

root.mainloop() 


