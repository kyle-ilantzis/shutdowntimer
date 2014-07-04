import multiprocessing as mp 
import queue
import tkinter as tk
import time
import sys

tkwevents = sys.modules[__name__]

class TkweventsSetup:
	def __init__(self, app):
		self.app = app
		
	def interval(self, ms, f, *args):
		tkwevents.interval(self.app, ms, f, *args)
		
	def timeout(self, ms, f, *args):
		tkwevents.timeout(self.app, ms, f, *args)
		
	def mainloop(self):
		self.app.mainloop()

def interval(app, ms, f, *args):
	def g():
		f(*args)
		app.after(ms, g)
	app.after(ms, g)
	
def timeout(app, ms, f, *args):
	def g():
		f(*args)
	app.after(ms, g)
	
def setup(App):
	root = tk.Tk()
	app = App(root)
	return TkweventsSetup(app)
