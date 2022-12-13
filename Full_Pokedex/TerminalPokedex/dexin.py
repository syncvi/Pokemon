import curses
import pypokedex
import PIL.Image
import urllib3
import ascii_magic
from io import BytesIO
# from rich import print

ASCII_CHARS = [" ", "#", "@", "%", "?", "*", "+", ";", ":", ",", "."]
ASCII_LOGOS = [" ", "#", "@", "%", "?", "*", "+", " ", ":", ",", "."]


def writeShit(ascii_image):
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


def resize_image(image, new_width=80):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width*0.7 * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


def resize_pokemon(image, new_width=60):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * 0.5 * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return (characters)


def logo_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_LOGOS[pixel//25] for pixel in pixels])
    return (characters)


def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


def getPokemon(userInput, new_width=60):
    pokemon = pypokedex.get(dex=userInput)

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('shiny'))
    image = PIL.Image.open(BytesIO(response.data))

    newImageData = pixels_to_ascii(grayify(resize_pokemon(image)))
    pixel_count = len(newImageData)
    ascii_image = "\n".join([newImageData[index:(index+new_width)]
                            for index in range(0, pixel_count, new_width)])

    # newSize = image.resize((20, 20))

    # output = ascii_magic.from_image(
    #     newSize, columns=50, width_ratio=2.2, mode=ascii_magic.Modes.ASCII)

    # ascii_magic.to_terminal(output)
    return ascii_image
    # text = "dogpiss low"
    # return text


def getPokemonFlipped(userInput, new_width=60):
    pokemon = pypokedex.get(dex=userInput)

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.back.get('shiny'))
    image = PIL.Image.open(BytesIO(response.data))
    #image = old_image.transpose(method=PIL.Image.FLIP_LEFT_RIGHT)

    newImageData = pixels_to_ascii(grayify(resize_pokemon(image)))
    pixel_count = len(newImageData)
    ascii_image = "\n".join([newImageData[index:(index+new_width)]
                            for index in range(0, pixel_count, new_width)])

    # newSize = image.resize((20, 20))

    # output = ascii_magic.from_image(
    #     newSize, columns=50, width_ratio=2.2, mode=ascii_magic.Modes.ASCII)

    # ascii_magic.to_terminal(output)
    return ascii_image
    # text = "dogpiss low"
    # return text


def getPokemonInfo(userInput):
    pokemon = pypokedex.get(dex=userInput)
    info = ""
    info = "ID: " + str(pokemon.dex) + "\n" + "Name: " + \
        pokemon.name.capitalize() + "\n" + "Type: " + ", ".join(pokemon.types)

    return info


def getPokemonBio(userInput):
    pokemon = pypokedex.get(dex=userInput)
    pokemon_tuple = pokemon.base_stats
    (hp, attack, defense, sp_atk, sp_def, speed) = pokemon_tuple
    bio = ""
    bio = "Height: " + str(pokemon.height) + " " + \
        "Weight: " + str(pokemon.weight) + "\nBase Stats:\n" + \
        "Health: " + str(hp) + "\n" + "Attack: " + \
        str(attack) + "\n" + "Defense: " + \
        str(defense) + "\n" + "SP_ATK: " + str(sp_atk) + \
        "\n" + "SP_DEF: " + str(sp_def) + "\n" + "Speed: " + str(speed)

    return bio


def getLogo(new_width=80):
    image = PIL.Image.open("TerminalPokedex/logo.png")
    output = ascii_magic.from_image(resize_image(image))
    newImageData = logo_to_ascii(grayify(resize_image(image)))
    pixel_count = len(newImageData)
    ascii_image = "\n".join([newImageData[index:(index+new_width)]
                            for index in range(0, pixel_count, new_width)])

    return ascii_image


def getPokeball(new_width=60):
    image = """\
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠙⣿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⢿⣧⡀⠀⢠⣿⠟⠛⠛⠿⣿⡆⠀
⠀⢰⣿⣿⣿⣿⣿⣿⠿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠙⠿⠿⠟⠋⠀⠀⠀⣠⣿⠇⠀
⠀⢸⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⠟⠋⠀⠀
⠀⢸⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣾⠿⠛⠉⠀⠀⠀⠀⠀
⠀⠈⢿⣷⣤⣤⣄⣠⣤⣤⣤⣤⣶⣶⣾⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀
⠀⢸⣿⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀
⠀⠀⢻⣧⠀⠈⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⠀⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠟⠀⣠⣾⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢀⣤⣾⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣶⣦⣤⣤⣤⣤⣤⣤⣶⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
    # output = ascii_magic.from_image(resize_image(image))
    # newImageData = logo_to_ascii(grayify(resize_pokeball(image)))
    # pixel_count = len(image)
    # ascii_image = "\n".join([newImageData[index:(index+new_width)]
    #                         for index in range(0, pixel_count, new_width)])

    return image


def resize_pokeball(image, new_width=60):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width*0.75 * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)
