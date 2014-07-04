import tkwevents
import tkinter as tk

class App(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.createWidgets()
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(3, weight=0)
		self.grid(sticky=tk.NSEW)
		master.grid_columnconfigure(0, weight=1, minsize=300)
		master.grid_rowconfigure(0, weight=1, minsize=200)		
	
	def createWidgets(self):	
	
		self.label = tk.Label(self, text="LABEL")
		self.label.grid(row=0, column=0, rowspan=2, columnspan=4, sticky=tk.NSEW)
		
		self.label2 = tk.Label(self, text="LABEL2")
		self.label2.grid(row=3, column=0)
		
		self.entry = tk.Entry(self)
		self.entry.grid(row=3, column=1, sticky=None)
		
		self.group = tk.Frame(self)
		self.group.grid(row=3, column=2)
		
		self.radio1 = tk.Radiobutton(self.group, text="RADIO1")
		self.radio1.grid(row=0)
	
		self.radio2 = tk.Radiobutton(self.group, text="RADIO2")
		self.radio2.grid(row=1)
		
		self.group2 = tk.Frame(self)
		self.group2.grid(row=3, column=3)
		
		self.btn1 = tk.Button(self.group2, text="BUTTON1")
		self.btn1.grid(row=0)
	
		self.btn2 = tk.Button(self.group2, text="BUTTON2")
		self.btn2.grid(row=1)
		# self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
		# self.msgListbox = tk.Listbox(self, yscrollcommand=self.scrollbar.set)	
		# self.onlineListbox = tk.Listbox(self)
		# self.entry = tk.Entry(self, validate="key", validatecommand=vcmd)		
		# self.scrollbar.config(command=self.msgListbox.yview)
		# self.entry.bind("<KeyRelease-Return>", self.send)		
		# self.scrollbar.grid(row=0, column=1, sticky=tk.NSEW)
		# self.msgListbox.grid(row=0, column=0, sticky=tk.NSEW)
		# self.onlineListbox.grid(row=0, column=2, sticky=tk.NSEW)
		# self.entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

	def update(self): pass

def main():
	
	setup = tkwevents.setup(App)
	setup.app.master.wm_title("TODO")
	setup.app.focus()

	# setup.interval(10000, setup.app.updateChatters);

	setup.mainloop()
		
if __name__ == "__main__":	main()