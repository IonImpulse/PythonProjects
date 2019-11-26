import csv
import tkinter as tk
from tkinter import filedialog
import os
import sys

clear = lambda: os.system('cls')
root = tk.Tk()
user = os.environ.get('USERNAME')
root.withdraw()

def progress(count, total, status=''):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()
