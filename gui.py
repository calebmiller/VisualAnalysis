import tkinter as tk
from VisualAnalysis import VisualAnalysis 
from tkinter import ttk
from tkinter import *
import matplotlib
matplotlib.use("Agg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Gui:
	def __init__(self, master):
		#create landing page
		#wait for user file input and settings
		#Buttons should call other functions for making other pages
		self.root=master
		self.tabControl=ttk.Notebook(master)
		self.root.geometry("700x700")
		self.tabs={}
		self.VA =VisualAnalysis()

		maintab=ttk.Frame(self.tabControl)
		self.tabControl.add(maintab,text='Main')
	
		plot_button1 = Button(maintab, command = lambda: self.Setup(), height = 2, width = 10, text = "Plot") #instead of plotall should call method which get's VA to draw
		plot_button1.pack()
		#	self.NplotsEntry= tk.Entry(maintab)
		#	BTabs = Button(maintab, command = lambda: self.BuildTabs(), height = 2, width = 10, text = "BuildTabs") #should query VA for number of plots
		#	self.NplotsEntry.pack()
		#	BTabs.pack()
		self.tabControl.pack(expand = 1, fill ="both")

	def UpdateLim(self,ax):
		lims = ax.viewLim
		xstart, xend = lims.intervalx
		self.VA.ApplyLimit(ax.get_title(), xstart,xend)
		ncols=self.VA.get_NCols()
		for i in range(int(ncols)):
			self.Plot(i,self.tabs[i])
	def Plot(self,col,tmaster=None): 
		# Get Fig fro VA
		fig = self.VA.get_hist(col)

		# creating the Tkinter canvas
		# containing the Matplotlib figure
		canvas = FigureCanvasTkAgg(fig,tmaster)
		canvas.draw()

		ax=fig.get_axes()[0]
		ax.set_xlabel(col)
		ax.callbacks.connect('xlim_changed',self.UpdateLim)	
	
		# placing the canvas on the Tkinter window
		canvas.get_tk_widget().pack()
	
		# creating the Matplotlib toolbar
		toolbar = NavigationToolbar2Tk(canvas,tmaster)
		toolbar.update()

		# placing the toolbar on the Tkinter window
		canvas.get_tk_widget().pack()

	def Setup(self):
		self.VA.load_data()
		ncols=self.VA.get_NCols()
		self.BuildTabs(ncols)
		for i in range(int(ncols)):
			self.Plot(i,self.tabs[i])
	def BuildTabs(self,ncols):
		for i in range(int(ncols)):
			self.tabs[i] = ttk.Frame(self.tabControl)
			self.tabControl.add(self.tabs[i], text ='Tab '+str(i))

		self.tabControl.pack(expand = 1, fill ="both")

	def ReadFileInput():
		#gets input filenames from user
		return 

	def MakePages():
		#sets up all the pages and passes frame to VA for plots
		return

	def Page():
		#default setup of 1 page
		# sets up layout, can be called iteratively to setup multiple pages
		return

	def MakeCuts():
		#reads all user cuts and passes to VA method
		return

	def Save():
		#calls VA save function
		return


root = tk.Tk()
gui = Gui(root)
root.mainloop()
