import random
import tkinter as tk

genre = ["FPS", "Action", "Adventure", "Horror", "RPG", "MMORPG", "Stealth", "Puzzle", "Side-Scroller", "Platformer"]
main_character = ["Dragon", "Dog", "Bird", "Snail", "Cube", "Sphere", "Loner", "Swordsmen", "Chef", "Knight"]
objective = ["Capture the flag", "Search and Destroy", "Search and Rescue", "Survive", "Save Everyone",
             "Race the Clock", "Solve a Puzzle", "Escape", "Explore"]
HEIGHT = 700
WIDTH = 600
COLOR = "black"


# Button functionality
def genre_button(event):
    genre_label = tk.Label(root, text=random.choice(genre))
    genre_label.place(relx=0.413, rely=0.223, relheight=0.04, relwidth=0.173, anchor='n')


def character_button(event):
    character_label = tk.Label(root, text=random.choice(main_character))
    character_label.place(relx=0.413, rely=0.304, relheight=0.04, relwidth=0.173, anchor='n')


def goal(event):
    goal_label = tk.Label(root, text=random.choice(objective))
    goal_label.place(relx=0.413, rely=0.384, relheight=0.04, relwidth=0.173, anchor='n')


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="Video game characters.png")
background_label = tk.Label(canvas, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#ffffff', bd=5)
frame.place(relx=0.5, rely=0.22, relwidth=0.35, relheight=0.045, anchor='n')

frame2 = tk.Frame(root, bg='#ffffff', bd=5)
frame2.place(relx=0.5, rely=0.30, relwidth=0.35, relheight=0.045, anchor='n')

frame3 = tk.Frame(root, bg='#ffffff', bd=5)
frame3.place(relx=0.5, rely=0.38, relwidth=0.35, relheight=0.045, anchor='n')

button = tk.Button(frame, text="Genre", font=20)
button.bind("<Button-1>", genre_button)
button.place(relx=0.75, rely=0.03, relheight=1, relwidth=0.5, anchor='n')

button2 = tk.Button(frame2, text="Character", font=20)
button2.bind("<Button-1>", character_button)
button2.place(relx=0.75, rely=0.03, relheight=1, relwidth=0.5, anchor='n')

button3 = tk.Button(frame3, text="Objective", font=20)
button3.bind("<Button-1>", goal)
button3.place(relx=0.75, rely=0.03, relheight=1, relwidth=0.5, anchor='n')

label = tk.Label(canvas, text="Game Idea Generator", font=50)
label.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.5, anchor='n')

root.mainloop()
