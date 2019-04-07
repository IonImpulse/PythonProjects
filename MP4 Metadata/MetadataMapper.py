import tkinter as tk
from tkinter import filedialog
import os
import sys
import subprocess
print("Select Video File:")
inputFile = filedialog.askopenfilename()
print("Select Metadata:")
inputData = filedialog.askopenfilename()
outputFile = str(inputFile)[:-3] + "Meta.mp4"
string = str("ffmpeg -i \"" + str(inputFile) + "\" -i \"" + str(inputData) + "\" -map_metadata 1 -codec copy \"" + str(outputFile)) + "\""
print(string)
subprocess.call(string, shell = True)
