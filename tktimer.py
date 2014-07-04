import tkinter as tk
import sys

tktimer = sys.modules[__name__]

class TkTimer:
	def __init__(self, app):
		self.app = app
		
	def interval(self, ms, f, *args):
		tktimer.interval(self.app, ms, f, *args)
		
	def timeout(self, ms, f, *args):
		tktimer.timeout(self.app, ms, f, *args)

def interval(app, ms, f, *args):
	def g():
		f(*args)
		app.after(ms, g)
	app.after(ms, g)
	
def timeout(app, ms, f, *args):
	def g():
		f(*args)
	app.after(ms, g)
