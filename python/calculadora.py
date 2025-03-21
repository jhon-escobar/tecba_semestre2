import tkinter as tk
from tkinter import messagebox

class Calculadora :
    def _init_(self,root):
        self.root = root
        self.root.root.title("calculadora")
        self.root.root.configure(bg="#2b2b2b")
        self.root.root.geometry(375*550)
        self.root.root.resizable(False,False)

        self.entrada = tk.Entry(root, width=17, font=('Arial',28), borderwidth=0, relief="solid", bg="#2b2b2b7", fg="white", justify="right")
        
        self.entrada.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=(10,5))
        
        self.crear_botones()

    def crear_botones(self):
        botones = [
         ('c',2), (' <-', 1)
          ]
      