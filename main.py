import tkwevents
import tkinter as tk

class App(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.createWidgets()
		self.configure(bg="black")
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.grid(sticky=tk.NSEW)
		master.grid_rowconfigure(0, weight=1, minsize=200)		
		master.grid_columnconfigure(0, weight=1, minsize=300)
	
	def createWidgets(self):	
	
		self.time = tk.Label(self, text="0:00", font=("Arial",72), fg="white", bg="black")
		self.time.grid(row=0, column=0, sticky=tk.NSEW)		
		
		bottom = tk.Frame(self, bg="black")
		bottom.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
		bottom.grid_columnconfigure(0, pad=5)
		bottom.grid_columnconfigure(1, pad=5)
		bottom.grid_columnconfigure(2, pad=5)
		bottom.grid_columnconfigure(3, pad=5)
		
		tk.Label(bottom, text="In x minutes", fg="white", bg="black").grid(row=0, column=0, sticky=tk.W)
		
		self.entry = tk.Entry(bottom)
		self.entry.grid(row=0, column=1, sticky=tk.EW)

		panel = tk.Frame(bottom, bg="black")
		panel.grid(row=0, column=2)		
		self.radioShutdown = tk.Radiobutton(panel, text="Shutdown", fg="white", bg="black")
		self.radioShutdown.grid(row=0)	
		self.radioHibernate = tk.Radiobutton(panel, text="Hibernate", fg="white", bg="black")
		self.radioHibernate.grid(row=1)
		
		panel = tk.Frame(bottom, bg="black")
		panel.grid(row=0, column=3)
		panel.grid_rowconfigure(0, pad=2)
		panel.grid_rowconfigure(1, pad=2)
		self.btnStart = tk.Button(panel, text="Start", width=15, fg="white", bg="black")
		self.btnStart.grid(row=0)
		self.btnStop = tk.Button(panel, text="Stop", width=15, fg="white", bg="black")
		self.btnStop.grid(row=1)


def main():
	
	setup = tkwevents.setup(App)
	setup.app.master.wm_title("TODO")
	setup.app.focus()

	# setup.interval(10000, setup.app.update);

	setup.mainloop()
		
if __name__ == "__main__":	main()