import pypokedex
from PIL import ImageTk, Image
import tkinter as tk
import urllib3
from io import BytesIO
import customtkinter as ctk
from rembg import remove


"""
    Responsible for 'Customers' database access
"""


class PokemonModel:
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        pass

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    def getPokemon(self, givenName, ImageLabel, IdLabel, TypeLabel):
        pokemon = pypokedex.get(name=givenName)

        http = urllib3.PoolManager()
        response = http.request('GET', pokemon.sprites.front.get('default'))
        image = Image.open(BytesIO(response.data))
        newSize = image.resize((150, 150))
        output = remove(newSize)

        img = ImageTk.PhotoImage(output)

        ImageLabel.configure(image=img)
        ImageLabel.image = img

        IdLabel.configure(text=f'{pokemon.dex} - {pokemon.name}')
        TypeLabel.configure(text=' | '.join([t for t in pokemon.types]))
