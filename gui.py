import tkinter as tk
import customtkinter as ctk
import backend as bk
import numpy as np
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation

animation_refresh_seconds=1
lenia = bk.Lenia()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def create_window():
    root=ctk.CTk()
    root.geometry("600x600")
    root.title("Gui")

    label=ctk.CTkLabel(root, text="Hello", font=('Roboto',30))
    label.pack(padx=10, pady=10)

    button = tk.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tk.BOTTOM)

    return root


def initialize_world():
    lenia.clear_world()
    lenia.load_cells(0)
    lenia.multiply_cells(12)
    lenia.calc_kernel()
    lenia.add_cells()
    fig, img = lenia.show_world(lenia.world, is_display=False)
    return fig, img

def create_canvas(root, fig):
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().pack()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

def animate(i):
    lenia.calc_once()
    img.set_array(lenia.world)
    return img,

fig, img = initialize_world()
root = create_window()
canvas = create_canvas(root, fig)
anim = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

root.mainloop()
