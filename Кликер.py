from tkinter import *

root = Tk()
root.geometry("1280x720")
root.title("Кликер")
root['bg'] = "black"

#Созаем кнопку
click_button = Button(root,
                      bg = "crimson",
                      text = "press me",
                      fg = "#735184",
                      font = ("Comic Sans MS",13,"italic")
                      )
click_button.place(x = 615,y = 295)

#создаём label(Это надпись на экране)
lbl = Label(root,
            text = "Start",
            bg = "black",
            fg = "white",
            font = ("Comic Sans MS",20,"bold")
            )

lbl.pack()#label тоже надо закреплять




root.mainloop()