import tkinter as tk
import constants as c



def increase():
    value = int(lbl_counter_var.get())
    lbl_counter_var.set(str(value + 1))


def decrease():
    value = int(lbl_counter_var.get())
    value -= 1
    lbl_counter_var.set(str(value))




root = tk.Tk()
root.title('Python Counter')
root.geometry('600x400')


lbl_title = tk.Label(root,
                     text='Py Counter',
                     font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE))
lbl_title.pack(padx=c.PAD_X_TITLE, pady=c.PAD_Y_TITLE)


frame_counter = tk.Frame(root)
frame_counter.pack()


btn_minus = tk.Button(frame_counter, text='-',
                      font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE),
                      command=decrease)
btn_minus.pack(padx=c.PAD_Y_TITLE, pady=c.PAD_Y_TITLE,
               ipadx=c.PAD_Y_TITLE, ipady=c.PAD_Y_TITLE,
               side=tk.LEFT)


lbl_counter_var = tk.StringVar(value='0')
lbl_counter = tk.Label(frame_counter,
                       textvariable=lbl_counter_var,
                       font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE))
lbl_counter.pack(padx=c.PAD_Y_TITLE, pady=c.PAD_Y_TITLE,
                 ipadx=c.PAD_Y_TITLE, ipady=c.PAD_Y_TITLE,
                 side=tk.LEFT)


btn_plus = tk.Button(frame_counter, text='+',
                     font=(c.FONT_FAMILY, c.FONT_SIZE_TITLE),
                     command=increase)
btn_plus.pack(padx=c.PAD_Y_TITLE, pady=c.PAD_Y_TITLE,
              ipadx=c.PAD_Y_TITLE, ipady=c.PAD_Y_TITLE,
              side=tk.LEFT)




root.mainloop()
