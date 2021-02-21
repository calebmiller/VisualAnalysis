import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
#from sklearn.decomposition import PCA
import pandas as pd
import math

# A class that will downsample the data and recompute when zoomed.
class LimitUpdater:
	def __init__(self,ph):
		self.placeholder=ph
	def update(self, ax):
   		# Update the line
		lims = ax.viewLim
		if abs(lims.width) > 1e-8:
			xstart, xend = lims.intervalx
			print(xstart)
			print(xend)
			ax.figure.canvas.draw_idle()


# import some data to play with
iris = datasets.load_iris()
df = pd.DataFrame()
df['sepal_length'] = iris['data'][:,0]
df['sepal_width'] = iris['data'][:,1]
df['petal_length'] = iris['data'][:,2]
df['petal_width'] = iris['data'][:,3]

fig, ax = plt.subplots(2, 2)
limupdate=LimitUpdater(0)

for x in range(len(df.columns)):
	df.hist(column = df.columns[x], bins = 12, ax=ax[math.floor(x/2),x%2], figsize=(20, 18)) #axes numbering is set up to loop over (0,0 to 1,1). If pages for plots, page num = math.floor(x/4)
	ax[math.floor(x/2),x%2].callbacks.connect('xlim_changed',limupdate.update)
	
plt.show()
