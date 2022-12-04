from tkinter import *
from tkinter import ttk

def sub_window():
    sub_root = Tk()
    sub_root.title('S3 ls')
    sub_frame = ttk.Frame(sub_root, padding=16)
    sub_label = ttk.Label(sub_frame, text='S3バケット検索')

root = Tk()
root.title('AWS S3 CRUD')

frame1 = ttk.Frame(root, padding=16)
label1 = ttk.Label(frame1, text='Your name')
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(
    frame1,
    text='OK',
    command=lambda: sub_window()
)

frame1.pack()
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
button1.pack(side=LEFT)

root.mainloop()