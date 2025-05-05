import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk #pillow, manipulacja obrazami
from io import BytesIO #latwe manipulowanie obrazami, traktowanie danych binarnych jako pliku w pamieic

class NASAimages:

    def __init__(self):
        self.api_url = "https://images-api.nasa.gov/search"

    def pobierzZdjecia(self, query):
        params = {'q': query}
        response = requests.get(self.api_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Nie można pobrać danych, kod: {response.status_code}")

    def showResults(self, data, limit=5):
        elements = data.get("collection", {}).get("items", [])

        if not elements:
            print("Nie znaleziono wyników")
            return []

        results = []
        for element in elements[:limit]:
            data_element = element.get("data", [])
            links = element.get("links", [])

            title = data_element[0].get("title", "Brak tytułu") if data_element else "Brak tytułu"
            link = links[0].get("href", "Brak linku") if links else "Brak linku"

            results.append((title, link))

        return results

def showImageFromUrl(url):
    response = requests.get(url)
    if response.status_code == 200:
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((400, 400))

        top = tk.Toplevel() #nowe okno
        top.title("Podgląd")
        tk_img = ImageTk.PhotoImage(img) #konwertujemy obraz
        label = tk.Label(top, image=tk_img)
        label.image = tk_img
        label.pack()
    else:
        print("Nie udało się załadować obrazka")

def search():
    query = entry.get()
    fetcher = NASAimages()

    try:
        data = fetcher.pobierzZdjecia(query)
        results = fetcher.showResults(data)

        output_list.delete(1.0, "end")  # Usuwamy stare wyniki z listy

        for widget in output_frame.winfo_children():
            if str(widget) != str(output_list):
                widget.destroy()

        if not results:
            output_list.insert("end", "Brak wyników.\n")
            return

        for i, (title, link) in enumerate(results, start=1):
            output_list.insert("end", f"{i}. {title}\n{link}\n\n")

            button = tk.Button(output_frame, text=f"Zobacz {title}", command=lambda url=link: showImageFromUrl(url))
            button.pack(padx=5, pady=5)

        text_log.insert("end", f"Sukces, pobrano {query}\n")

    except Exception as e:
        text_log.insert("end", f"Blad: {e}\n")

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

