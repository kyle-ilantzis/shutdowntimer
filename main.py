import tkinter as tk
import time
import subprocess

class App(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.action = tk.StringVar(value="S")
		self.createWidgets()
		self.initGrid()
		self.stop()
	
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
		self.radioShutdown = tk.Radiobutton(panel, text="Shutdown", value="S", variable=self.action, 
			fg="white", bg="black", activeforeground="green", activebackground="black", selectcolor="black")
		self.radioShutdown.grid(row=0)	
		self.radioHibernate = tk.Radiobutton(panel, text="Hibernate", value="H", variable=self.action, 
			fg="white", bg="black", activeforeground="green", activebackground="black", selectcolor="black")
		self.radioHibernate.grid(row=1)
		
		panel = tk.Frame(bottom, bg="black")
		panel.grid(row=0, column=3)
		panel.grid_rowconfigure(0, pad=2)
		panel.grid_rowconfigure(1, pad=2)
		self.btnStart = tk.Button(panel, text="Start", width=15, 
			fg="white", bg="black", activeforeground="green", activebackground="black",
			command=self.start)
		self.btnStart.grid(row=0)
		self.btnStop = tk.Button(panel, text="Stop", width=15,
			fg="white", bg="black", activeforeground="green", activebackground="black",
			command=self.stop)
		self.btnStop.grid(row=1)

	def initGrid(self):
		self.configure(bg="black")
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.grid(sticky=tk.NSEW)
		self.master.grid_rowconfigure(0, weight=1)		
		self.master.grid_columnconfigure(0, weight=1)
		
	def start(self):
		self.setState(tk.DISABLED)
		self.btnStop.configure(state=tk.NORMAL)
		
		self.durationTime = int(self.entry.get()) * 60
		self.startTime = time.time()
		
		self.showTimeLeft(self.durationTime)
		self.master.after(1000, self.tick)
	
	def stop(self):
		self.setState(tk.NORMAL)
		self.btnStop.configure(state=tk.DISABLED)
		
		self.startTime = 0
		self.showTimeLeft(0)
		
	def setState(self, s):
		self.entry.configure(state=s)
		self.radioShutdown.configure(state=s)
		self.radioHibernate.configure(state=s)
		self.btnStart.configure(state=s)
		self.btnStop.configure(state=s)
		
	def tick(self): 
		if not self.startTime: return
		
		progress = time.time() - self.startTime
		if progress > self.durationTime:
			self.quit()
		else:
			self.showTimeLeft(self.durationTime - progress)
			self.master.after(1000, self.tick)
			
	def showTimeLeft(self, seconds):
		seconds = int(seconds)
	
		h = seconds // (60 * 60)
		m = (seconds % (60 * 60)) // 60
		s = (seconds % (60 * 60)) % 60
		
		txt = ":".join(["{0:02d}".format(x) for x in [h,m,s]])
		
		self.time.configure(text=txt)
		
def main():
	root = tk.Tk()
	app = App(root)
	app.master.wm_title("KI Shutdown Timer v1.0")
	app.focus()
	
	app.mainloop()
	
	subprocess.call(
		["shutdown", "/f", "/s", "/t", "0"] if app.action.get() == "S" else ["shutdown", "/h"], 
		shell=True
	)
		
if __name__ == "__main__":	main()