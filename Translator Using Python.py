import googletrans
from googletrans import Translator,LANGUAGES
import textblob
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("google translator")
root.geometry("1000x400")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.config(text=c)
    label2.config(text=c1)
    root.after(1000, label_change)


def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c2 = combo1.get()
        c3 = combo2.get()
        if text_:
            translator = Translator()
            translation = translator.translate(text_, src=c2, dest=c3)
            text2.delete(1.0, END)
            text2.insert(END, translation.text)
    except Exception as e:
        print(e)
        messagebox.showerror("googletrans", "please try again")


image_icon = PhotoImage(file="Google_Translate_icon.png")
root.iconphoto(False, image_icon)

# arrow_image=PhotoImage(file="convert-arrows-icon.png")
# image_label =Label(root,image=arrow_image,width=450)
# image_label.place(x=460,y=50)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="roboto 30", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="black", bd=5)
f.place(x=10, y=120, width=440, height=260)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=250)

scroll1 = Scrollbar(f)
scroll1.pack(side="right", fill="y")

scroll1.config(command=text1.yview)
text1.config(yscrollcommand=scroll1.set)

combo2 = ttk.Combobox(root, values=languageV, font="roboto 14", state="r")
combo2.place(x=630, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="roboto 30", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=550, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=550, y=120, width=440, height=260)

text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=250)

scroll2 = Scrollbar(f1)
scroll2.pack(side="right", fill="y")

scroll2.config(command=text2.yview)
text2.config(yscrollcommand=scroll2.set)

translate = Button(root, text="Translate", font="roboto 12 bold", activebackground="purple", cursor="hand2", bd=3,
                   bg="red", fg="white", command=translate_now)
translate.place(x=455, y=250)

label_change()

root.config(bg="white")
root.mainloop()