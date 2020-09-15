import tkinter as tk
import webbrowser

# Defining the window
root = tk.Tk()
root.title("WEB BROWSER")
root.geometry("450x300")


# defining the function
def fb():
    webbrowser.open_new("https://www.facebook.com/")


def yt():
    webbrowser.open_new("https://www.youtube.com/")


def ig():
    webbrowser.open_new("https://www.instagram.com/")


def ht():
    webbrowser.open_new("https://www.hotstar.com/")


def amz():
    webbrowser.open_new("https://www.amazon.com/")


def wtp():
    webbrowser.open_new("https://web.whatsapp.com/")


def ud():
    webbrowser.open_new("https://www.udemy.com/")

def search():
    word = x.get()
    Search = 'https://www.google.com/search?q=' + word
    webbrowser.open_new(Search)


# initializing the buttons

x = tk.StringVar()
b1 = tk.Button(root, text="Facebook", fg="white", bg="#3b5998", command=fb)
b2 = tk.Button(root, text="Youtube", fg="white", bg="#FF0000", command=yt)
b3 = tk.Button(root, text="Instagram", fg="white", bg="#C13584", command=ig)
b4 = tk.Button(root, text="Hotstar", fg="gold", bg="black", command=ht)
b5 = tk.Button(root, text="amazon", fg="white", bg="blue", command=amz)
b6 = tk.Button(root, text="Web Whatsapp", fg="white", bg="Green", command=wtp)
b7 = tk.Button(root, text="Search", fg="white", bg="#202020", command=search)
b8 = tk.Button(root, text="Udemy", fg="white", bg="red", command=ud).place(x=280, y=70, width=80, height=30)
# placing the buttons

b1.place(x=10, y=70, width=80, height=30)
b2.place(x=100, y=70, width=80, height=30)
b3.place(x=190, y=70, width=80, height=30)
b4.place(x=10, y=105, width=135, height=30)
b5.place(x=155, y=105, width=135, height=30)
b6.place(x=300, y=105, width=135, height=30)
b7.place(x=320, y=10, width=70, height=50)
e1 = tk.Entry(root, textvariable=x)
e1.place(x=10, y=10, width=300, height=50)
root.mainloop()
