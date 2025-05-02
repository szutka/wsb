import requests
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk


root = tk.Tk()
root.title("NASAimages")
root.geometry("1000x800")

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=2)

input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

ttk.Label(input_frame, text="Podaj zapytanie: ").pack(side="left", padx=5)
entry = ttk.Entry(input_frame, width=40) #pole tekstowe do zapytania
entry.pack(side="left", padx=5)
ttk.Button(input_frame, text="Szukaj", command=search).pack(side="left", padx=5)

output_frame = ttk.LabelFrame(root, text="Wyniki")
output_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

log_frame = ttk.LabelFrame(root, text="Logi")
log_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
text_log = tk.Text(log_frame, width=40, height=30)
text_log.pack(fill="both", expand=True)

output_list = tk.Text(output_frame, width=60, height=15)
output_list.pack(fill="both", expand=True) #pole tekstowe rozszerza sie na cale miejsce w ramce

root.mainloop()