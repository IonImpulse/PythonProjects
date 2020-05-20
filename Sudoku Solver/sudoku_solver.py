import math
import multiprocessing
import tkinter as tk
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()
clear = lambda: os.system('cls')

def clean_input(raw) :
    output = []
    for line in raw :
        output.append(line.replace("\n", "").replace("\r", ""))

    return output

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2

class SudokuSolver :

    def __init__(self) :
        inputFile = filedialog.askopenfilename(filetypes = (("Text File","*.txt"),("All files", "*.*")))

        with open(inputFile, mode="r") as f :
            raw_data = f.readlines()
        
        self.puzzle = clean_input(raw_data)
        self.dim = (len(self.puzzle), len(self.puzzle[0].split(",")))

        #Error checking section
        #Will check for two things: whether or not the puzzle is square
        #and whether or not the puzzle has a int root
        if self.dim[0] != self.dim[1] :
            print("Puzzle not square. Please use a square puzzle.")
            os._exit(1)
        
        if is_square(self.dim[0]) == False :
            print("Puzzle not a perfect square. Please us a perfect square puzzle.")
            os._exit(1)
        

    def print_puzzle() :
        print("-")

solver = SudokuSolver()

for i in solver.puzzle :
    print(i)