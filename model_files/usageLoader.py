import sys

import pandas as pd
from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename

class usageLoader:
	"""
	Loads the usage data of the business being modelled
	"""
    def __init__(self):
        self.filename = None
        self.usage = None
    
    def load(self):
        # Load usage data
        self.root = tk()
        self.fileName = askopenfilename(title="Load Usage Data", filetypes=[('CSV file','.csv')])
        
        try:
            self.usage = pd.read_csv(self.fileName, encoding='latin-1')
        except Exception:
            print('Error loading usage data.')
            self.root.destroy()
            sys.exit()
        
        if self.validateUsage() == True:
            print('Usage data loaded.')
        else:
            print('Error: Usage data did not pass validation.')
        
        self.root.destroy()
    
    def validateUsage(self):
        # TODO: validate usage data
        return True
    
    def getUsage(self):
        return self.usage