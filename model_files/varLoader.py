import sys

import pandas as pd
from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename

class varLoader:
	"""
	Loads the user-specified variables the model relies on
	"""
    def __init__(self):
        self.filename = None
        self.varFile = None
        self.vars = None
    
    def load(self):
        # Load var file
        self.root = tk()
        self.fileName = askopenfilename(title="Load Model Variables", filetypes=[('CSV file', '.csv')])

        try:
            self.varFile = pd.read_csv(self.fileName, encoding='latin-1')
        except Exception:
            print('Error loading model variables.')
            self.root.destroy()
            sys.exit()
        
        self.vars = self.parseVars()
        
        if self.validateVars() == True:
            print('Model variables loaded.')
        else:
            print('Error: Model variables did not pass validation.')
        
        self.root.destroy()
    
    def parseVars(self):
        self.vars = {}
        for i in range(len(self.varFile)):
            self.vars[self.varFile.loc[i, 'var']] = self.varFile.loc[i, 'value']
    
    def validateVars(self):
        # TODO: validate model variables
        return True
    
    def getVars(self):
        return self.vars