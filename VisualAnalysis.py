import uproot
import numpy as np
import pandas as pd
import sklearn.datasets # for iris
from matplotlib.figure import Figure

class VisualAnalysis:
	def __init__(self):
		#creates class, waits for GUI controls
		self.base_data=pd.DataFrame()
	def load_data(self,files=[],tree=""):
		df_collection={} #to store data from multiple files, unless we want to merge all dfs and make new coloumn describing source
		if bool(files) and bool(tree): # checks both are given, otherwise load iris
			for file in files:
				fin=uproot.open(file) #opens TFile
				tin=fin[tree] #gets TTree
				data=tin.arrays(library="pd") #converts all keys in tree to pandas arrays
				df_collection[file]=data #store by filename key
		else: # if no files passed in load default
			data = sklearn.datasets.load_iris(return_X_y=True, as_frame=True)[0] #loads as pandas dataframe
#			data.columns = data.columns.str.replace(' ', '_') #replace spaces with underscores
#			data.columns = data.columns.str.replace("_\(cm\)", '') #remove (cm)
			self.base_data=data
			return
		self.base_data=df_collection[files[0]] #return only first df for now
		return
	def get_hist(self,col):
		#return ax to plot
		#set up callbacks.connect to LimitUpdater
		ax=self.base_data.hist(column=self.base_data.columns[col], bins=12)		
#		print(type(ax[0][0]))
#		return
		fig=ax[0][0].get_figure()
		return fig	
	def get_NCols(self):
		#returns number of columns in df
		return len(self.base_data.columns)
	def LimitUpdater(self):
		#applys cuts
		#see InteractiveCutExample.py
		return
	def Save(self):
		#saves cut data to file 
		return
