from tkinter import messagebox
from models.Pokemon import PokemonModel
from core.Controller import Controller


class PokedexController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.pokedexView = self.loadView("pokedex")
        self.pokemon = PokemonModel()

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        @Override
    """

    def main(self):
        self.pokedexView.main()

    def pokemon_button(self):
        self.pokedexView.make_bar(True)
        self.pokemon.getPokemon(self.pokedexView.text_id_name.get(1.0, "end-1c"), self.pokedexView.pokemon_image,
                                self.pokedexView.pokemon_identification, self.pokedexView.pokemon_types)
