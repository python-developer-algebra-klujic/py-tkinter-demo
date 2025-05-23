import sys
import tkinter as tk
import constants as c


def on_btn_exit():
    root.destroy()


root = tk.Tk()
root.title('Tkinter Demo')
root.geometry('600x400')

lbl_title = tk.Label(root,
                     text='Hello World!',
                     font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE))
lbl_title.pack(padx=c.PAD_X_TITLE, pady=c.PAD_Y_TITLE)

lbl_subtitle = tk.Label(root,
                        text='Jednostavna Python tkinter aplikacija',
                        font=(c.FONT_FAMILY, c.FONT_SIZE_SUBTITLE))
lbl_subtitle.pack(padx=c.PAD_X_SUBTITLE, pady=c.PAD_Y_SUBTITLE)

btn_exit = tk.Button(root,
                     text='Exit',
                     font=(c.FONT_FAMILY, c.FONT_SIZE_NORMAL),
                     command=on_btn_exit)
btn_exit.pack(padx=c.PAD_X_NORMAL, pady=c.PAD_Y_NORMAL)




root.mainloop()
