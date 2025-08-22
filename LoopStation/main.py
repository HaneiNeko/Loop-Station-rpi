"""
HaneiNeko
Loop Station
"""

from tkinter import *

root = Tk()
root.title("RPI-Looper3000")
root.geometry("800x480")
root.configure(bg='#121212')

# Frame that contains all the buttons
bottom_frame = Frame(root, bg='#121212')
bottom_frame.pack(side=BOTTOM, pady=65)

# Buttons in the frame, aligned horizontally
track1 = Button(bottom_frame, text="1", font=("Arrial", 30), width=2, bd=3, bg='#121212', fg='white',activebackground='#242424',activeforeground='white')
track1.pack(side=LEFT, padx=50)

track2 = Button(bottom_frame, text="2", font=("Arrial", 30), width=2, bd=3, bg='#121212', fg='white',activebackground='#242424',activeforeground='white')
track2.pack(side=LEFT, padx=50)

track3 = Button(bottom_frame, text="3", font=("Arrial", 30), width=2, bd=3, bg='#121212', fg='white',activebackground='#242424',activeforeground='white')
track3.pack(side=LEFT, padx=50)

track4 = Button(bottom_frame, text="4", font=("Arrial", 30), width=2, bd=3, bg='#121212', fg='white',activebackground='#242424',activeforeground='white')
track4.pack(side=LEFT, padx=50)

root.mainloop()
