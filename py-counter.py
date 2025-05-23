import tkinter as tk
import constants as c


counter = 0

def increase():
    global counter
    counter += 1
    lbl_counter.config(text=str(counter))


def decrease():
    global counter
    counter -= 1
    lbl_counter.config(text=str(counter))




root = tk.Tk()
root.title('Python Counter')
root.geometry('600x400')

lbl_title = tk.Label(root,
                     text='Py Counter',
                     font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE))
lbl_title.pack(padx=c.PAD_X_TITLE, pady=c.PAD_Y_TITLE)


btn_minus = tk.Button(root, text='-',
                      font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE),
                      command=decrease)
btn_minus.pack(padx=c.PAD_X_TITLE, pady=c.PAD_Y_TITLE,
               ipadx=c.PAD_Y_TITLE, ipady=c.PAD_Y_TITLE,
               side=tk.LEFT)

lbl_counter = tk.Label(root,
                       text='0',
                       font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE))
lbl_counter.pack(padx=c.PAD_X_TITLE, pady=c.PAD_Y_TITLE)

btn_plus = tk.Button(root, text='+',
                     font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE),
                     command=increase)
btn_plus.pack(padx=c.PAD_X_TITLE, pady=c.PAD_Y_TITLE,
              ipadx=c.PAD_Y_TITLE, ipady=c.PAD_Y_TITLE,
              side=tk.RIGHT)




root.mainloop()
