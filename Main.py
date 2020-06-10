import SourceCode
import tkinter as tk

PyPlayer = tk.Tk()

background = tk.PhotoImage(file=".\\imgs\\background.png")

HEIGHT = background.height()
WIDTH = background.width()
PyPlayer.title("PyPlayer")
PyPlayer.geometry('%dx%d+0+0' % (WIDTH, HEIGHT))

Screen = tk.Frame(PyPlayer)
Screen.pack(fill="both", expand="yes")
background_label = tk.Label(Screen, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

entry = tk.Entry(Screen, font=40, exportselection=0, justify="center")
entry.place(relwidth=0.7, relheight=0.1, relx=0.15, rely=0.3)
 
play_button = tk.Button(Screen, text="Play Song", command=lambda: SourceCode.play(entry.get()), border=0, compound="top")
play_button.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.6)

stop_button = tk.Button(Screen, text="Stop Song", command=lambda: SourceCode.stop(), border=0, compound="top")
stop_button.place(relwidth=0.4, relheight=0.1, relx=0.3, rely=0.8)

PyPlayer.mainloop()