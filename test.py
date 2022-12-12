from tkinter import *
from tkinter import filedialog


root = Tk()
root.title(":D")

def get_path():
    path = filedialog.askdirectory()


def download():
    pass


canvas = Canvas(root, width=600, height=350)
canvas.pack()

image = PhotoImage(file="youtube.png")
canvas.create_image(300, 80, image=image)

Label(root, text="Url:", font=("Arial", 12, "bold")).place(x=50, y=200, anchor="center")
Entry(root, width=50).place(x=277.5, y=200, anchor="center")

Label(root, text="Path:", font=("Arial", 12, "bold")).place(x=50, y=250, anchor="center")
Button(root, text="Select", font=("Arial", 8, "bold"), padx=10, pady=5, command=lambda: get_path()).place(x=125, y=250, anchor="w")

Label(root, text="Format:", font=("Arial", 12, "bold")).place(x=50, y=300, anchor="center")
Button(root, text="MP4", font=("Arial", 8, "bold"), padx=10, pady=5, command=lambda: download()).place(x=125, y=300, anchor="w")
Button(root, text="MP3", font=("Arial", 8, "bold"), padx=10, pady=5, command=lambda: download()).place(x=180, y=300, anchor="w")

root.mainloop()
