# importing library
from tkinter import *
from PIL import ImageTk, Image
import time


def loading_screen():

    w = Tk()

    #w.bind('<Enter>', w.destroy())
    # Using piece of code from old splash screen
    width_of_window = 430
    height_of_window = 250
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    x_coordinate = (screen_width/2)-(width_of_window/2)
    y_coordinate = (screen_height/2)-(height_of_window/2)
    w.geometry("%dx%d+%d+%d" %
               (width_of_window, height_of_window, x_coordinate, y_coordinate))
    # w.configure(bg='#ED1B76')
    w.overrideredirect(1)  # for hiding titlebar

    # new window to open

    Frame(w, width=430, height=250, bg='#272727').place(x=0, y=0)
    label1 = Label(w, text='POKEMON', fg='white', bg='#272727')  # decorate it
    # You need to install this font in your PC or try another one
    label1.configure(font=("Calamity Regular", 44, "bold"))
    #label1.place(x=10, y=75)

    labelPokemon = Label(w, text='O', fg='white', bg='#272727')
    labelPokemon.configure(font=("Pokemon pixels 1", 54, "bold"))
    #labelPokemon.place(x=150, y=50)

    label2 = Label(w, text='Loading...', fg='white',
                   bg='#272727')  # decorate it
    label2.configure(font=("Calibri", 11))
    label2.place(x=10, y=215)

    # making animation

    image_a = ImageTk.PhotoImage(Image.open('assets/c2.png'))
    image_b = ImageTk.PhotoImage(Image.open('assets/c1.png'))
    image_pokeball = ImageTk.PhotoImage(
        Image.open('assets/Pokeball2.png').resize((125, 125)))
    image_pokeball

    lp = Label(w, image=image_pokeball, border=0, bg='#272727',
               relief=SUNKEN).place(x=150, y=30)

    # animation
    for i in range(2):
        l1 = Label(w, image=image_a, border=0,
                   relief=SUNKEN).place(x=180, y=180)
        l2 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=200, y=180)
        l3 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=220, y=180)
        l4 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=240, y=180)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=180, y=180)
        l2 = Label(w, image=image_a, border=0,
                   relief=SUNKEN).place(x=200, y=180)
        l3 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=220, y=180)
        l4 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=240, y=180)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=180, y=180)
        l2 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=200, y=180)
        l3 = Label(w, image=image_a, border=0,
                   relief=SUNKEN).place(x=220, y=180)
        l4 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=240, y=180)
        w.update_idletasks()
        time.sleep(0.5)

        l1 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=180, y=180)
        l2 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=200, y=180)
        l3 = Label(w, image=image_b, border=0,
                   relief=SUNKEN).place(x=220, y=180)
        l4 = Label(w, image=image_a, border=0,
                   relief=SUNKEN).place(x=240, y=180)
        w.update_idletasks()
        time.sleep(0.5)

    w.destroy()


# loading_screen()
