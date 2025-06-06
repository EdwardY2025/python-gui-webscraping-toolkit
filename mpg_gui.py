#!/usr/bin/env python3

# Edward Yeboah
# CSE 337 HW 5
# SBU ID: 114385084

import tkinter as tk
from tkinter import ttk

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()

        # Define string variables for text entry fields
        self.test = tk.StringVar()
        self.miles_driven = tk.StringVar()
        self.used_gallons = tk.StringVar()
        self.mpg = tk.StringVar()

        # Display the grid of components

        # Add padding to all components

        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles_driven).grid(
            column=1, row=1)

        ttk.Label(self, text="Gallons of Gas Used:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.used_gallons).grid(
            column=1, row=2)

        ttk.Label(self, text="Miles Per Gallon:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.mpg).grid(
            column=1, row=3)
        
        ttk.Button(self, text="Calculate", command=self.calculate).grid(column=0, row=4, sticky=tk.W)
        ttk.Button(self, text="Clear", command=self.clear).grid(column=1, row=4, sticky=tk.W)
            
        

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
        
    def calculate(self):
        distance = float(self.miles_driven.get())
        fuel = float(self.used_gallons.get())

        if distance == 0 or fuel == 0:
            self.mpg.set("Error")
            return

        mpg = distance / fuel

        self.mpg.set(f"{mpg:.2f}")


    def clear(self):
            self.miles_driven.set("")
            self.used_gallons.set("")
            self.mpg.set("")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fuel Efficiency Calculator")
    MyFrame(root)
    root.mainloop()
