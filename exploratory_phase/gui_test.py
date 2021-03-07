import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTk
from matplotlib.figure import Figure

class Gui:
    def __init__(self, master):
        # Create a container
        self.master = master
        frame = tk.Frame(self.master)

        #label the text boxes
        self.label1 = tk.Label(frame, text='Plot1 xlims')
        self.label2 = tk.Label(frame, text='Plot2 xlims')
        self.label3 = tk.Label(frame, text='Plot3 xlims')
        self.label4 = tk.Label(frame, text='Plot4 xlims')
        # Create entry box
        self.lowerlim1 = tk.Entry(frame)
        self.upperlim1 = tk.Entry(frame)
        self.lowerlim2 = tk.Entry(frame)
        self.upperlim2 = tk.Entry(frame)
        self.lowerlim3 = tk.Entry(frame)
        self.upperlim3 = tk.Entry(frame)
        self.lowerlim4 = tk.Entry(frame)
        self.upperlim4 = tk.Entry(frame)
        # Create button
        self.button1 = tk.Button(frame,text="Plot1 Update",
                                        command=self.change_limits1)
        self.button2 = tk.Button(frame,text="Plot2 Update",
                                        command=self.change_limits2)
        self.button3 = tk.Button(frame,text="Plot3 Update",
                                        command=self.change_limits3)
        self.button4 = tk.Button(frame,text="Plot4 Update",
                                        command=self.change_limits4)
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

        self.fig, self.ax = plt.subplots(2,2,figsize=(6,5))
        axs = [self.ax[0,0],self.ax[0,1],self.ax[1,0],self.ax[1,1]]
        for i in range(0,len(axs)):
            axs[i].plot(range(10))
            axs[i].set_title("Plot %s"%(i+1))
        #self.line, = self.ax.plot(range(10))
        self.fig.tight_layout()
        self.canvas = FigureCanvasTkAgg(self.fig,self.master)
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        frame.pack()

    def change_limits1(self):
        xmin = self.lowerlim1.get()
        xmax = self.upperlim1.get()
        self.ax[0,0].set_xlim(float(xmin),float(xmax))
        self.canvas.draw()
        
    def change_limits2(self):
        xmin = self.lowerlim2.get()
        xmax = self.upperlim2.get()
        self.ax[0,1].set_xlim(float(xmin),float(xmax))
        self.canvas.draw()

    def change_limits3(self):
        xmin = self.lowerlim3.get()
        xmax = self.upperlim3.get()
        self.ax[1,0].set_xlim(float(xmin),float(xmax))
        self.canvas.draw()
        
    def change_limits4(self):
        xmin = self.lowerlim4.get()
        xmax = self.upperlim4.get()
        self.ax[1,1].set_xlim(float(xmin),float(xmax))
        self.canvas.draw()
    
root = tk.Tk()
gui = Gui(root)
root.mainloop()
