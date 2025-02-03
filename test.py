import tkinter as tk
from tkinter import *
import subprocess
import threading

def speak_thread():
    text = textvab.get()
    if text.strip():
        try:
            subprocess.run(['espeak', text])
        except Exception as e:
            print(f"Error: {e}")

def speaknow():
    threading.Thread(target=speak_thread, daemon=True).start()

root = Tk()
obj = LabelFrame(root, text=" Write your Text! | TTS Tool", font=("Verdana", 17), bd=1)
obj.pack(fill="both", expand="yes", padx=20, pady=10)

lbl = Label(obj, text="Enter your text here! : ", font=("Verdana", 12))
lbl.pack(side=tk.LEFT, padx=10, pady=10)

textvab = StringVar()
text = Entry(obj, textvariable=textvab, width=50, font=("Verdana", 12))
text.pack(side=tk.LEFT, padx=10, pady=10)

btn = Button(obj, text="Speak", font=("Verdana", 12), command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

root.mainloop()