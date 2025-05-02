import requests
from tkinter import Tk, Toplevel, Label, Text, Button, Entry
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

class NASAimages:
    def __init__(self):
        self.api_url = "https://images-api.nasa.gov/search"

    def pobierzZdjecia(self, query):
        params = {'q': query}
        response = requests.get(self.api_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
