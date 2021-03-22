import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTk
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
import sklearn.datasets # for iris
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import root_pandas as rp #if we want to save as root_ntuple
from matplotlib import rc #for custom label formatting
'''Make larger axes labels for plots for papers and such'''
matplotlib.rcParams['text.usetex'] = False
matplotlib.rcParams["figure.titlesize"] = 30
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=20)
plt.rc('axes', titlesize=20)


class Gui:
    def __init__(self, master):

        #Visual analysis initiation
        self.base_data = self.load_data()
        
        ### GUI STUFF ###
        # Create a container
        self.master = master
        self.frame = tk.Frame(self.master)

        #label the text boxes
        self.label1 = tk.Label(self.frame, text='Plot1 xlims')
        self.label2 = tk.Label(self.frame, text='Plot2 xlims')
        self.label3 = tk.Label(self.frame, text='Plot3 xlims')
        self.label4 = tk.Label(self.frame, text='Plot4 xlims')
        # Create entry box
        self.lowerlim1 = tk.Entry(self.frame)
        self.upperlim1 = tk.Entry(self.frame)
        self.lowerlim2 = tk.Entry(self.frame)
        self.upperlim2 = tk.Entry(self.frame)
        self.lowerlim3 = tk.Entry(self.frame)
        self.upperlim3 = tk.Entry(self.frame)
        self.lowerlim4 = tk.Entry(self.frame)
        self.upperlim4 = tk.Entry(self.frame)
        # Create button
        self.button1 = tk.Button(self.frame,text="Plot1 Update",
                                        command=self.change_limits1)
        self.button2 = tk.Button(self.frame,text="Plot2 Update",
                                        command=self.change_limits2)
        self.button3 = tk.Button(self.frame,text="Plot3 Update",
                                        command=self.change_limits3)
        self.button4 = tk.Button(self.frame,text="Plot4 Update",
                                        command=self.change_limits4)
        self.button5 = tk.Button(self.frame,text="Reset plots",
                                        command=self.reset)
        self.button6 = tk.Button(self.frame,text="Save updated data",
                                        command=self.save)
        #pack widgets
        self.label1.grid(row=0,column=0)
        self.lowerlim1.grid(row=0,column=1)
        self.upperlim1.grid(row=0,column=2)
        self.button1.grid(row=0,column=3)
        self.label2.grid(row=0,column=4)
        self.lowerlim2.grid(row=0,column =5)
        self.upperlim2.grid(row=0, column = 6)
        self.button2.grid(row=0, column = 7)
        self.label3.grid(row=1, column = 0)
        self.lowerlim3.grid(row=1, column = 1)
        self.upperlim3.grid(row=1, column = 2)
        self.button3.grid(row=1, column = 3)
        self.label4.grid(row=1, column = 4)
        self.lowerlim4.grid(row=1, column = 5)
        self.upperlim4.grid(row=1, column = 6)
        self.button4.grid(row=1, column = 7)
        self.button5.grid(row = 2, column = 3,ipadx = 20, ipady = 20)
        self.button6.grid(row = 2, column = 5, ipadx = 20, ipady = 20)

        self.fig, self.ax = plt.subplots(2,2,figsize = (8,6))
        self.axs = [self.ax[0,0],self.ax[0,1],self.ax[1,0],self.ax[1,1]]
        for i in range(0,len(self.axs)):
            self.axs[i].hist(self.base_data[self.base_data.columns[i]],bins = 15, histtype = 'step',
                             range = (self.base_data[self.base_data.columns[i]].min()-0.5,self.base_data[self.base_data.columns[i]].max()+0.5),label = 'original')
            self.axs[i].set_xlabel(self.base_data.columns[i])
            self.axs[i].grid()
        #self.plot_histograms(self.base_data)
        #self.line, = self.ax.plot(range(10))
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig,self.master)
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        self.frame.pack()

    def change_limits1(self):
        xmin = self.lowerlim1.get()
        xmax = self.upperlim1.get()
        data = self.base_data
        zoom1 = data.loc[(data[data.columns[0]]>=float(xmin))&(data[data.columns[0]]<=float(xmax))]

        for i in range(0,len(self.axs)):
            self.axs[i].hist(zoom1[zoom1.columns[i]],bins = 15, histtype = 'step',
                             range = (self.base_data[self.base_data.columns[i]].min()-0.5,self.base_data[self.base_data.columns[i]].max()+0.5),label='reduced')
            #self.axs[i].set_xlabel(zoom1[zoom1.columns[i]])
            self.axs[i].grid()
        self.axs[0].set_xlim(float(xmin),float(xmax))
        self.axs[1].set_xlim(zoom1[zoom1.columns[1]].min()-0.5,zoom1[zoom1.columns[1]].max()+0.5)
        self.axs[2].set_xlim(zoom1[zoom1.columns[2]].min()-0.5,zoom1[zoom1.columns[2]].max()+0.5)
        self.axs[3].set_xlim(zoom1[zoom1.columns[3]].min()-0.5,zoom1[zoom1.columns[3]].max()+0.5)
        self.canvas.draw()
        return zoom1
        
    def change_limits2(self):
        xmin = self.lowerlim2.get()
        xmax = self.upperlim2.get()
        data = self.base_data
        zoom2 = data.loc[(data[data.columns[1]]>=float(xmin))&(data[data.columns[1]]<=float(xmax))]
        print(zoom2)
        for i in range(0,len(self.axs)):
            self.axs[i].hist(zoom2[zoom2.columns[i]],bins = 15, histtype = 'step',
                             range = (self.base_data[self.base_data.columns[i]].min()-0.5,self.base_data[self.base_data.columns[i]].max()+0.5),label='reduced')
            #self.axs[i].set_xlabel(zoom2[zoom2.columns[i]])
            self.axs[i].grid()
        self.axs[1].set_xlim(float(xmin),float(xmax))
        self.axs[0].set_xlim(zoom2[zoom2.columns[0]].min()-0.5,zoom2[zoom2.columns[0]].max()+0.5)
        self.axs[2].set_xlim(zoom2[zoom2.columns[2]].min()-0.5,zoom2[zoom2.columns[2]].max()+0.5)
        self.axs[3].set_xlim(zoom2[zoom2.columns[3]].min()-0.5,zoom2[zoom2.columns[3]].max()+0.5)
        self.canvas.draw()

        return zoom2
    def change_limits3(self):
        xmin = self.lowerlim3.get()
        xmax = self.upperlim3.get()
        data = self.base_data
        zoom3 = data.loc[(data[data.columns[2]]>=float(xmin))&(data[data.columns[2]]<=float(xmax))]
        print(zoom3)
        for i in range(0,len(self.axs)):
            self.axs[i].hist(zoom3[zoom3.columns[i]],bins = 15, histtype = 'step',
                             range = (self.base_data[self.base_data.columns[i]].min()-0.5,self.base_data[self.base_data.columns[i]].max()+0.5),label='reduced')
            #self.axs[i].set_xlabel(zoom3[zoom3.columns[i]])
            self.axs[i].grid()
        self.axs[2].set_xlim(float(xmin),float(xmax))
        self.axs[0].set_xlim(zoom3[zoom3.columns[0]].min()-0.5,zoom3[zoom3.columns[0]].max()+0.5)
        self.axs[1].set_xlim(zoom3[zoom3.columns[1]].min()-0.5,zoom3[zoom3.columns[1]].max()+0.5)
        self.axs[3].set_xlim(zoom3[zoom3.columns[3]].min()-0.5,zoom3[zoom3.columns[3]].max()+0.5)
        self.canvas.draw()

        return zoom3
    def change_limits4(self):
        xmin = self.lowerlim4.get()
        xmax = self.upperlim4.get()
        data = self.base_data
        zoom4 = data.loc[(data[data.columns[3]]>=float(xmin))&(data[data.columns[3]]<=float(xmax))]
        print(zoom4)
        for i in range(0,len(self.axs)):
            self.axs[i].hist(zoom4[zoom4.columns[i]],bins = 15, histtype = 'step',
                             range = (self.base_data[self.base_data.columns[i]].min()-0.5,self.base_data[self.base_data.columns[i]].max()+0.5),label='reduced')
            #self.axs[i].set_xlabel(zoom4[zoom4.columns[i]])
            self.axs[i].grid()
        self.axs[3].set_xlim(float(xmin),float(xmax))
        self.axs[0].set_xlim(zoom4[zoom4.columns[0]].min()-0.5,zoom4[zoom4.columns[0]].max()+0.5)
        self.axs[1].set_xlim(zoom4[zoom4.columns[1]].min()-0.5,zoom4[zoom4.columns[1]].max()+0.5)
        self.axs[2].set_xlim(zoom4[zoom4.columns[2]].min()-0.5,zoom4[zoom4.columns[2]].max()+0.5)
        self.canvas.draw()

        return zoom4
    ### VISUAL ANALYSIS STUFF###

    def load_data(self): #for now just use iris
        data = sklearn.datasets.load_iris(return_X_y=True, as_frame=True)[0] #loads as pandas dataframe
        data.columns = data.columns.str.replace(' ', '_') #replace spaces with underscores
        data.columns = data.columns.str.replace("_\(cm\)", '') #remove (cm)
        return data
    def plot_histograms(self,data):
        fig, ax = plt.subplots(2,2,figsize=(8,6))
        axs = [ax[0,0],ax[0,1],ax[1,0],ax[1,1]]
        for i in range(0,len(axs)):
            axs[i].hist(data[data.columns[i]])
            axs[i].set_xlabel(data.columns[i])
            axs[i].grid()
        return fig, axs

    def save_zoomed_data(self, df, path, filename, filetype = 'root'): #Default filetype is 'root'.
        df.to_root(path + filename+'.'+filetype, key='tree')

    def save(self):
        pass

    def reset(self):
        self.frame.destroy()
        self.canvas.get_tk_widget().destroy()
        self.__init__(self.master)
        #self.canvas.get_tk_widget().delete('all')
        #self.canvas.get_tk_widget().pack_forget()

root = tk.Tk()
gui = Gui(root)
root.mainloop()
